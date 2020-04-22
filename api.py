import cv2
import ntpath
from pathlib import Path

class API():
    
    def __init__(self, data_path="data"):
        data_path = Path(data_path)
        self.training_samples = get_paths(data_path.joinpath("training"))
        self.validation_samples = get_paths(data_path.joinpath("validation"))
        self.test_samples = get_paths(data_path.joinpath("test"))

    def total_number_of_training_samples(self):
        return len(self.training_samples)

    def total_number_of_validation_samples(self):
        return len(self.validation_samples)

    def total_number_of_test_samples(self):
        return len(self.test_samples)

    def train_api(self, image_id, show_image=False):
        path = self.training_samples[image_id]
        return self._get_image_and_label(path)

    def valid_api(self, image_id, show_image=False):
        path = self.validation_samples[image_id]
        return self._get_image_and_label(path)

    def test_api(self, image_id, show_image=False):
        path = self.test_samples[image_id]
        return self._get_image_and_label(path)

     
    def _get_image_and_label(self, path, show_image=False):
        # extract image name from the path
        image_name = ntpath.basename(path)

        # extract label from image name
        if "stego" in image_name:
            label = 1
        elif "original" in image_name:
            label = 0
        else:
            raise Exception("File name not according to the convention")

        # load image in memory
        image = cv2.imread(path)

        # optionally, show the image
        if show_image:
            print("Press ENTER while the window with the image is focused to continue..")
            cv2.imshow(image_id, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return image, label


def get_paths(images_dir):
    # returns the full paths to all the images in the directory (not recursive)
    paths = []

    for image_path in images_dir.glob("*.png"):
        paths.append(str(image_path))
   
    return paths

