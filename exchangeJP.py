import csv
import os
import sys
import telegram
from pymongo import MongoClient
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

os.system('wget --user-agent="Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko" http://rate.bot.com.tw/xrt/flcsv/0/day -O 55688.csv')

print ('hello word 01')

gginin = []

sn1 = '台灣銀行匯率'
yahoo = time.strftime("%Y_%m_%d_%H:%M")
cc = '55688.csv'

with open(cc, 'r',encoding='UTF-8', newline='') as csvfile:
    #gginin = csv.reader(csvfile, delimiter=',') 

    gginin = csvfile.readlines()
    lline= []
    aa=[]
    bb=[]
    cc=[]
    dd=[]
    ee=[]

    print ('hello word 02')

    for line in gginin:
        line = line.split(',')
        aa.append(line[0])
        bb.append(line[1])
        cc.append(line[2])
        dd.append(line[11])
        ee.append(line[12])

    print ('hello')
    aa.remove('\ufeff幣別')
    bb.remove('匯率')
    cc.remove('現金')
    dd.remove('匯率')
    ee.remove('現金') 

    client = MongoClient('192.168.8.28', 27017)
    db = client.nono
    exchange_rate = db.exchange_rate
    print('rrrrrrororo')

    for x in range(0,19):
        post = {"author": "台灣銀行",
        "幣別": aa[x],
        "銀行現金買入":cc[x],
        "銀行現金賣出":ee[x],
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
        exchange_rate.insert_one(post)

print ("發TG囉")
exe= "日圓"+"現金匯率"+'※'+"本行買入"+'['+cc[7]+']'+"本行賣出"+'['+ee[7]+']'+'※'
bot = telegram.Bot(token='448602699:AAFznWoWzSrG5u297xnh7P1SBGwb-guN4gc')
bot.sendMessage(chat_id='-1001084633429', text="#"+yahoo+'\n'+sn1+'\n'+exe)

print ("準備刪除55688.csv")
os.system('rm 55688.csv')
print ('end')

