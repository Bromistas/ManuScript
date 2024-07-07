# ManuScript

A Latin manuscript deep learning transcriber

> Authors
>
> 1. [Karen Dianelis Cantero López C-411](https://github.com/karendcl)
> 2. [Luis Alejandro Rodríguez Otero C-411](https://github.com/Drackaro)
> 3. [Hector Miguel Rodríguez Sosa C-411](https://github.com/hmrguez)
> 4. [Sebastian Suárez Gómez C-411](https://github.com/sebas-suarez01)

## Introduction

ManuScript is a deep learning project aimed at transcribing Latin manuscripts. The project leverages the power of
Optical Character Recognition (OCR) to convert handwritten or printed text in Latin manuscripts into machine-encoded
text.

The project uses Python as the primary language and TensorFlow for implementing the deep learning model. The OCR model
is trained on a dataset of Italian letters called [LAM](https://www.kaggle.com/datasets/vpippi/lam-dataset/data),
allowing it to accurately transcribe the text.

## Installation

The project dependencies are listed in the `requirements.txt` file. To install these dependencies, use the following pip
command:

```bash
pip install -r requirements.txt
```

## Usage

In the image_preprocessing folder, more precisely the preprocessing_filters.py file, is a script ready to apply different kinds of
preprocessing filters to your dataset images. Read the documentation in the file to know how to use it.

Afterward the code relies on all the image dataset chosen for training, validation and testing will remain in the
image_preprocessing/Out folder.

All the code necessary to train and evaluate the model is in the `model/playground.ipynb` notebook. 