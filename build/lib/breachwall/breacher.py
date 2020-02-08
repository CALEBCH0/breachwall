import platform
import ctypes
import os
import sys
# import gconf
import wget
from PIL import Image
import schedule
import time


def get_wall(wall_type):
    url = 'https://ih0.redbubble.net/image.702318777.9332/poster,840x830,f8f8f8-pad,1000x1000,f8f8f8.jpg'
    # 'https://i.imgur.com/WpZuQvO.png'
    if wall_type == 'Windows':
        wall_path = 'C://Users/Public/hen.jpg'
        if os.path.isfile(wall_path):
            os.remove(wall_path)
        wget.download(url, wall_path)
        stretch_wall(wall_path)
    elif wall_type == 'Linux':
        wall_path = 'hoem/caleb/test_downloads/hen.jpg'
        if os.path.isfile(wall_path):
            os.remove(wall_path)
        wget.download(url, wall_path)
        # stretch_wall(wall_path)
    else:
        print("get_wall_error")
    return wall_path


def stretch_wall(wall_path):
    image = Image.open(wall_path)
    width, height = image.size
    if width <= 800 and height <= 800:
        image = image.resize((800, 800), Image.ANTIALIAS)
        os.remove(wall_path)
        image = image.save(wall_path)


def retract(retract_type, wall_type):
    if wall_type == 'Windows':
        if retract_type == 'rr':
            windows_breacher('C://Users/kmcho/OneDrive/Pictures/dokkaebi_drawing.png')
        elif retract_type == 'r':
            windows_breacher('https://s23527.pcdn.co/wp-content/uploads/2017/09/underexposing_the_scene-768x432.jpg.optimal.jpg')
    elif wall_type == 'Linux':
        print("unavailable")
    elif wall_type == 'Darwin':
        print("unavailable")
    else:
        print("retract_error")


def breach_wall():
    startup = input("start \n")
    if startup == 'k':
        set_wallpaper()
    elif startup == 'r' or startup == 'rr':
        wall_type = platform.system()
        print("retracting...")
        retract(startup, wall_type)
        print("retracted.")
    else:
        print("breach_wall_error")


def gnome_breacher(wall_path):
    system('gsettings set org.gnome.desktop.background picture-uri file:///home/caleb/test_downloads/hen.jpg')


def windows_breacher(wall_path):
    wall_path = os.path.normpath(wall_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_path, 0)


def set_wallpaper():
    wall_type = platform.system()
    print("getting wall...")
    wall_path = get_wall(wall_type)
    print("\n got it.")
    print("breaching wall...")
    if wall_type == 'Windows':
        windows_breacher(wall_path)
        print("wall breached.")
    elif wall_type == 'Linux':
        gnome_breacher(wall_path)
        print("wall breached.")
    elif wall_type == 'Darwin':
        print("unavailale")
    else:
        print("set_wallpaper_error")
