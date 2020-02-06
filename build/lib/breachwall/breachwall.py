#! breachwall/Scripts/python
import breacher
import argparse

# TODO: add argparse in future for helps?
def main():
    parser = argparse.ArgumentParser(description='Breach, bleach, and bring walls')
    parser.add_arguemt('operation', help='what do you want to do?')
    args = parser.parse_args()
    if args.operation == 'ot': 
        breacher.breach_wall()
    elif args.operation == 'at':
        breacher.periodic_breach_wall()
    else:
        print("main_error")


if __name__ == '__main__':
    main()
