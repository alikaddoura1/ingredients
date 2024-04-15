import cv2
import pytesseract
import PIL.Image

"""
Page segmentation modes:
0 Orientation and script detection (OSD) only
1 Automatic page segmentation with OSD.
2 Automatic page segmentation, but no OSD, or OCR.
3 Fully automatic page segmentation, but no OSD. (Default)
4 Assume a single column of text of variable sizes
5 Assume a single uniform block of vertically aligned text.
6 Assume a single uniform block of text.
7 Treat the image as a single text line.
8 Treat the image as a single word.
9 Treat the image as a single word in a circle.
10 Treat the image as a single character.
11 Sparse text. Find as much text as possbile in no particulate order.
12 Sparse text with OSD.
12 Raw line. Treat the image as a single text line,
"""

"""
OCR Enginer Mode
0 Legacy engine only
1 Neural nets LSTM engine only
2 Legacy + LSTM engines
3 Default, based on what is available
"""


'''
PLAN OF ACTION: 

- OPEN IMAGE
- FIX Image and make it look nicer with SRGAN
- THEN process Image
'''

my_config = r"--psm 6 --oem 3"
box_config =r"--psm 12 --oem 3"


box_text = pytesseract.image_to_string(PIL.Image.open("box.png"), config =box_config)
cookiess_text = pytesseract.image_to_string(PIL.Image.open("cookiess.png"), config = box_config)



print(box_text)

