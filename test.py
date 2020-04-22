from generator import ImagesGenerator
from tensorflow.keras.models import load_model

import argparse
from api import API

# only needed if you are running tf-GPU with cuda version that doesn't support >2.0
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)



def get_args():
    parser = argparse.ArgumentParser(description="This script tests DNN used for steganography detection.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--model_path", type=str, required=True,
                        help="path to model file (e.g. /Downloads/model.hdf5)")
    parser.add_argument("--show_image", type=bool, default=False,
                        help="Show the image for which prediction is computed")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    api = API()
    generator = ImagesGenerator(api.total_number_of_test_samples(), api.test_api, batch_size=1, show_image=args.show_image)
    model = load_model(args.model_path)

    for image, ground_truth in generator:
        print("prediction: ", model.predict(image))
        print("ground truth: ", ground_truth)
        print()

if __name__ == '__main__':
    main()
