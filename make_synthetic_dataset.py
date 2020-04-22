#!/usr/bin/env python

'''
This script generates 10 000 images and splits them in train/validation/test directories in 60%-20%-20% ratio.

Exactly 5000 images have upper left corner (10x10) completely black and they are named "<id>_stego.png". This represents the message "Yes".

Other 5000 images don't have that pattern in themselves and they are named "<id>_original.png". These images represent no message encoded.

The only difference between original and stego images are those 100 pixels.
'''
import cv2
import numpy as np

height = 100
width = 100

blank_image = np.zeros((height, width,3))

samples_required = 5000

training_treshold = 0
validation_treshold = 3000
test_treshold = 4000

# generate legit samples
for counter in range(samples_required):
    # generate a random image
    blank_image = np.random.rand(height,width,3)

    # show it  (for debugging purposes)
#    print(blank_image)
#    cv2.imshow('image', blank_image)
#    cv2.waitKey()


    # save it
    if counter > test_treshold:
        cv2.imwrite("data/test/" + str(counter) + '_original.png', blank_image*255)
    elif counter > validation_treshold:
        cv2.imwrite("data/validation/" + str(counter) + '_original.png', blank_image*255)
    else:
        cv2.imwrite("data/training/" + str(counter) + '_original.png', blank_image*255)

    # write the secret message..
    blank_image[0:20,0:20,:] = 0

    #for i in range(100):
    #    for j in range(50):
    #        for k in range(3):
    #            blank_image[i][j][k] = 0   

    # show it  (for debugging purposes)
#    print(blank_image)
#    cv2.imshow('image', blank_image)
#    cv2.waitKey()

    if counter > test_treshold:
        cv2.imwrite("data/test/" + str(counter) + '_stego.png', blank_image*255)
    elif counter > validation_treshold:
        cv2.imwrite("data/validation/" + str(counter) + '_stego.png', blank_image*255)
    else:
        cv2.imwrite("data/training/" + str(counter) + '_stego.png', blank_image*255)

