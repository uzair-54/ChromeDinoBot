import pyautogui
from PIL import Image, ImageGrab
import time

def hitKey(key):
    pyautogui.keyDown(key)

def collide(data):

    for x in range (450,480): 
        for y in range(300,338):
            if data[x,y] < 247: 
                return True
    return False


time.sleep(3)
hitKey("up")
while True:
    
    image = ImageGrab.grab().convert('L')
    data = image.load()

    if collide(data):
        hitKey("up")

def drawShape(data): # checking where to detect the collision
    for x in range (450,480):  #(a,b) a = left , b = right
        for y in range(300,338): #(a,b) a = top , b = bottom
            data[x,y] = 0             #247 BG color

#drawShape(data)
#image.show()