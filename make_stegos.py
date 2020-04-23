
from stegano import lsbset
from stegano import lsb
from stegano.lsbset import generators
import os
import numpy as np
import shutil
import argparse
from cv2 import imread, imwrite

def get_args():
    parser = argparse.ArgumentParser(description="This script generates stego images, and sorts them into train, test, val dirs",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input_dir", type=str,
                        help="directory of original images (no subdirs)")
    parser.add_argument("--split", type=list, default=[.6, .2, .2],
                        help="Train, Test, Validation split")
    parser.add_argument("--embed_messages", type=list, default=None,
                        help="list of messages to embed within the images, if None: generates random 20 character str")
    args = parser.parse_args()
    return args

def encr_img(imgpath:str, message:str, outpath:str):
    if not os.path.isfile(imgpath):
        print('Invalid Image Path')
        return
    # embed message
    # steg = lsb.hide(input_image=imgpath, message=message, auto_convert_rgb=True)
    steg = lsbset.hide(imgpath, message, generators.eratosthenes(), auto_convert_rgb=True)
    steg.save(outpath)

def decr_img(imgpath):
    # message = lsb.reveal(imgpath)
    message = lsbset.reveal(imgpath, generators.eratosthenes())
    return message

def generate_stegos(imagedir, messages:list=None, split:list=[.6, .2, .2]):
    imgs = [x for x in os.listdir(imagedir) if '.jpg' in x or '.png' in x]
    test_len = int(len(imgs)*split[1])
    val_len = int(len(imgs)*split[2])
    train_len = int(len(imgs)*split[0])
    chrs = list(tuple(chr(i) for i in range(32, 126) if chr(i).isprintable()))
    def sortimg(imgname, outpath):
        og_img = os.path.join(imagedir, imgname)
        cover = os.path.join(os.getcwd(), 'data', outpath, imgname.replace('.jpg', '.png').replace(".", "_original."))
        imwrite(cover, imread(og_img))
        steg = os.path.join(os.getcwd(), 'data', outpath, imgname.replace('.jpg', '.png').replace(".", '_stego.'))
        # cover = os.path.join(os.getcwd(), 'data', outpath, imgname.replace(".", "_original."))
        if not messages:
            msg = ''.join(np.random.choice(chrs, 20))
        else:
            msg = np.random.choice(messages)
        encr_img(cover, msg, steg)

    # split into test, val, and train directories
    for i in imgs[:test_len]:
        # do test
        sortimg(i, 'test')
    print(f'Test split: {test_len} stego images')

    for i in imgs[test_len:test_len+val_len]:
        # do valid
        sortimg(i, 'validation')
    print(f'Validation split: {val_len} stego images')

    for i in imgs[test_len+val_len:]:
        # do train
        sortimg(i, 'training')
    print(f'Train split: {train_len} stego images')

def main():
    args = get_args()
    generate_stegos(imagedir=args.input_dir, messages=args.embed_messages, split=args.split)


if __name__ == '__main__':
    main()
