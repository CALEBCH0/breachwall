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
    # parser = argparse.ArgumentParser(description="Breach, Bleach, and Bring walls")
    # parser.add_argument('operation', help="which operation?")
    # args = parser.parse_args()
    # # TODO: clean this up
    # if args.operation == 'ot':
    #     if args.r == 'r':
    #         system('cd breachwall && python breachwall. py ot -r')
    #     if args.r == 'rr':
    #         system('cd breachwall && python breachwall.py ot -rr')
    #     system('cd breachwall && python breachwall.py ot')
    # elif args.operation == 'at':
    #     system('cd breachwall && python breachwall.py at')
    system('cd breachwall && python breachwall.py')
elif env == 'Linux':
    print('unavailable')
