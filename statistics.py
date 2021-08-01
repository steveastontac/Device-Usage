# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 00:53:53 2021

@author: Steve Aston D Almeida
"""
import re
from datetime import date
import pandas as pd 
import sys
import csv


filename='C:\\Users\\ASUS\\Desktop\\Deviceusage\\csvs\\'
summaryname=filename+"summaries\\"
if(len(sys.argv)>1):
    
    filename+=sys.argv[1]
    summaryname+=sys.argv[1]
else:
    filename+=''.join(re.findall('[0-9]+', date.today().strftime("%d/%m/%Y")))+".csv"
    summaryname+=''.join(re.findall('[0-9]+', date.today().strftime("%d/%m/%Y")))+".csv"
#filename="16062021.csv"
apps={}
summary={}

def gettimes(t):
    s=t
    h=s//(60*60)
    r=s-(h*60*60)
    m=r//60
    r=r-(m*60)
    s=r
    return h,m,s

def gettimesdict(t):
    s=t
    h=s//(60*60)
    r=s-(h*60*60)
    m=r//60
    r=r-(m*60)
    s=r
    dictd={"h":h,"m":m,"s":s}
    return dictd

df=pd.read_csv(filename)
df=pd.DataFrame(df)

for index,row in df.iterrows() :
    di={}
    if row[3] in apps :
        di=apps[row[3]]
    else:
        di[row[0]]=row[1]
        apps[row[3]]=di
    if row[0] not in di:
             di[row[0]]=row[1]
        
tot=0

if(len(sys.argv)>2):
    key=sys.argv[2]
    val=apps[key]
    print ( " IN THE APP : : : : : : : :", key)
    tot=0
    for k,v in val.items():
        print( k," has been on screen for ",v)
        tot+=v
    print( " total time on ",key," formatted is : ",gettimes(tot),"\n\n\n\n")
else:    
    for key,val in apps.items():
        print ( " IN THE APP : : : : : : : :", key)
        tot=0
        for k,v in val.items():
            print( k," has been on screen for ",v)
            tot+=v
        print( " total time on ",key," formatted is : ",gettimes(tot),"\n\n\n\n")
        summary[str(key)]=gettimesdict(tot)

fields=['Name','H','M','S']
with open(summaryname,mode='w', newline='')as filo:
    fwriter=csv.DictWriter(filo, fieldnames=fields)
    fwriter.writeheader()
    for key,value in summary.items():
        fwriter.writerow({'Name': key, 'H': value['h'],'M':value['m'],'S':value['s'] })
