from keras import models
from keras.layers import core, pooling, Conv2D


def get_model(image_size):
    """
    :param image_size: Model will expect images with image_size x image_size dimensions.
    """
    model = models.Sequential()

    # block 1
    model.add(Conv2D(16, (3, 3), input_shape=(image_size, image_size, 3), activation="relu"))
    model.add(Conv2D(16, (3, 3), activation="relu"))
    model.add(pooling.MaxPooling2D(pool_size=(2, 2)))

    # block 2
    model.add(Conv2D(32, (3, 3), activation="relu"))
    model.add(Conv2D(32, (3, 3), activation="relu"))
    model.add(pooling.MaxPooling2D(pool_size=(2, 2)))

    # block 3
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(pooling.MaxPooling2D(pool_size=(2, 2)))

    # block 4
    model.add(Conv2D(128, (3, 3), activation="relu"))
    model.add(Conv2D(128, (3, 3), activation="relu"))
    model.add(pooling.MaxPooling2D(pool_size=(2, 2)))

    # block 5
    model.add(Conv2D(256, (3, 3), activation="relu"))
    model.add(Conv2D(256, (3, 3), activation="relu"))
    model.add(pooling.MaxPooling2D(pool_size=(2, 2)))

    model.add(core.Flatten())

    model.add(core.Dense(500, activation="relu"))
    model.add(core.Dropout(rate=0.5))
    model.add(core.Dense(100, activation="relu"))
    model.add(core.Dropout(rate=0.25))

    model.add(core.Dense(1))

    return model
