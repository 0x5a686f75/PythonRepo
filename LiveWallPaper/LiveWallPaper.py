#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image
import win32gui
import win32con
import win32api
import re
import sys
import os

# Author  : ZMYCHOU
# Version :V1.0
# Since   :2017/09/02
# Modified:2017/09/02
# To run this program, you need follow module:
# Python 3.6
# win32 module,website :https://sourceforge.net/projects/pywin32/
# Image module,website :https://pypi.python.org/pypi/Pillow
# BeautifulSoup,website:https://www.crummy.com/software/BeautifulSoup/  
# Navigate to the directory where this source file is located from DOS command and then enter
# follow command:
# python LiveWallPaper.py 

def setWallpaper(imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") 
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)
	
def setWallPaperBMP(imagePath):
    bmpImage = Image.open(imagePath)
    newPath = imagePath.replace('.jpg', '.bmp')
    bmpImage.save(newPath, "BMP")
    setWallpaper(newPath)
	
# Get image from Bing
bing = urlopen("http://cn.bing.com/").read()
str = bing.decode("gbk",'ignore')
imgUrl = re.search(r'az/hprichbg/rb(.){1,100}.jpg?', str)
if imgUrl:
	print(imgUrl.group())
imgFile = open(os.getcwd() + r"\img.bmp", "wb+")
img = urlopen("http://cn.bing.com/" + imgUrl.group()).read()
imgFile.write(img)
imgFile.flush()
imgFile.close()
setWallPaperBMP(os.getcwd() + r"\img.bmp")
