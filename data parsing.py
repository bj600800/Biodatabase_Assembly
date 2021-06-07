#!/usr/bin/env python           
# -*- coding:utf-8 -*-          
# @Filename:    data parsing.py      
# @Author:      Eric Dou        
# @Time:        2021/5/17 9:40 

"""Function: cleaning and formatting raw data."""
import os
import re
from collections import defaultdict
import csv
from collections import Counter
path = r'F:\subject\active\GH temperature adaptation\sequence data\data\GH10_genbank'

def get_lines(file_path):
    with open (file_path,'r') as f:
        temp = [line for line in f]
        return temp
def get_fasta(path_seq):
    with open (path_seq,'r') as fasta:
        content = fasta.readlines()
        content = list(zip(*[iter(content)] * 2))
        return content


# get genbank flatfile content
flatfile = ''.join(get_lines(os.path.join(path,'genbank_gh10.gb')))
flatfile = re.split(r'//\n',flatfile) #LOCUS       ARQ79354                 333 aa            linear   BCT 16-MAY-2017
dict_flatfile = defaultdict() # ['BCT', 'xylanase [Cellvibrio sp. KY-GH-1].', 'Cellvibrio sp. KY-GH-1',
# ['154..208,/region_name="Big_7",/note="Bacterial Ig domain; pfam17957",/db_xref="CDD:380075",', '261..528,/region_name="Glyco_10",/note="Glycosyl hydrolase family 10; smart00633",/db_xref="CDD:214750",', '535..651,/region_name="CBM6_xylanase-like",/note="Carbohydrate Binding Module 6 (CBM6); many are,appended to glycoside hydrolase (GH) family 11 and GH43,xylanase domains; cd04084",/db_xref="CDD:271150",', '663..792,/region_name="CBM_4_9",/note="Carbohydrate binding domain; pfam02018",/db_xref="CDD:376716",', '811..943,/region_name="CBM_4_9",/note="Carbohydrate binding domain; pfam02018",/db_xref="CDD:376716",']]

# acc = get_fasta(os.path.join(path_seq,'GH10.fa'))[0]
# sequence = get_fasta(os.path.join(path_seq,'GH10.fa'))[1]


for i in flatfile:
    fetures = [] #
    oneline_feture = i.split('\n')
    for p in oneline_feture:
        if re.match('DEFINITION',p): # enzymes name
            fetures.append(p.split('  ')[-1])
        if re.match('LOCUS',p): # domain
            fetures.append(re.split(r' +',p)[-2])
        if re.match('SOURCE',p):
            fetures.append(p.split('      ')[-1])
        if re.match('VERSION',p):
            dict_flatfile[p.split('     ')[-1]] = fetures
    # toxonomy
    r1 = re.compile(' ORGANISM(.+)REFERENCE {3}1', re.S | re.M)
    b = r1.findall(i)
    b = ''.join(b).replace('\n', ',')
    b = re.sub(' {2,}', '', b)
    b = b.split(',')[1:]
    b = ','.join(b).replace(',', '').split(';')
    fetures.append(b)

    # region
    r = re.compile("( {5}Region {10}.?\d+\.\..?\d+.+\"\n {21}.+\"\n) +CDS.+\d", re.S | re.M)
    a = r.findall(i)
    a = ''.join(a).replace('\n',',')
    a = re.sub(' {2,}','',a)
    a = a.split('Region')[1:] # ['1..>51,/region_name="Glyco_hydro_1",/note="Glycosyl hydrolase family 1; cl23725",/db_xref="CDD:304882",']
    fetures_temp = [w.split(',')[:-1] for w in a] #['144..499', '/region_name="Glyco_hydro_1"', '/note="Glycosyl hydrolase family 1; cl23725"', '/db_xref="CDD:304882"']
    if len(fetures_temp) > 1:
        fetures.append(fetures_temp)
    if len(fetures_temp) == 1:
        fetures.append(a[0].split(',')[:-1])
    if len(fetures_temp) == 0:
        fetures.append('GH10')

#sequence
path_seq = r'F:\subject\active\GH temperature adaptation\sequence data\data\GH'
fasta = get_fasta(os.path.join(path_seq,'GH10.fa'))
for item in fasta:
    for key, value in dict_flatfile.items():
        if key == item[0].split('|')[0][1:]:
            dict_flatfile[key].append(item[1][:-1])

# taxomony id
path_spe = r'F:\subject\active\GH temperature adaptation\sequence data\data\GH\GH10'
with open(os.path.join(path_spe,'species.txt'),'r') as f:
    content = set(f.readlines()) # 不去重就会反复追加taxid
    for i in content:
        for key,value in dict_flatfile.items():
            if key == i.split('\t')[0]:
                dict_flatfile[key].append(i.split('\t')[1].strip('\n'))
for k,v in dict_flatfile.items():
    if len(v) ==  6:
        dict_flatfile[k].append('None')

# temperature lable
path_tem = r'F:\subject\active\GH temperature adaptation\sequence data\data'
with open(os.path.join(path_tem,'temperature_data.csv'),'r') as f:
    content = csv.reader(f)
    for i in content:
        for key,value in dict_flatfile.items():
            if value[6] == i[3]:
                dict_flatfile[key].append(i[2]) #温度对应的taxid有多个，所以，用最后一个value值就行，
print(dict_flatfile['ACR83565.1'])
for k,v in dict_flatfile.items():
    if len(v) ==  7:
        dict_flatfile[k].append('None')


# output test

print(dict_flatfile['VEI00167.1']) #['BCT', 'xylanase GH10 [Paenibacillus amylolyticus].', 'Paenibacillus amylolyticus', ['Bacteria', ' Firmicutes', ' Bacilli', ' Bacillales', ' Paenibacillaceae', 'Paenibacillus.'], [['47..328', '/region_name="Glyco_10"', '/note="Glycosyl hydrolase family 10; smart00633"', '/db_xref="CDD:214750"']], 'MPTEIPSLHATYANTFKIGAAVHTRMLQSEADFIAKHFNSITAENQMKFEEIHPEEDRYSFEAADKIVDFAVAQGIGVRGHTLVWHNQTSKWVFEDTSGAPASRELLLSRLKQHIDTVVGRYKGQIYAWDVVNEAVEDKTDLFMRDTKWLELVGEDYLLQAFSMAHEADPNALLFYNDYNETDPVKREKIYNLVRSLLDKGAPVHGIGLQGHWNIHGPSIEEIRMAIERYASLDVQLHVTELDMSVFRHEDRRTDLTAPTSEMAELQERRYEEIFNLFREYKSSITSVTFWGVADNYTWLDHFPVRGRKNWPFVFDQQLQPKESFWRIINPMS']
# print(type(dict_flatfile['ABC94556.1'][4]),dict_flatfile['ABC94556.1'][4])
# print(type(dict_flatfile['ADU28823.1'][4]), dict_flatfile['ADU28823.1'][4])

# fill in blank items
path_acc = r'F:\subject\active\GH temperature adaptation\sequence data\data\GH\GH10'
# GH10_acc = get_lines(os.path.join(path_acc,'GH10_acc.txt'))
# """remove \n"""
# GH10_acc_pro = [i[:-1] for i in GH10_acc]
#
# acc_key = [key for key,value in dict_flatfile.items()]
# missing_items = [i for i in GH10_acc_pro if i not in acc_key]
#
# if missing_items: # empty list refers to False
#     print('missing_item is not empty\n')
#     with open(os.path.join(path,'missing_gb.txt'),'a+') as gb:
#         for i in missing_items:
#             gb.write(i)
#             gb.write('\n')
# else:
#     print('missing_item is empty\n')

# data formatting and storing in a new file
"""
>accessiong, domain, enzyme name, source, taxonomy, region annotation
sequence
"""

writeinfo = []
with open(os.path.join(path_acc,'annotation_by_ncbi.csv'),'w+',newline='') as f:
    with open(os.path.join(path_acc, 'sequence.txt'), 'w+', newline='') as seq:
        writecsv = csv.writer(f)
        writecsv.writerow(['Accession_num','Domain(BCT\PLN\VAR\Other)','Enzyme_name','Source','Taxonomy','Region_annotation','Sequence','Species taxid','Optimal temperature'])
        for key,value in dict_flatfile.items():
            # only 'GH10' in value[4]
            if type(value[4]) == str:
                writecsv.writerow([key, value[0], value[1], value[2], ';'.join(value[3]), value[4], value[5].upper(),value[6],value[7]])
                seq.write(value[5].upper())
            # one region
            if type(value[4]) == list:
                if type(value[4][0]) == str:
                    single_region = []
                    single_region.append(re.search(r'\d+\.\.\d+',re.sub('<|>','',value[4][0])).group(0))
                    single_region.append(value[4][1].split('=')[1].replace('"',''))
                    single_region = ' | '.join(single_region)
                    begin = int(re.search(r'\d+\.\.\d+', re.sub('<|>', '', value[4][0])).group(0).split('..')[0])
                    end = int(re.search(r'\d+\.\.\d+', re.sub('<|>', '', value[4][0])).group(0).split('..')[1])
                    writecsv.writerow([key, value[0], value[1], value[2], ';'.join(value[3]), single_region, value[5][begin:end+1].upper(),value[6],value[7]])
                    seq.write(value[5][begin:end+1].upper())
                # more than one region
                if type(value[4][0]) == list:
                    for i in value[4]:
                        single_region = []
                        if re.match(r'Glyco',i[1].split('=')[1].replace('"','')):
                            single_region.append(re.search(r'\d+\.\.\d+', re.sub('<|>', '', i[0])).group(0))
                            single_region.append(i[1].split('=')[1].replace('"', ''))
                            begin = int(re.search(r'\d+\.\.\d+', re.sub('<|>', '', i[0])).group(0).split('..')[0])
                            end = int(re.search(r'\d+\.\.\d+', re.sub('<|>', '', i[0])).group(0).split('..')[1])
                            single_region = ' | '.join(single_region)
                            writecsv.writerow([key, value[0], value[1], value[2], ';'.join(value[3]), single_region,
                                               value[5][begin:end + 1].upper(),value[6],value[7]])
                            seq.write(value[5][begin:end + 1].upper())

with open(os.path.join(path_acc, 'sequence.txt'), 'r') as f:
    content = f.readlines()
    aa_frequence = Counter(str(content))
    print(aa_frequence)

alnseq = []
path_aln = r'F:\subject\active\GH temperature adaptation\sequence data\data\dbcan2\dbCAN-fam-aln-V9'
with open(os.path.join(path_aln,'GH10.aln'),'r') as f:
    content = f.readlines()
    for i in content:
        if '>' not in i:
            alnseq.append(i)
aa_aln_result = Counter(str(''.join(alnseq)))
print(aa_aln_result)
#



