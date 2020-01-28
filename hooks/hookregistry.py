#!/usr/bin/env python

class HookRegistry:
    hooks = []
    
    def register_hook(f):
        HookRegistry.hooks.append(f)            
        def wrap(*args, **kwargs):
            f(*args, **kwargs)
        return wrap


    def execute_hooks(*args, **kwargs):
        for f in HookRegistry.hooks:
            f(*args, **kwargs)




