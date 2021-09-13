import cv2
import pytesseract as pt

def to_string_ocr(img):
    text = pt.image_to_string(img)
    return text


# turn to greyscale, threshold and delete noise to make an image easier to read
def modify(img):
    return cv2.medianBlur(cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY + cv2. THRESH_OTSU)[1], 5)

im_input = input ("Enter name of image:")
image = cv2.imread('{}.png'.format(im_input))
image = modify(image)
print(image)
words=to_string_ocr(image)
print(words)
