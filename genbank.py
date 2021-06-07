#!/usr/bin/env python           
# -*- coding:utf-8 -*-          
# @Filename:    genbank.py      
# @Author:      Eric Dou        
# @Time:        2021/5/5 12:45 

'''Function: obtain genbank database'''

from Bio import Entrez
import os
import time
from func_timeout import func_timeout, FunctionTimedOut
import datetime
PATH = r'F:\subject\active\GH temperature adaptation\sequence data\data\GH10_genbank'
Entrez.email = "bj600800@vip.qq.com"
from urllib.error import HTTPError
with open(os.path.join(PATH, 'genbank_missing.gb'), 'a+') as w:
    with open (os.path.join(PATH,'missing_gb.txt')) as f:
        uids = f.readlines()
        maxline = len(uids)
        count = 1
        attempt = 1
        def task(count, maxline):
            print("Going to download record %i to %i" % (count, maxline))
            handle = Entrez.efetch(db="protein", id=i, rettype="gb", retmode="text")
            w.writelines(handle.read())
            print(r"Mission completed", (count / maxline) * 100, "%")
        while attempt <= 3:
            try:
                for i in uids:
                    try:
                        doitReturnValue = func_timeout(10, task, args=(count, maxline))
                        count += 1
                        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(time)
                    except FunctionTimedOut:
                        with open(os.path.join(PATH, 'missing_item.txt'),'a+') as m:
                            m.write('number %i could not complete within 10 secs and continue\n' % count)
                        continue
            except HTTPError as err:
                if 500 <= err.code <= 599:
                    print("Received error from server %s" % err)
                    print("Attempt %i of 3" % attempt)
                    attempt += 1
                    time.sleep(15)
                else:
                    raise
