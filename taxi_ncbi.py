#!/usr/bin/env python           
# -*- coding:utf-8 -*-          
# @Filename:    taxi_ncbi.py      
# @Author:      Eric Dou        
# @Time:        2021/5/28 8:48 

"""Function: """
from ete3 import NCBITaxa                       # 导入此模块
import os
import csv

# ncbi = NCBITaxa()
# ncbi.update_taxonomy_database()                 # 升级模块
ncbi = NCBITaxa()
print(ncbi.get_lineage(421767))                        #用于获取输入Taxid代表的物种的完整分类信息，结果为一连串的Taxid号
print(ncbi.get_taxid_translator([611301]))             # 用于将Taxid转换为物种名或者对应的分类单位名，输入为列表形式
print(ncbi.get_descendant_taxa('Xanthomonas citri pv. citri'))               # 用于获取某分类单位所包含之后的各后代名
print(ncbi.get_name_translator(['Xanthomonas citri pv. citri']))   #用于将物种名或者分类单位名转换为Taxid，输入为列表形式

path = r'F:\subject\active\GH temperature adaptation\sequence data\data\GH\GH10'
acc_taxo = []
taxo = []

new_ann = []
with open(os.path.join(path,'annotation_by_ncbi.csv'),'r') as csvfile:
    content = csv.reader(csvfile)
    for row in content:
        a = row[0]+'\t'+row[3].strip('.')
        acc_taxo.append(a)
        taxo.append(row[3])

# with open(os.path.join(path,'new_ann.csv'),'w+',newline='') as f:
#     writecsv = csv.writer(f)
#     for i in new_ann:
#         writecsv.writerow([i[0],i[1],i[2],])
with open(os.path.join(path,'acc_taxo.txt'),'w') as f:
    for i in taxo[1:]:
        f.write(i+'\n')

with open(os.path.join(path,'taxo.txt'),'w') as f:
    for i in taxo[1:]:
        f.write(i+'\n')
taxid = []
with open(os.path.join(path,'taxid.txt'),'w') as f:
    for i in acc_taxo[1:]:
        a = i.split('\t')[1]
        for k,v in ncbi.get_name_translator([a]).items():
            f.write(i.split('\t')[0]+ '\t')
            f.write(str(v[0])+'\n')
