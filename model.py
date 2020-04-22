from tensorflow.keras import models
from tensorflow.keras.layers import Dense, Flatten, MaxPooling2D, Conv2D, Dropout


def get_model(image_size):
    """
    :param image_size: Model will expect images with image_size x image_size dimensions.
    """
    model = models.Sequential()
    # feed forward neural network 
    # model.add(Dense(64, input_dim=image_size*image_size*3, activation='relu'))
    # model.add(Dropout(0.5))
    # model.add(Dense(64, activation='relu'))
    # model.add(Dropout(0.5))
    # model.add(Dense(1, activation='sigmoid'))
    # return model

    # VGG-like CNN

    # block 1
    model.add(Conv2D(16, (3, 3), input_shape=(image_size, image_size, 3), activation="relu"))
    model.add(Conv2D(16, (3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # block 2
    model.add(Conv2D(32, (3, 3), activation="relu"))
    model.add(Conv2D(32, (3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # block 3
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # block 4
    model.add(Conv2D(128, (3, 3), activation="relu"))
    model.add(Conv2D(128, (3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # block 5
    model.add(Conv2D(256, (3, 3), activation="relu"))
    model.add(Conv2D(256, (3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(500, activation="relu"))
    model.add(Dropout(rate=0.25))

    model.add(Dense(1, activation="sigmoid"))

    return model
