# clipboard_ocr
Convert a screenshot to text directly from clipboard (tested on Windows)

## How it works
The program continuously listens to `keyboard` hotkey event, when pressed it copies the image from clipboard and processes using `OpenCV` and applies `tesseract` OCR and copies the text result to clipboard again. The default hotkey is `ctrl` + `shift` + `g`.

## Dependencies
- `pillow`
- `keyboard`
- `pytesseract`
- `opencv-python`
- `numpy`
- `pandas`
- `pyperclip`

## Getting Started
0. Download & install Tesseract-OCR binary or compile it: https://tesseract-ocr.github.io/tessdoc/Downloads.html


1. Clone the repository
```shell
git clone https://github.com/rokibulislaam/clipboard_ocr.git
```
2. `cd` into `clipboard-ocr`
```shell
cd clipboard-ocr
```
3. Install `pipenv` (if you do not have it installed)
```shell
pip install pipenv
```
4. Install the dependencies
```shell
pipenv install
```
5. Start `pipenv` shell
```shell
pipenv shell
```
5. Run the program in python
```shell
python main.py
```
## Demo
![A working demo](demo/Demo%20GIF.gif "A working demo")
