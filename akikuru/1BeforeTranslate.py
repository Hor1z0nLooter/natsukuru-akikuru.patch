import json
import os


if (1):
    fhl = open('LIST.TXT','r')
    list1 = fhl.read().splitlines()

for m in list1:
    print(m)
    jsonname='jsonin/'+m
    jsonout='jsonout/'+m


    rawjson = []
    with open(jsonname,'r',encoding = 'utf-8') as f:
        datatext = f.read()
        rawjson = json.loads(datatext)

    fp = open(jsonout,'w',encoding='utf-8')
    fp.write('[')
    fp.close()


    #print(rawjson['scenes'][0]['texts'][0][0])
    outjson = {}
    textobjnum=0
    for sceneslist in rawjson['scenes']:
        if 'texts' in sceneslist:
            for textobjall in sceneslist['texts']:
                if(type(textobjall[0])==str):
                    outjson['name'] = textobjall[0]

                if(1):
                    outjson['message'] = textobjall[2]

                json1 = json.dumps(outjson, ensure_ascii=False,sort_keys=True, indent=4, separators=(',', ': '))
                fp = open(jsonout,  "a",encoding='utf-8')
                fp.write(json1)
                fp.write(',')
                dictfline={}
                fp.close()


    fp = open(jsonout,  "rb+")
    fp.seek(-1, os.SEEK_END)
    fp.truncate()
    fp.close()

    fp = open(jsonout,  "a",encoding='utf-8')
    fp.write(']')
    fp.close()
