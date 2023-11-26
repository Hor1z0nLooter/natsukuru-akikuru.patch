import json
import os
import re

fname1  = 'rn21'
fnamein  ='j/'+ fname1 + '.txt'
fnameout ='c/'+ fname1 + '.txt'
jnamein  ='j/'+ fname1 + '.json'
jnameout ='c/'+ fname1 + '.json'


new_listj = []
with open(jnamein,'r',encoding = 'utf-8') as f:
    datatext = f.read()
    new_data_list = re.split('},',datatext)
    #分割的时候 把}去掉了，所以后面需要再把}加到新的json对象后面
    #这样一个json对象才完整 {}
    for i in new_data_list:
        ii = i+'}'
        new_listj.append(ii)

i=0
for list1 in new_listj:
    #print(list1)
    
    i=i+1
print('j',i)

new_listc = []
with open(jnameout,'r',encoding = 'utf-8') as f:
    datatext = f.read()
    new_data_list = re.split('},',datatext)
    #分割的时候 把}去掉了，所以后面需要再把}加到新的json对象后面
    #这样一个json对象才完整 {}
    for i in new_data_list:
        ii = i+'}'
        new_listc.append(ii)

i=0
for list1 in new_listc:
    #print(list1)
    
    i=i+1
print('c',i)

new_listc[0] = new_listc[0][1:]
new_listc[i-1] = new_listc[i-1][:-2]

############
json_listc = {}
i=0
for list1 in new_listc:
    json_listc[i] =(json.loads(new_listc[i]))
    i=i+1

#print(json_listc[i-1]['message'])
#print(json_listc[153]['name'])
############
fp = open(fnamein,  "r",encoding='shift_jis')
rawtxtlines =fp.readlines()#读取出来是list
fp.close()

jsonorder = 0
msgtype = 0
dictfline={}
havetext = 0
havename = 0
multlinetxt = ''
for fline in rawtxtlines:
    msgtype = 1
    if (fline.startswith('*')):
        msgtype = 0
        fp = open(fnameout,  "a",encoding='utf-16')           
        fp.write(fline)
        fp.close()
    if (fline.startswith('[')):
        msgtype = 0
        fp = open(fnameout,  "a",encoding='utf-16')           
        fp.write(fline)
        fp.close()
    if (fline.startswith(';')):
        msgtype = 0
        fp = open(fnameout,  "a",encoding='utf-16')           
        fp.write(fline)
        fp.close()
    if (fline.startswith('【')):
        msgtype = 2
        havename = 1
    if (fline=='\n'):
        msgtype = 3
        if(havetext == 0):
            fp = open(fnameout,  "a",encoding='utf-16')           
            fp.write('\n')
            fp.close()

        
    
    if(msgtype == 1):
        multlinetxt = multlinetxt + fline
        havetext = 1
        
    if((msgtype == 3) and (havetext == 1)):

        if(havename == 1):
            fp = open(fnameout,  "a",encoding='utf-16')
            fp.write('【')
            fp.write(json_listc[jsonorder]['name'])
            fp.write('】') 
            fp.write('\n')
            fp.close()
        
        fp = open(fnameout,  "a",encoding='utf-16')
        fp.write(json_listc[jsonorder]['message'])
        fp.write('\n\n')
        fp.close()
        dictfline={}
        multlinetxt = ''
        havename = 0
        havetext = 0
        jsonorder = jsonorder+1
        #print(jsonorder)
