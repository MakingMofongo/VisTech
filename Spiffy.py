# function to preprocess image like by finding biggest contour and cropping it then using various filters with the goal of making text as sharp as possible and then removing any noise that apperared in the process
import cv2
import numpy as np
import pytesseract
import os
import easyocr
def thresholding(img):
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blur the image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # invert the image
    invert = cv2.bitwise_not(thresh)
    # extract the contours by cropping the image starting from biggest countour to next 5 countours
    
    # dilation and erosion to remove noise from invert
    kernel = np.ones((1,1), np.uint8)
    dilate = cv2.dilate(invert, kernel, iterations=1)
    erode = cv2.erode(dilate, kernel, iterations=1)
    
    return erode


# function to preprocess the image
def preprocess(img):
    # get the contour of the image
    thresh = thresholding(img)

    # display thresh
    # cv2.imshow('thresh', thresh)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return thresh

def easyocr(img):
    # easy ocr thresh image
    text1=easyocr.Reader(['en']).readtext(img)

    # take only the phrases from easy ocr output
    text1 = [i[1] for i in text1] # type: ignore
    # join the phrases
    text1 = ' '.join(text1)


    # print the text
    print(text1)

    # add text to original image
    cv2.putText(img, text1, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    list = [text1, img]
    return list


if __name__ == '__main__':
    # read the image
    img = cv2.imread('OCR_Test_Images/GVK-One.jpg')
    # preprocess the image
    thresh = preprocess(img)

    # easy ocr thresh image
    text1=easyocr.Reader(['en']).readtext(img)

    # take only the phrases from easy ocr output
    text1 = [i[1] for i in text1] # type: ignore
    # join the phrases
    text1 = ' '.join(text1)


    # print the text
    print(text1)

    # add text to original image
    cv2.putText(img, text1, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # display the image
    cv2.imshow('original', img)
    cv2.imshow('thresh', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()