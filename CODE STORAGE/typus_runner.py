# from keyboard import write
# from time import sleep
#
#
# s = ''''''
#
#
# sleep(2)
# for ch in s:
#     write(ch)
#     sleep(0.0305)
#
#



import pyautogui
import time
import cv2
import pytesseract
import keyboard

time.sleep(1)
pyautogui.screenshot('img/' + '1' + '.png', region=(800, 690, 1300, 530))


img = cv2.imread('img/1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
string = pytesseract.image_to_string(img,)

keyboard.write('q')
time.sleep(4)
string = ' '.join(string.split())
if string[0] == '|' or 'l':
    string = string[1:]
for i in string:
    keyboard.write(i)
    time.sleep(0.06)
print(string)

