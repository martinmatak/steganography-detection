
def total_number_of_training_samples():
    return 5

def total_number_of_validation_samples():
    return 2

def train_api(image_id, show_image=False):
    image = None #TODO @Jane: Load based on image_id
    label = None #TODO @Jane: Load based on image_id
    if show_image:
        print("Press ENTER while the window with the image is focused to continue..")
        cv2.imshow(image_id, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return image, label

def valid_api(image_id, show_image=False):
    #Check train_api
    return 3,1
