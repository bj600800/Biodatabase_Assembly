#!/usr/bin/env python           
# -*- coding:utf-8 -*-          
# @Filename:    pdb_parser.py      
# @Author:      Eric Dou        
# @Time:        2021/5/27 9:02 

"""Function: """
from Bio import PDB
from Bio.PDB import *
import os
from collections import Counter
from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP


path = r'F:\subject\active\GH temperature adaptation\sequence data\data\GH\GH10\pdb\high'
# PDB download
# with open(os.path.join(path,'PDB.txt'),'r') as f:
#     content = f.readlines()
#     for i in content:
#         pdbl = PDBList()
#         pdbl.retrieve_pdb_file(i.strip(), pdir = '.', file_format = 'pdb')
#

# PDB parser
dirname = [name for name in os.listdir(path)
        if os.path.isfile(os.path.join(path, name))]
print(dirname)

pat = 'F:/subject/active/GH temperature adaptation/sequence data/data/GH/GH10/pdb/high/'

# for i in dirname:
#     print(i)
#     l = pat + i
#     print(l)
#     p = PDBParser()
#     structure = p.get_structure(i[:4], l)
#     model = structure[0]
#     dsspi = DSSP(model, l)
#     # for row in dssp:
#     #     with open(os.path.join(path,'dssp.txt'), 'a') as q:
#     #         print(row[1,3])
#     #         q.write(str(row[1:3]))

p = PDBParser()
structure = p.get_structure("1MOT", r"F:\subject\active\GH temperature adaptation\sequence data\data\GH\GH10\pdb\high\1mot.pdb")
model = structure[0]
dssp = DSSP(model, r"F:\subject\active\GH temperature adaptation\sequence data\data\GH\GH10\pdb\high\1mot.pdb")

