#!/usr/bin/env python
import argparse
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description='Make plots',
                                     prog='results.py',
                                     formatter_class=argparse
                                     .ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--file", type=str, help='log file',
                        default='../trained_models/emotion_models/fer2013_emotion_training.log')
    args = parser.parse_args()

    results = pd.read_csv(args.file)
    results.rename(columns={'epoch': 'Epoch number', 'acc': 'Training Accuracy',
                            'val_acc': 'Test Accuracy',
                            'loss': 'Training Loss', 'val_loss': 'Test Loss'}, inplace=True)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    results.plot(x="Epoch number", y=["Training Accuracy", "Test Accuracy"],
                 ax=ax)
    plt.legend(loc='lower right')
    ax.set_xlabel("Epochs")
    ax.set_ylabel("Accuracy")
    plt.title("FER2013 emotion data set")
    fig.savefig("acc.png", bbox_inches='tight')

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    results.plot(x="Epoch number", y=["Training Loss", "Test Loss"],
                 ax=ax)
    plt.legend(loc='upper right')
    ax.set_xlabel("Epochs")
    ax.set_ylabel("Loss")
    plt.title("FER2013 emotion data set")
    fig.savefig("loss.png", bbox_inches='tight')


if __name__ == '__main__':
    main()
