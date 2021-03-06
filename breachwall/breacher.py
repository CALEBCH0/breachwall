import platform
import ctypes
import os
import sys
# import gconf
import wget
from PIL import Image
import schedule
import time
import shutil
import keyboard

import dejavu


def get_wall(wall_type):
    name = 'get_wall'
    try:
        # not so messed up version
        url = 'https://i.kym-cdn.com/photos/images/newsfeed/000/063/585/1209077053849_jpg__roflposters_com__myspace.jpg'
        # 'https://ih0.redbubble.net/image.702318777.9332/poster,840x830,f8f8f8-pad,1000x1000,f8f8f8.jpg'
        # blocked by school firewall
        # 'https://i.imgur.com/WpZuQvO.png'
        if wall_type == 'Windows':
            wall_path =  get_home_dir(wall_type)+'\\hen.jpg'
            if os.path.isfile(wall_path):
                os.remove(wall_path)
            wget.download(url, wall_path)
            stretch_wall(wall_path)
        elif wall_type == 'Linux':
            wall_path = get_home_dir(wall_type)+'/hen.jpg'
            if os.path.isfile(wall_path):
                os.remove(wall_path)
            wget.download(url, wall_path)
            # stretch_wall(wall_path)
        else:
            print("get_wall_input_error")    
        return wall_path
    except:
        get_error(name)


def stretch_wall(wall_path):
    image = Image.open(wall_path)
    width, height = image.size
    if width <= 800 and height <= 800:
        image = image.resize((800, 800), Image.ANTIALIAS)
        os.remove(wall_path)
        image = image.save(wall_path)


# TODO: outdated
def retract(retract_type):
    name = 'retract'
    try:
        wall_type = platform.system()
        if wall_type == 'Windows':
            if retract_type == 'rr':
                revert(retract_type)
                # windows_breacher('C://Users/kmcho/OneDrive/Pictures/backgrounds/python.png')
            elif retract_type == 'r':
                windows_breacher('https://s23527.pcdn.co/wp-content/uploads/2017/09/underexposing_the_scene-768x432.jpg.optimal.jpg')
        elif wall_type == 'Linux':
            print("unavailable")
        elif wall_type == 'Darwin':
            print("unavailable")
        else:
            print("input_error")
    except:
        get_error(name)


# CachedFiles works by deleting the folder every time there is a change but it sometimes doesn't work 
# https://superuser.com/questions/966650/path-to-current-desktop-backgrounds-in-windows-10
def revert(revert_type):
    name = 'revert'
    if revert_type == 'rv':
        wall_type = platform.system()
        if wall_type == 'Windows':
            # windows_breacher(os.environ['APPDATA']+'\\Microsoft\\Windows\\Themes\\CachedFiles')
            windows_breacher(os.environ['APPDATA']+'\\Microsoft\\Windows\\Themes\\TranscodedWallpaper.jpg')
            # saveOrigin(True)
            # dir = os.environ['APPDATA']+'\\Microsoft\\Windows\\Themes\\CachedFiles'
            # for  x in os.listdir(dir):
                # path = dir + "\\" + x
                # path = os.environ['APPDATA']+'\\Microsoft\\Windows\\Themes\\TranscodedWallpaper'
                # path = os.environ['APPDATA']+'\\Microsoft\\Windows\\Themes\\TranscodedWallpaper'
                # target = os.environ['APPDATA']+'\\Microsoft\\Windows\\Themes\\TranscodedWallpaper.jpg'
                # shutil.copyfile(path, target)
            # windows_breacher(path)
        elif wall_type == 'Linux':
            print("no")
        elif wall_type == 'Darwin':
            print("no")
        else:
            print("revert_input_error")
    elif revert_type == 'rr':
        windows_breacher('C://Users/kmcho/OneDrive/Pictures/backgrounds/python.png')
   

def breach_wall():
    print("in breach_wall: %s, %s" % (dejavu.is_dejavu, dejavu.is_breached)) 
    name = 'breach_wall'
    saveOrigin()
    startup = input("start \n")
    if startup == 'k':
        set_wallpaper()
        set_dejavu(False, True)
    elif startup == 'rv' or startup == 'rr':
        if not dejavu.is_dejavu:
            if dejavu.is_breached:        
                print("reverting...")
                revert(startup)
                print("reverted.")
                set_dejavu(True, False)
            if not dejavu.is_breached:
                set_dejavu(True, False)
    elif startup == 'n':
        print("abort")
    elif startup == 'at':
        periodic_breach()
    else:
        print("breach_wall_input_error")


# TODO: minimize the console during operation
# keyboard
# https://stackoverflow.com/questions/24072790/detect-key-press-in-python
def periodic_breach():
    set_wallpaper()
    # for test, do seconds
    schedule.every().seconds.do(set_wallpaper)
    while True:
        if keyboard.is_pressed('q'):
            print("periodic breach ended")
            break
        schedule.run_pending()
        time.sleep(4)
    

def gnome_breacher(wall_path):
    try:
        os.system('gsettings set org.gnome.desktop.background picture-uri file://' + wall_path)
    except:
        get_error("gnome_breacher")


def windows_breacher(wall_path):
    origin = 'windows_breacher'
    try:
        wall_path = os.path.normpath(wall_path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_path, 0)
    except:
        get_error(origin)


# on hold
#def saveOrigin(dejavu, breached):
#    lines = open('dejavu.py').read().splitlines()
#    if not breached and not dejavu:
#        origin = os.path.normpath('C://Users/kmcho/AppData/Roaming/Microsoft/Windows/Themes/TranscodedWallpaper')
#        target = os.path.normpath('C://Users/kmcho/AppData/Roaming/Microsoft/Windows/Themes/TranscodedWallpaper.jpg')
#        shutil.copyfile(origin, target) 
#        lines[0] = 'is_dejavu = True'
#        lines[1] = 'is_breached = True'
#        open('dejavu.py', 'w').write('\n'.join(lines))
#        #with open('dejavu.py', "w") as f:
#        #    f.write('is_dejavu = True\nis_breached = True')
#    if breached and not dejavu:
#        lines[0] = 'is_dejavu = False'
#        lines[1] = 'is_breached = False'
#        open('dejavu.py', 'w').write('\n'.join(lines))
#        #with open('dejavu.py', 'w') as f:
#        #    f.write('is_dejavu = False\nis_breached = False')
#    if dejavu:
#        lines[0] = 'is_dejavu = False'
#        open('dejavu.py', 'w').write('\n'.join(lines))
#        #with open('dejavu.py', 'w') as f:
#        #    f.write('is_dejavu = ')

def saveOrigin():
    if not dejavu.is_breached:
        origin = os.path.normpath('C://Users/kmcho/AppData/Roaming/Microsoft/Windows/Themes/TranscodedWallpaper')
        target = os.path.normpath('C://Users/kmcho/AppData/Roaming/Microsoft/Windows/Themes/TranscodedWallpaper.jpg')
        shutil.copyfile(origin, target)

        
def set_dejavu(rv_dejavu, breached):
    lines = open('dejavu.py').read().splitlines()
    lines[0] = 'is_dejavu = %s' % rv_dejavu
    lines[1] = 'is_breached = %s' % breached
    open('dejavu.py', 'w').write('\n'.join(lines))


def set_wallpaper():    
    name = 'set_wallapper'
    try:
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
            print("set_wallpaper_input_error")
    except:
        get_error(name)


def get_home_dir(wall_type):
    if wall_type == 'Windows':
        return os.environ['HOMEDRIVE']+'\\Users\\Public'
    elif wall_type == 'Linux':
        return os.environ['HOME']
    elif wall_type == 'Darwin':
        return 'Users/'
    else:
        return 'No match'


# name doesn't ring
# on hold because I'm not sure whether it cathes new errors or just prints the same
def get_error(name):
    e = sys.exc_info()[0]
    # discard if you need to display exit
    # if not e == SystemExit:
        # print(origin+"_error: %s" % e)
        # sys.exit()
    print(name+"_error: %s" % e)
    sys.exit()

