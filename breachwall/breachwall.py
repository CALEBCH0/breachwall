#! breachwall/Scripts/python
import breacher
import argparse


# TODO: decide where are you gonna pass args
def main():
    # parser = argparse.ArgumentParser(description='Breach, bleach, and bring walls')
    # parser.add_arguemt('operation', help='what do you want to do?')
    # args = parser.parse_args()
    # if args.operation == 'ot':
    #     breacher.breach_wall()
    # elif args.operation == 'at':
    #     breacher.periodic_breach()
    # else:
    #     print("main_error")
    breacher.breach_wall()
    # breacher.periodic_breach()


if __name__ == '__main__':
    main()

