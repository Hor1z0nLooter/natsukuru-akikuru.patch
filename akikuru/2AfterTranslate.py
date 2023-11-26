import json
import os
import re

if (1):
    fhl = open('LIST.TXT','r')
    list1 = fhl.read().splitlines()
########################
for m in list1:
    print(m)
    jsonname='jsonin/'+m
    jsonout='jsonout/'+m
    jsoncn = 'jsoncn/'+m
################
    rawjson = []
    with open(jsonname,'r',encoding = 'utf-8') as f:
        datatext = f.read()
        rawjson = json.loads(datatext)

#################

#################
    new_listc = []
    with open(jsoncn,'r',encoding = 'utf-8') as f:
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
    print('j',i)

    new_listc[0] = new_listc[0][1:]
    new_listc[i-1] = new_listc[i-1][:-2]

############
    json_listc = {}
    i=0
    for list1 in new_listc:
        json_listc[i] =(json.loads(new_listc[i]))
        i=i+1

####################################
#print (json_listc[1]['message'])
#print (json_listc[1]['name'])
#json_listc[i]储存了翻译后的文本和名字

    texti=0
    for sceneslist in rawjson['scenes']:
        if 'texts' in sceneslist:
            for textobjall in sceneslist['texts']:
                if(type(textobjall[0])==str):
                    textobjall[0]=json_listc[texti]['name']

                if(1):
                    textobjall[2]=json_listc[texti]['message']
                    texti=texti+1

    #print (rawjson['scenes'][0]['texts'][0][2])

    with open (jsonout,'w',encoding = 'utf-8') as f:
        finaljsonstr=json.dumps(rawjson,ensure_ascii=False)
        f.write(finaljsonstr)
