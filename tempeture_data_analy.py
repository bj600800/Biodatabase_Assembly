#!/usr/bin/env python           
# -*- coding:utf-8 -*-          
# @Filename:    tempeture_data_analy.py      
# @Author:      Eric Dou        
# @Time:        2021/5/28 22:19 

import os
import csv
from collections import Counter

temp = []
"""Function: """
path = r'F:\subject\active\GH temperature adaptation\sequence data\data\GH\GH10'
with open(os.path.join(path,'annotation_by_ncbi.csv'),'r') as csvfile:
    content = csv.reader(csvfile)
    for row in content:
        if row[8] != 'None':
            a = row[0]+'\t'+row[6]+'\t'+row[8]
            temp.append(a)
temp = temp[1:]

print(len(temp))

high = []
media = []
low = []
for i in temp:
    if int(i.split('\t')[2]) < 25:
        low.append(i)
    if 24 < int(i.split('\t')[2]) < 50:
        media.append(i)
    if int(i.split('\t')[2]) > 49:
        high.append(i)

print(len(low))
print(len(media))
print(len(high))

aa_low = []
aa_median = []
aa_high = []
with open(os.path.join(path,'acc_seq_temp.csv'),'w',newline='') as f:
    writecsv = csv.writer(f)
    writecsv.writerow(['Accession','Sequence','Temperature'])
    for i in low:
        i = i.strip('\n').split('\t')
        writecsv.writerow([i[0],i[1],i[2]])
        aa_low.append(i[1])
    writecsv.writerow('\n'*2)

    for i in media:
        i = i.strip('\n').split('\t')
        writecsv.writerow([i[0],i[1],i[2]])
        aa_median.append(i[1])
    writecsv.writerow('\n'*2)

    for i in high:
        i = i.strip('\n').split('\t')
        writecsv.writerow([i[0],i[1],i[2]])
        aa_high.append(i[1])
    writecsv.writerow('\n')

low = ''.join(aa_low)
media = ''.join(aa_median)
high = ''.join(aa_high)

print(Counter(low))
print(Counter(media))
print(Counter(high))