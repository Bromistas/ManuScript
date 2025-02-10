import cv2
import numpy as np
import os


def processing_1(Image, name):
    """Bilateral Filter and Adaptative Binarization"""

    # Load the image in gray scale
    image = cv2.imread(Image, cv2.IMREAD_GRAYSCALE)

    # Bilateral Filter
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    # Adaptative Binarization
    # binarized = cv2.adaptiveThreshold(bilateral, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)

    # Save the Results
    cv2.imwrite(f'Out/{name}', bilateral)


def processing_2(Image, name):
    """Bilateral Filter, Adaptative Binarization and Dilatation"""

    # Load the image in gray scale
    image = cv2.imread(Image, cv2.IMREAD_GRAYSCALE)

    # Bilateral Filter
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    # Adaptative Binarization
    binarized = cv2.adaptiveThreshold(bilateral, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)

    # Dilatation
    kernel = np.ones((2, 2), np.uint8)
    dilated = cv2.dilate(binarized, kernel, iterations=1)

    # Save the Results
    cv2.imwrite(f'Out/{name}', dilated)


def processing_3(Image, name):
    """Bilateral Filter, Adaptative Binarization and Salt and Pepper Filter"""

    # Load the image in gray scale
    image = cv2.imread(Image, cv2.IMREAD_GRAYSCALE)

    # Bilateral Filter
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    # Adaptative Binarization
    binarized = cv2.adaptiveThreshold(bilateral, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)

    # Salt and Pepper
    kernel = np.ones((2, 2), np.uint8)
    kernel2 = np.ones((2, 2), np.uint8)
    close = cv2.morphologyEx(binarized, cv2.MORPH_CLOSE, kernel)
    open = cv2.morphologyEx(close, cv2.MORPH_OPEN, kernel2)

    # Save the Results
    cv2.imwrite(f'Out/{name}', open)


def processing_4(Image, name):
    """Bilateral Filter and Normal Binarization"""

    # Load the image in gray scale
    image = cv2.imread(Image, cv2.IMREAD_GRAYSCALE)

    # Bilateral Filter
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    # Binarization
    _, binarized = cv2.threshold(bilateral, 185, 255, cv2.THRESH_BINARY)

    # Save the Results
    cv2.imwrite(f'Out/{name}', binarized)


# Processing script

# Images's path
# Path = '../dataset/img'
Path = '../dataset/A'
Images = [File for File in os.listdir(Path) if File.endswith(('.png', '.jpg', '.jpeg'))]

# Process all images
for img in Images:
    to_proc = os.path.join(Path, img)
    # Select the processing(s) to apply
    processing_1(to_proc, str(img))