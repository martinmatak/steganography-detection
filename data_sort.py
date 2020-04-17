import os
import numpy as np
import pandas as pd
import shutil
import random
import argparse

def extract_dataset(data_dir:str, split:list=[.6, .2, .2], source:str='stegoappdb'):
    """
    This function takes the path of the extracted dataset from the StegoAppDB and sorts the images
    images are placed into the test, train, validation directories according to the supplied split param
    :param path: path to extracted dataset
    :param split: [train, test, split] ie [.6, .2, .2]
    :param source: source of dataset - default StegoAppDB
    """
    if not os.path.isdir(data_dir):
        print(f'Invalid Path: {data_dir}')
        return
    listdir = os.listdir(data_dir)
    # if source == 'stegoappb':
    steg_csv = [x for x in listdir if 'stego_directory.csv' in x][0]
    data_df = pd.read_csv(os.path.join(data_dir, steg_csv))
    # can change this later if want to include ALL stegos
    unique_inputs = list(set(data_df['cover_image_id']))
    test_len = int(len(unique_inputs)*split[1])
    valid_len = int(len(unique_inputs)*split[2])
    train_len = int(len(unique_inputs) - test_len - valid_len)
    print('train, test, valid', train_len, test_len, valid_len)
    # now move images to respective dirs based on unique inputs
    def sortimgs(cover_id, dir):
        #  stego img
        steg_subs = data_df[data_df['cover_image_id']==cover_id]
        rand_steg = steg_subs.iloc[np.random.randint(0, len(steg_subs))]
        steg_img = os.path.join(data_dir, 'stegos', str(rand_steg['image_filename']))
        new_steg = os.path.join(os.getcwd(), f'data/{dir}', str(rand_steg['image_id'])+'_stego.png')
        shutil.copy(steg_img, new_steg)
        # original cover img
        cover_img = os.path.join(data_dir, 'covers', str(cover_id)+'.PNG')
        new_cover_img = os.path.join(os.getcwd(), f'data/{dir}', str(rand_steg['image_id'])+'_original.png')
        shutil.copy(cover_img, new_cover_img)

    shuffled = np.random.permutation(len(unique_inputs))
    # sort test images to test dir
    for i in shuffled[:test_len]:
        img_id = unique_inputs[i]
        sortimgs(img_id, 'test')
    # sort validation imgs
    for i in shuffled[test_len:test_len+valid_len]:
        img_id = unique_inputs[i]
        sortimgs(img_id, 'validation')
    # sort training imgs
    for i in shuffled[test_len+valid_len:]:
        img_id = unique_inputs[i]
        sortimgs(img_id, 'training')


def get_args():
    parser = argparse.ArgumentParser(description="This script sorts and labels StegoAppDB dataset",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--data_dir", type=str, required=True,
                        help="path to model file (e.g. /Downloads/StegoAppDB_stegos_20200416-144427)")
    parser.add_argument("--split", type=list, default=[.6, .2, .2],
                        help="Train, test, validate split")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    extract_dataset(args.data_dir, args.split)


if __name__ == '__main__':

    main()
