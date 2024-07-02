import cv2
import numpy as np
import os

def proc(Image, name):
    # Cargar la imagen en escala de grises
    image = cv2.imread(Image, cv2.IMREAD_GRAYSCALE)

    #-NOT USED FILTERS-#

    # Gaussian Blur
    #gaussian_Blur = cv2.GaussianBlur(image, (5, 5), 0)

    # Median Blur
    #median_Blur = cv2.medianBlur(image, 5)

    # Mean Filter
    #kernel = np.ones((5,5), np.float32) / 25
    #mean_Filter = cv2.filter2D(image, -1, kernel)

    # Laplacian Filter
    #laplacian_Filter = cv2.Laplacian(image, cv2.CV_64F)
    #laplacian_abs = cv2.convertScaleAbs(laplacian)

    # Binarization
    #_, binarized = cv2.threshold(gaussian_Blur, 185, 255, cv2.THRESH_BINARY)

    # Salt and Pepper
    #kernel = np.ones((2,2), np.uint8)
    #kernel2 = np.ones((2,2), np.uint8)
    #close = cv2.morphologyEx(binarized, cv2.MORPH_CLOSE, kernel)
    #open = cv2.morphologyEx(close, cv2.MORPH_OPEN, kernel2)

    # Dilatation
    #kernel = np.ones((2,2), np.uint8)
    #dilated = cv2.dilate(open, kernel, iterations = 1)
    #dilated2 = cv2.dilate(binarized, kernel, iterations = 1)

    #-PREPROCESSING-#

    # Bilateral Filter
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)
    
    # Adaptative Binarization
    binarized = cv2.adaptiveThreshold(bilateral, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)

    # Save the Results
    cv2.imwrite(f'Out/{name}', binarized)


# Original images's path
Path = '../dataset/img'
Images = [File for File in os.listdir(Path) if File.endswith(('.png', '.jpg', '.jpeg'))]

# Process all images
for img in Images:
    to_proc = os.path.join(Path, img)
    proc(to_proc, str(img))