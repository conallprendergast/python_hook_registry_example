#!/usr/bin/env python
from hookregistry import HookRegistry

@HookRegistry.register_hook
def do_something(*args, **kwargs):
    if kwargs["day"] == 1:
    	print(">>> In hook that should be executed at the start of each month")





