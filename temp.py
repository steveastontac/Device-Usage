# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:28:55 2021

@author: Steve Aston D Almeida
"""

from win32gui import GetWindowText, GetForegroundWindow 
import win32process
import time
import pandas as pd
import csv
from datetime import date
import  psutil,win32gui
import re
import signal
import os.path
import wmi


def get_app_name():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return(psutil.Process(pid[-1]).name(),pid)
    except:
        pass

def processender(appname):
    ti = 0
     
    # This variable stores the name
    # of the process we are terminating
    # The extension should also be
    # included in the name
    name = appname
     
    # Initializing the wmi object
    f = wmi.WMI()
      
    # Iterating through all the
    # running processes
    for process in f.Win32_Process():
         
        # Checking whether the process
        # name matches our specified name
        if process.name == name:
     
            # If the name matches,
            # terminate the process   
            process.Terminate()
         
            # This increment would acknowledge
            # about the termination of the
            # Processes, and would serve as
            # a counter of the number of processes
            # terminated under the same name
            ti += 1
     
     
    # True only if the value of
    # ti didn't get incremented
    # Therefore implying the
    # process under the given
    # name is not found
    if ti == 0:
     
        # An output to inform the
        # user about the error
        print("Process not found!!!")
        
os.system("taskkill /im chrome.exe")



