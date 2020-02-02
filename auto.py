from os import system
import platform
import subprocess
import sys

env = platform.system()
if env == 'Windows':
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    if not 'wget' and 'image' in installed_packages:
        system('pip install wget Image')
    system('cd breachwall && python breachwall.py')
elif env == 'Linux':
    print('unavailable')

