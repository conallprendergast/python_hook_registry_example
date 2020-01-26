#!/usr/bin/env python

class HookRegistry:
    hooks = []
    
    def register_hook(day, start_end):
        def wrap(f):
            HookRegistry.hooks.append({"function": f, "day": day, "start_end": start_end})            
        return wrap


    def execute_hooks(day, start_end):
        hooks_to_execute = [h["function"] for h in HookRegistry.hooks if h["day"] == day and h["start_end"] == start_end]
        
        if len(hooks_to_execute) == 0:
            print("There are no hooks to execute")
        else:
            for f in hooks_to_execute:
                f()




