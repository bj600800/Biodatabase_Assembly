#!/usr/bin/env python               #
# -*- coding:utf-8 -*-              #
# @Filename:    selectCBM.py        #
# @Author:      Eric Dou            #
# @Time:        2021/4/7 15:42      #
#####################################
'''Function: File redistribution and format rearrangement.'''

'''Use regular expression model to extract valid information from raw data.'''
import re

'''Creat lists to collect and store raw data for CBM and GH, named CBM, GH.
   Creat lists to catalog the orthologs enzyme sequences into different families, named CBMs, GHs.'''
CBM = []
GH = []
CBMs = []
GHs = []

'''Read raw data from CAZy sequences, and store them in CBM and GH lists.'''
with open(r'F:\subject\active\CBM-cellulose\bigdata\sequence_data\CAZyDB.07312020.fa','r+') as file:
    content = file.readlines()
    content = list(zip(*[iter(content)]*2))
    for i in content:
        patterncbm = re.compile(r'CBM')
        if patterncbm.findall(i[0]):
            CBM.append(i)
        patterngh = re.compile(r'GH')
        if patterngh.findall(i[0]):
            GH.append(i)
print('section 1 done')

'''Classify CBM sequences with different enzyme families.'''
# for j in range(1,88):
#     CBM_ = []
#     for a in CBM:
#         patterncbmnum = re.compile(r'CBM(%d)\|'%j)
#         target = a[0].split('|') # CBM exists mutiple times
#         if patterncbmnum.findall(target[1]+'|'): # only consider the 1st position of CBM index, AA enzyme is not in our consideration
#             CBM_.append(a)
#     CBMs.append(CBM_)

'''Classify GH sequences with different enzyme families.'''
for j in range(1,169):
    GH_ = []
    for a in GH:
        patternghnum = re.compile(r'GH(%d)\|' % j)
        if patternghnum.findall(a[0]):
            GH_.append(a)
    GHs.append(GH_)
print('section 2 done')

'''Write CBM sequences in CBM.fa file.'''
# with open('CBM.fa','w+') as out1:
#     for i in CBM:
#         out1.write(i[0])
#         out1.write(i[1])

'''Write GH sequences in GH.fa file.'''
# with open('GH.fa','w+') as out2:
#     for i in GH:
#         out2.write(i[0])
#         out2.write(i[1])

'''Write accession number of CBM in CBMacc.fa file.'''
# with open('CBMacc.fa','w+') as out1_1:
#     for i in CBM:
#         pattern = re.compile(r'^>(.+\d\|?)')
#         a = pattern.search(i[0]).group(1)
#         l = a.split('|')
#         out1_1.write(''.join(l[0])+'\n')

'''Write accession number of GH in GHacc.fa file.'''
# with open('GHacc.fa','w+') as out2_1:
#     for i in GH:
#         pattern = re.compile(r'^>(.+\d\|)')
#         a = pattern.search(i[0]).group(1)
#         l = a.split('|')
#         out2_1.write(''.join(l[0])+'\n')
# print('section 3 done')

'''Creat files for every CBM families to store enzyme sequences with accession number and family index.'''
# for i in range(1,88):
#     with open('F:\\subject\\active\CBM-cellulose\\bigdata\\sequence_data\\CBM\\CBM%d.fa' % i, 'w+') as out3:
#         for q in CBMs[i-1]:
#             out3.write(q[0])
#             out3.write(q[1])

'''Creat files for CBM-GH related information including a CBM domain connected with other CBM domain and GH domain.'''
CBM_GH = []
# for i in range(1,88):
#     with open('F:\\subject\\active\CBM-cellulose\\bigdata\\sequence_data\\CBM-GH\\CBM%d.fa' % i, 'w+') as out3:
#         GHcount = []
#         for q in CBMs[i-1]:
#             if list(q[0]).count('|') > 2 and re.search(r'GH',q[0]):
#                 out3.write(q[0])



'''Creat files for every GH families to store enzyme sequences with accession number and family index.'''
for i in range(1,169):
    # with open('F:\\subject\\active\CBM-cellulose\\bigdata\\sequence_data\\GH\\GH%d.fa' % i, 'w+') as out3:
    #     for q in GHs[i-1]:
    #         out3.write(q[0])
    #         out3.write(q[1])
    with open(r'F:\subject\active\GH temperature adaptation\sequence data\data\GHacc\GHacc\GHacc%d.fa' % i,'w+') as out4:
        for j in GHs[i-1]:
            pattern = re.compile(r'^>(.+\d\|?)')
            a = pattern.search(j[0]).group(1)
            l = a.split('|')
            out4.write(''.join(l[0]) + '\n')
print('section 4 done')

# '''Write the total number of CBM and GH sequences.'''
# with open('statistic.txt','w+') as sta:
#     a = 0
#     for i in CBMs:
#         a+=1
#         sta.write('CBM%d\t'%a)
#         sta.write(str(len(i))+'\n')
#     a = 0
#     for i in GHs:
#         a+=1
#         sta.write('GH%d\t'%a)
#         sta.write(str(len(i))+'\n')
#




