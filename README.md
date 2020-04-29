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
## Generate Stego Images

```bash
usage: make_stegos.py [-h] [--input_dir INPUT_DIR] [--split SPLIT]
                [--embed_messages EMBED_MESSAGES]

This script generates stego images, and sorts them into train, test, val dirs

optional arguments:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR
                        directory of original images (no subdirs) (default:
                        None)
  --split SPLIT         Train, Test, Validation split (default: [0.6, 0.2,
                        0.2])
  --embed_messages EMBED_MESSAGES
                        list of messages to embed within the images, if None:
                        generates random 20 character str (default: None)

```

## StegoAppDB
Data can be downloaded from the StegoAppDB interface:

https://data.csafe.iastate.edu/StegoDatabase/
* First query the database for images matching desired characteristics
* Download the dataset
* Extract the images to any directory
* run data_sort.py to sort/split into train, test, validation directories

```bash
usage: data_sort.py [-h] --data_dir DATA_DIR [--split SPLIT]

The script shuffles, and splits the images in the data_dir, into the train, test, validation directories

required arguments:
  --data_dir DATA_DIR
                        path to extracted dataset
                             (e.g. /Downloads/StegoAppDB_stegos_20200416-144427)

optional arguments:
  -h, --help            show this help message and exit

  --split SPLIT
                        The split ratio for train, test, validation respecitvely 
                        (default: [.6, .2, .2])
```

#### Results 
 
![Image](chart.png?raw=true)
