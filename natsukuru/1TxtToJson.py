import json
import os

fname1 = 'hm23'

fnamein=fname1 + '.txt'
fnameout=fname1 + '.json'

fp = open(fnamein,  "r",encoding='shift_jis')
filelines =fp.readlines()#读取出来是list
fp.close()


fp = open(fnameout,  "w",encoding='utf-8')
fp.write('[')
fp.close()

jsonorder = 0
msgtype = 0
dictfline={}
havetext = 0
multlinetxt = ''
for fline in filelines:
    msgtype = 1
    if (fline.startswith('*')):
        msgtype = 0
    if (fline.startswith('[')):
        msgtype = 0
    if (fline.startswith(';')):
        msgtype = 0
    if (fline.startswith('【')):
        msgtype = 2
        nameformat = fline[1:-2]
        dictfline['name'] = nameformat
    if (fline=='\n'):
        msgtype = 3
    
    if(msgtype == 1):
        multlinetxt = multlinetxt + fline
        havetext = 1
        
    if((msgtype == 3) and (havetext == 1)):
        dictfline['message'] = multlinetxt
        json1 = json.dumps(dictfline, ensure_ascii=False,sort_keys=True, indent=4, separators=(',', ': '))
        fp = open(fnameout,  "a",encoding='utf-8')
        fp.write(json1)
        fp.write(',')
        dictfline={}
        multlinetxt = ''
        nameformat = ''
        havetext = 0
        jsonorder = jsonorder+1
        #print(jsonorder)
fp = open(fnameout,  "rb+")
fp.seek(-1, os.SEEK_END)
fp.truncate()
fp.close()

fp = open(fnameout,  "a",encoding='utf-8')
fp.write(']')
fp.close()
