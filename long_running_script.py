#!/usr/bin/env python
import time
import argparse
import importlib

from hooks import *


def main():

    print("There are currently {} hooks registered".format(len(hookregistry.HookRegistry.hooks)))
    hookregistry.HookRegistry.execute_hooks()   


if __name__ == "__main__":
    main()
