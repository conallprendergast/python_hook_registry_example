#!/usr/bin/env python

@HookRegistry.register_hook(day=3, start_end="END")
def do_something_else():
    print(">>> In hook that should be executed at the end of each 3rd day of every month")
