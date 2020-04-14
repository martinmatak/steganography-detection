import tensorflow as tf
import api

from tf.keras.optimizers import Adam
from generator import ImagesGenerator
from model import get_model
from pathlib import Path
from tf.keras.callbacks import LearningRateScheduler, ModelCheckpoint
import numpy as np
import argparse
from tf.keras import metrics
from plotter import plot_loss_history


def get_args():
    parser = argparse.ArgumentParser(description="This script trains a model for steganography detection",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--output_dir", type=str, default="out",
                        help="directory where the best model will be saved")
    parser.add_argument("--batch_size", type=int, default=32,
                        help="batch size")
    parser.add_argument("--nb_epochs", type=int, default=30,
                        help="number of epochs")
    parser.add_argument("--lr", type=float, default=0.001,
                        help="learning rate")
    args = parser.parse_args()
    return args


class Schedule:
    """
    Decreases learning rate of an optimizer over time.
    """
    def __init__(self, nb_epochs, initial_lr):
        self.epochs = nb_epochs
        self.initial_lr = initial_lr

    def __call__(self, epoch_idx):
        if epoch_idx < self.epochs * 0.25:
            return self.initial_lr
        elif epoch_idx < self.epochs * 0.50:
            return self.initial_lr * 0.2
        elif epoch_idx < self.epochs * 0.75:
            return self.initial_lr * 0.04
        return self.initial_lr * 0.008


def main():
    args = get_args()
    image_size = 224

    # prepare model for training
    model = get_model(image_size=image_size)
    model.compile(optimizer=Adam(), loss=tf.keras.losses.BinaryCrossentropy, metrics=[metrics.accuracy])
    model.summary()

    # prepare output directory
    output_dir = Path(__file__).resolve().parent.joinpath(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    callbacks = [LearningRateScheduler(schedule=Schedule(args.nb_epochs, initial_lr=args.lr)),
                 ModelCheckpoint(str(output_dir) + "/model.hdf5",
                                 monitor="val_loss",
                                 verbose=1,
                                 save_best_only=True,
                                 mode="min")
                 ]

    # load training and test data
    nr_of_training_samples = api.total_number_of_training_samples()
    nr_of_valid_samples= api.total_number_of_validation_samples()
    train_api = api.train_api
    valid_api = api.valid_api
    train_gen = ImagesGenerator(nr_of_training_samples, train_api, image_size=image_size, batch_size=args.batch_size)
    valid_gen = ImagesGenerator(nr_of_valid_samples, valid_api, image_size=image_size, batch_size=args.batch_size)

    # train model
    hist = model.fit_generator(generator=train_gen,
                               epochs=args.nb_epochs,
                               validation_data=valid_gen,
                               verbose=1,
                               callbacks=callbacks)

    # save loss history
    np.savez(str(output_dir.joinpath("history.npz")), history=hist.history)
    plot_loss_history(hist, output_dir)


if __name__ == "__main__":
    main()
