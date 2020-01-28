from .hookregistry import HookRegistry
import sys
import os
sys.path.append(os.path.dirname(__file__))

all_classes=[]

# Import all classes in this directory so that classes with @register_class are registered. 

from os.path import basename, dirname, join
from glob import glob
pwd = dirname(__file__)
for x in glob(join(pwd, '*.py')):
    if not x.startswith('__'):
        all_classes.append(basename(x)[:-3])


__all__ = all_classes

