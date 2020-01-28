#!/usr/bin/env python
from hookregistry import HookRegistry

@HookRegistry.register_hook
def do_something_else(*args, **kwargs):
    if kwargs["day"] == 3:
        print(">>> In hook that should be executed at the end of each 3rd day of every month")
