#!/usr/bin/env python
import time
import argparse
import importlib

from hooks import *
from hooks.hookregistry import HookRegistry



def main():

    print("Today is the first day of the month, lets see what hooks we should execute...")
    HookRegistry.execute_hooks(day=1)   

    time.sleep(1)
    print()
    print("The script has now been running for 3 days, so it is time to execute the hooks for the end of day 3...")

    HookRegistry.execute_hooks(day=3)   


if __name__ == "__main__":
    main()
