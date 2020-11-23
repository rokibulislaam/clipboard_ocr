import numpy as np
import pytesseract
from pytesseract import Output
import pandas as pd
from PIL import ImageGrab
from PIL import Image
import cv2
import keyboard
from time import gmtime, strftime
import os
import pytesseract


custom_config = r'-c preserve_interword_spaces=1 --oem 1 --psm 1 -l eng'


def process_img(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def main():
    try:
        print("\n\nprocessing...\n\n")
        img = ImageGrab.grabclipboard()
        cap = np.array(img)
        file_name = strftime(
            "%S_%M_%H__%Y_%m_%d", gmtime())
        file_path = os.path.join(os.getcwd(), 'files', file_name + '.py')
        processed_image = process_img(cap)

        # Thanks to the author of the answer:
        # https://stackoverflow.com/questions/59582008/preserving-indentation-with-tesseract-ocr-4-x
        d = pytesseract.image_to_data(
            processed_image, config=custom_config, output_type=Output.DICT)
        df = pd.DataFrame(d)

        # clean up blanks
        df1 = df[(df.conf != '-1') & (df.text != ' ') & (df.text != '')]
        # sort blocks vertically
        sorted_blocks = df1.groupby(
            'block_num').first().sort_values('top').index.tolist()
        for block in sorted_blocks:
            curr = df1[df1['block_num'] == block]
            sel = curr[curr.text.str.len() > 3]
            char_w = (sel.width/sel.text.str.len()).mean()
            prev_par, prev_line, prev_left = 0, 0, 0
            text = ''
            for ix, ln in curr.iterrows():
                # add new line when necessary
                if prev_par != ln['par_num']:
                    text += '\n'
                    prev_par = ln['par_num']
                    prev_line = ln['line_num']
                    prev_left = 0
                elif prev_line != ln['line_num']:
                    text += '\n'
                    prev_line = ln['line_num']
                    prev_left = 0

                added = 0  # num of spaces that should be added
                if ln['left']/char_w > prev_left + 1:
                    added = int((ln['left'])/char_w) - prev_left
                    text += ' ' * added
                text += ln['text'] + ' '
                prev_left += len(ln['text']) + added + 1
            text += '\n'
            file = open(file_path, 'a')
            file.write(text)
            file.close()
            os.system("code " + file_path)
            print('saved to file: ', file_name + '.py' + "\n\n")

    except:
        print("Encountered an error\n\n")


if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+shift+alt+q', main)
    keyboard.wait()
