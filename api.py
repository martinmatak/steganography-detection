import cv2

def total_number_of_training_samples():
    return 5

def total_number_of_validation_samples():
    return 2

def total_number_of_test_samples():
    return 7

def train_api(image_id, show_image=False):
    image = cv2.imread('sample.png') #TODO @Jane: Load based on image_id
    label = 1 #TODO @Jane: Load based on image_id
    if show_image:
        print("Press ENTER while the window with the image is focused to continue..")
        cv2.imshow(image_id, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return image, label

def valid_api(image_id, show_image=False):
    #TODO @Jane
    image = cv2.imread('sample.png')
    label = 1
    return image, label

def test_api(image_id, show_image=False):
    #TODO @Jane
    image = cv2.imread('sample.png')
    label = 1
    return image, label
