#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple DOCX text extractor: reads word/document.xml and writes concatenated text to .txt files.
Usage: run without args; it looks for the three project docx files in the repo root.
"""
import os
import zipfile
import xml.etree.ElementTree as ET

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = [
    '作业1-博客平台愿景与范围.docx',
    '作业2-博客平台需求规格说明(1).docx',
    '设计规格说明模板.docx',
]

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

for fname in files:
    path = os.path.join(root, fname)
    outname = os.path.splitext(fname)[0] + '.txt'
    outpath = os.path.join(root, outname)
    if not os.path.exists(path):
        print(f"SKIP: {path} not found")
        continue
    try:
        with zipfile.ZipFile(path) as z:
            with z.open('word/document.xml') as docxml:
                tree = ET.parse(docxml)
                root_elem = tree.getroot()
                texts = []
                for t in root_elem.findall('.//w:t', ns):
                    texts.append(t.text if t.text is not None else '')
                full = '\n'.join(texts)
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(full)
        print(f"WROTE: {outpath}")
    except Exception as e:
        print(f"ERROR processing {path}: {e}")
