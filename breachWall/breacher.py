# This breaches walls!
# execute (.exe)
# check env
#   windows
#   ubuntu
#   mac
# get image
#   download
# set image
#   accordingly to env

import ctypes
import os
import struct
import subprocess
import sys
# import commands
import gconf

# import win32con

# from appscript import app, mactypes

import wget
from os import walk, getenv, system
from shutil import copyfile
from PIL import Image


### desktop environment begin ###


def get_desktop_environment(self):
    if sys.platform in ["win32", "cygwin"]:
        return "windows"
    elif sys.platform == "darwin":
        return "mac"
    else:  # Most likely either a POSIX system or something not much common
        desktop_session = os.environ.get("DESKTOP_SESSION")
        if desktop_session is not None:  # easier to match if we doesn't have  to deal with caracter cases
            desktop_session = desktop_session.lower()
            if desktop_session in ["gnome", "unity", "cinnamon"]:
                return desktop_session
            elif desktop_session.startswith("ubuntu"):
                return "unity"
        if os.environ.get('GNOME_DESKTOP_SESSION_ID'):
            if not "deprecated" in os.environ.get('GNOME_DESKTOP_SESSION_ID'):
                return "gnome2"
    return "unknown"
### desktop environment end ###


def get_wall():
    print("getting wall...")
    url = 'https://cdn.arstechnica.net/wp-content/uploads/2016/02/5718897981_10faa45ac3_b-640x624.jpg'
    wget.download(url, '/home/caleb/test_downloads/eye.jpg')
    wall_path = '/home/caleb/test_downloads/eye.jpg'
    return wall_path


def breach_wall():
    print("getting wall...")
    wall_path = get_wall()
    print("got it!")
    print("breaching wall...")
    print(gnome_breacher())
    # set_wallpaper(wall_path)
    print("wall breached!")


### gnome breacher begin ###
def gnome_breacher():
    system("gsettings set org.gnome.desktop.background picture-uri file:///home/caleb/test_downloads/eye.jpg")
#### gnome breacher end ###


### windows braecher begin ###
def windows_breacher():
    return True
### windows breacher end ###


### adaptive breacher begin ####
def set_wallpaper(self, file_loc, first_run):
    # Note: There are two common Linux desktop environments where
    # I have not been able to set the desktop background from
    # command line: KDE, Enlightenment
    desktop_env = self.get_desktop_environment()
    try:
        if desktop_env in ["gnome", "unity", "cinnamon"]:
            uri = "'file://%s'" % file_loc
            try:
                SCHEMA = "org.gnome.desktop.background"
                KEY = "picture-uri"
                gsettings = Gio.Settings.new(SCHEMA)
                gsettings.set_string(KEY, uri)
            except:
                args = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri]
                subprocess.Popen(args)
        elif desktop_env == "gnome2":  # Not tested
            args = ["gconftool-2", "-t", "string", "--set", "/desktop/gnome/background/picture_filename",
                    '"%s"' % file_loc]
            subprocess.Popen(args)
        elif desktop_env == "windows":
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_loc, 0)
        # elif desktop_env=="mac":
        #    try:
        #        app('Finder').desktop_picture.set(mactypes.File(file_loc))
        #     except ImportError:
        #        #import subprocess
        #        SCRIPT = """/usr/bin/osascript<<END
        #        tell application "Finder" to
        #         set desktop picture to POSIX file "%s"
        #        end tell
        #        END"""
        #        subprocess.Popen(SCRIPT%file_loc, shell=True)
        # else:
        #     if first_run:  # don't spam the user with the same message over and over again
        #         sys.stderr.write("Warning: Failed to set wallpaper. Your desktop environment is not supported.")
        #         # sys.stderr.write("You can try manually to set Your wallpaper to %s" % file_loc)
        #     return False
        # return True
    except:
        sys.stderr.write("ERROR: Failed to set wallpaper. There might be a bug.\n")
        return False


# def get_config_dir(self, app_name=APP_NAME):
#     if "XDG_CONFIG_HOME" in os.environ:
#         confighome = os.environ['XDG_CONFIG_HOME']
#     elif "APPDATA" in os.environ:  # On Windows
#         confighome = os.environ['APPDATA']
#     else:
#         try:
#             from xdg import BaseDirectory
#             confighome = BaseDirectory.xdg_config_home
#         except ImportError:  # Most likely a Linux/Unix system anyway
#             confighome = os.path.join(self.get_home_dir(), ".config")
#     configdir = os.path.join(confighome, app_name)
#     return configdir


def get_home_dir(self):
    if sys.platform == "cygwin":
        home_dir = os.getenv('HOME')
    else:
        home_dir = os.getenv('USERPROFILE') or os.getenv('HOME')
    if home_dir is not None:
        return os.path.normpath(home_dir)
    else:
        raise KeyError("Neither USERPROFILE or HOME environment variables set.")
### adaptive breacher end ####
