# -*- coding: utf-8 -*-
"""
Created on Wed May 30 14:50:14 2018

@author: Hat_Pinlei
"""

from distutils.core import setup
import py2exe

includes = ["tkFileDialog","csv"]

setup(windows = [{"script":"PinleiFunc.py"}],
      options = {"py2exe": {"dll_excludes": ["MSVCP90.dll"], "includes": includes}})
