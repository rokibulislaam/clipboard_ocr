import numpy as np
import pytesseract

from PIL import ImageGrab
import cv2
import keyboard
from time import gmtime, strftime
import os

pytesseract_config = ("-l eng --psm 1 --oem 3")


def process_img(image):

    original_image = image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(
        gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    return gray


def main():
    try:
        img = ImageGrab.grabclipboard()
        cap = np.array(img)
        file_name = strftime(
            "%S_%M_%H__%Y_%m_%d", gmtime())
        file_path = os.path.join(os.getcwd(), 'files', file_name + '.py')
        processed_image = process_img(cap)

        output_string = pytesseract.image_to_string(processed_image, config=pytesseract_config,
                                                    lang='eng')
        file = open(file_path, 'a')
        file.write(output_string)
        file.close()
        os.system("code " + file_path)
        print('saved to file: ', file_name + '.py')
    except:
        print("Encountered an error")


if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+shift+alt+q', main)
    keyboard.wait()
