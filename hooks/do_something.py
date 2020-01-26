#!/usr/bin/env python

@HookRegistry.register_hook(day=1, start_end="START")
def do_something():
    print(">>> In hook that should be executed at the start of each month")

