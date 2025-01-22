# coding: utf-8
from pathlib import Path
from textblob import TextBlob
blob = TextBlob(Path('pg1513.txt').read_text())
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
items = blob.word_counts.items()
items = [item for item in items if item[0] not in stop_words]
from operator import itemgetter
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
sorted_items[0]
top20 = sorted_items[1:21]
top20
import pandas as pd
df = pd.DataFrame(top20, columns=['word', 'count'])
df
get_ipython().run_line_magic('matplotlib', '')
axes = df.plot.bar(x='word', y='count', legend=False)
import matplotlib.pyplot as plt
plt.gcf().tight_layout()
