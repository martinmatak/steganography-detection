# Steganography Detection via DNN
Final Project for Network Security: Steganography detection via DNN <paper link here>

After installation of requirements, you should first train a model and then test it.

## Installation

0) Clone this repository.
1) (optional) Create virtual environment for python - execute `virtualenv -p python3 venv` and activate it by executing `source venv/bin/activate`.
2) Install requirements by executing `pip install -r requirements.txt`

## Training

```bash
python train.py 
```

Options:
```bash
usage: train.py [-h] [--output_dir OUTPUT_DIR] [--batch_size BATCH_SIZE] [--nb_epochs NB_EPOCHS] [--lr LR]

This script trains a model for steganography detection.

optional arguments:
  -h, --help                    show this help message and exit
  --output_dir  OUTPUT_DIR      directory where the best model will be saved (default: out)
  --batch_size  BATCH_SIZE      batch size (default: 32)
  --nb_epochs   NB_EPOCHS       number of epochs (default: 30)
  --lr          LR              learning rate (default: 0.001)
```

## Testing

```bash
usage: test.py [-h] --model_path MODEL_PATH [--show_image SHOW_IMAGE]

This script tests DNN used for steganography detection.

optional arguments:
  -h, --help            show this help message and exit
  --model_path MODEL_PATH
                        path to model file (e.g. /Downloads/model.hdf5)
                        (default: None)
  --show_image SHOW_IMAGE
                        Show the image for which prediction is computed
                        (default: False)
```

#### Results 
 
Add here graphs 
## StegoAppDB
Data can be downloaded from the StegoAppDB interface:

https://data.csafe.iastate.edu/StegoDatabase/

```bash
usage: extract_sort.py [-h] --model_path MODEL_PATH [--show_image SHOW_IMAGE]

This script tests DNN used for steganography detection.

optional arguments:
  -h, --help            show this help message and exit
  --model_path MODEL_PATH
                        path to model file (e.g. /Downloads/model.hdf5)
                        (default: None)
  --show_image SHOW_IMAGE
                        Show the image for which prediction is computed
                        (default: False)
```

