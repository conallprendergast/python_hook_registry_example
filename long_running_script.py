#!/usr/bin/env python
import time
import argparse
import importlib

from hooks.hookregistry import HookRegistry


def main():

    print("Today is the first day of the month, lets see what hooks we should execute...")
    HookRegistry.execute_hooks(1, "START")   

    time.sleep(1)
    print()
    print("The script has now been running for 3 days, so it is time to execute the hooks for the end of day 3...")

    HookRegistry.execute_hooks(3, "END")   


if __name__ == "__main__":
    parser = argparse.ArgumentParser()    

    parser.add_argument("--hooks", type=argparse.FileType('r'), nargs='+', help="file which contains hooks")
    args = parser.parse_args()


    if args.hooks:
        for f in args.hooks:
            print("Loading hooks from file {}...".format(f.name))
            exec(f.read())
    else:
        print("You have not loaded any hooks")
   
    print()
    main()
