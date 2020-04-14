import numpy as np
from keras.utils import Sequence
import cv2
import json


class ImagesGenerator(Sequence):
    """
    Class that loads data (image samples and ground truth values) that can be used by a model for training/validation.
    """

    def __init__(self, number_of_images, load_image_api, batch_size=32, image_size=224, show_image=False):
        """
        :param number_of_images: Total number of images.
        :param load_image_api: API that accepts n where n represents n-th image and returns image, label.                     
        :param batch_size: Number of samples per batch.
        :param image_size: Every image is resized to image_size x image_size
        :param show_image: Display loaded image before the image is preprocessed
        """
        self.image_num = number_of_images
        self.load_image_api = load_image_api
        self.batch_size = batch_size
        self.image_size = image_size
        self.indices = np.random.permutation(self.image_num)
        self.show_image = show_image

    def __len__(self):
        return self.image_num // self.batch_size

    def __getitem__(self, idx):
        batch_size = self.batch_size
        image_size = self.image_size

        x = np.zeros((batch_size, image_size, image_size, 3), dtype=np.float32)
        y = np.zeros((batch_size, 1), dtype=np.int32)

        sample_indices = self.indices[idx * batch_size:(idx + 1) * batch_size]

        for i, sample_id in enumerate(sample_indices):
            image, label = self.load_image_api(sample_id, self.show_image)
            x[i] = transform_image(image, image_size)
            y[i] = label

        return x, y

    def on_epoch_end(self):
        """
        Shuffles order of samples for the next epoch.
        """
        self.indices = np.random.permutation(self.image_num)

  
def transform_image(image, image_size):
    """
    :param image: original image
    :param image_size: returned image has dimensions image_size x image_size
    :return: resized image with pixel values in range [-1,1]
    """
    image = image.astype(np.float32)
    image -= 127.5
    image *= (1/127.5)
    return cv2.resize(image, (image_size, image_size))
