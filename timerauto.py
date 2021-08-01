# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 16:34:28 2021

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
import os.path


def get_app_name():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return(psutil.Process(pid[-1]).name())
    except:
        pass

#hms counter
def gettimes(t):
    s=t
    h=s//(60*60)
    r=s-(h*60*60)
    m=r//60
    r=r-(m*60)
    s=r
    return h,m,s


tdate=date.today().strftime("%d/%m/%Y");

filename='C:\\Users\\ASUS\\Desktop\\Deviceusage\\csvs\\' + ''.join(re.findall('[0-9]+',tdate ))+".csv"
fields=['Name','Time','Date','Exename']


if(not os.path.isfile(filename)):
    file = open(filename, 'w+')
    csvhead= csv.writer(file)
    csvhead.writerow(fields)
    file.close()


apps={}
df=pd.read_csv(filename)
df=pd.DataFrame(df)

for index,row in df.iterrows() :
    li=[]
    li.append(row[1])
    li.append(row[2])
    li.append( row[3])
    apps[row[0]]=li



while(True):
    try:
        time.sleep(0.5)
    except KeyboardInterrupt:
        break;    
    
    appname=''.join(re.findall('[a-zA-Z]*[0-9]*[" "]*["."]*', GetWindowText(GetForegroundWindow())))
    
    #parental controls begin
    if(re.findall( 'porn|babes|sexy|booty|fucking|pussy',appname)):
        os.system("taskkill /im "+get_app_name())

    #parental controls end
    if appname=="" and get_app_name()=="explorer.exe":
        appname="Desktop Home"
    if not(appname in apps.keys()):
        list1=[0,"none","unknown"]
        apps[appname]=list1
    item=apps[appname]
    item[0]+=0.5;
    item[1]=date.today().strftime("%d/%m/%Y")
    item[2]=get_app_name()
    print(item[0],item[1],item[2],appname)
    
    with open(filename,mode='w', newline='')as filo:
        fwriter=csv.DictWriter(filo, fieldnames=fields)
        fwriter.writeheader()
        for key,value in apps.items():
            fwriter.writerow({'Name': key, 'Time': value[0], 'Date':value[1],'Exename':value[2] })
