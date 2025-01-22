# coding: utf-8
import spacy
nlp = spacy.load('en_core_web_lg')
from pathlib import Path
document1 = nlp(Path('pg1513.txt').read_text())
document2 = nlp(Path('pg20288.txt').read_text())
document1.similarity(document2)
nlp = spacy.load('en_core_web_md')
document1 = nlp(Path('pg1513.txt').read_text())
document2 = nlp(Path('pg20288.txt').read_text())
document1.similarity(document2)
nlp = spacy.load('en_core_web_sm')
document1 = nlp(Path('pg1513.txt').read_text())
document2 = nlp(Path('pg20288.txt').read_text())
document1.similarity(document2)
