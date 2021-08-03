# Why are we doing this?
We are managing to build a protein properties database for deep learning and future feature analysis. 
It has been wildly accepted that the quantity and quality of database are crucial to the performance of deep learning or other machine learning methods. 

But up to now, it is tough to obtain a proper and open resources database for applying machine learning technology such as Penn Tree Bank corpus serving for NLP. 


This package aims to assemble a varity of biological database for public usage, and rebuild a functional and easy-to-use protein properties database. 
Finally, we will establish the database on Mariadb and also provide online user download interface.

First of all, We downloaded the accession number of CAZy from database dbscan2, in which the sequences were stored in fasta format.

We crawled the genbank flatfiles based on the given accession number, and parsered for a series of key information, including annotation of protein regions. Because the protein sequences is a full length protein sequences.

Based on the taxonomy of donor cell, we assigned the optimal temperature condition, and we assumed the optimal temperature of enzymes are consistent with the cell environment.

Therefore, we obtained the protein sequences with temperature label. Besides, Domain(BCT\PLN\VAR\Other), Enzyme_name, Source, Taxonomy, Region_annotation, Sequence, Species, taxid and Optimal temperature are also included into MariaDB for efficient calculation.
