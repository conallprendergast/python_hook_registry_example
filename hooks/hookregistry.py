#!/usr/bin/env python

config = {}

class HookRegistry(object):
    hooks = []
    
    def register_hook(f):
        HookRegistry.hooks.append(f)
        print("Registrering hook. There are now {} hooks registered.".format(len(HookRegistry.hooks)))
        def wrap(*args, **kwargs):
            f(*args, **kwargs)
        return wrap

    def execute_hooks(*args, **kwargs):
        for f in HookRegistry.hooks:
            f(*args, **kwargs)




