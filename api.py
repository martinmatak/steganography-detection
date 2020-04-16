import cv2

def total_number_of_training_samples():
    return 5

def total_number_of_validation_samples():
    return 2

def total_number_of_test_samples():
    return 7

def train_api(image_id, image_map, show_image=False):
    if image_map[image_id] == 'stegos':
        image = cv2.imread('./stegos/'+str(image_id)+'.png')
        label = 1
    elif image_map[image_id] == 'originals':
        image = cv2.imread('./originals/' + str(image_id) + '.png')
        label = 0
    if show_image:
        print("Press ENTER while the window with the image is focused to continue..")
        cv2.imshow(image_id, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return image, label

def valid_api(image_id, image_map, show_image=False):
    if image_map[image_id] == 'stegos':
        image = cv2.imread('./stegos/' + str(image_id) + '.png')
        label = 1
    elif image_map[image_id] == 'originals':
        image = cv2.imread('./originals/' + str(image_id) + '.png')
        label = 0
    return image, label

def test_api(image_id, image_map, show_image=False):
    if image_map[image_id] == 'stegos':
        image = cv2.imread('./stegos/' + str(image_id) + '.png')
        label = 1
    elif image_map[image_id] == 'originals':
        image = cv2.imread('./originals/' + str(image_id) + '.png')
        label = 0
    return image, label
