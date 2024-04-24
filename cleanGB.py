#!/usr/bin/env python
# coding: utf-8

"""
@author: Rodrigo Monjaraz-Ruedas (monroderik@gmail.com)

- Clean GenBank Files and converts them to fasta files

- Input format is a genbank file (.gb) downloaded from GenBank
  can contain a single or multiple sequences.

- Headings retain: Ascention_OrganismName_Code#

Usage: python cleanGB.py [INPUT_FASTA] [OUTPUT_FILE_NAME]

Requires Biopython

NOTE: This program Clean sequences based on factor number 
      if you file have a non traditional name, make sure you double check the output names.

"""
import re
import sys
from Bio import SeqIO

# Get Arguments
gb_file=sys.argv[1]
output_file=sys.argv[2]

sequences = []
for gb_record in SeqIO.parse(open(gb_file,"r"), "genbank"):
    factors_count = len(re.findall(r'\S+', gb_record.description))
    pattern = r'^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+.*$'  
    
    # Set the replacement pattern based on the number of factors
    if factors_count == 14:
        replacement_pattern = r'\1 \2 \5'
    elif factors_count == 13:
        replacement_pattern = r'\1 \2 \4'
    elif factors_count == 12:
        replacement_pattern = r'\1 \2 \3'

    if replacement_pattern:
        tmp_seq_name = re.sub(pattern, replacement_pattern, gb_record.description)
        new_seq_name = re.sub(r"\s+", '_', tmp_seq_name)
        gb_record.id = new_seq_name
        gb_record.description = gb_record.name
        sequences.append(gb_record)   

with open(output_file, "w") as outf:
    SeqIO.write(sequences, outf, "fasta")


