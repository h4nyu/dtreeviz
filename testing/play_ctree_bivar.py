import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from dtreeviz.trees import *

know = pd.read_csv("data/knowledge.csv")
class_names = ['very_low', 'Low', 'Middle', 'High']
know['UNS'] = know['UNS'].map({n: i for i, n in enumerate(class_names)})

max_depth=3
X_train = know.drop('UNS', axis=1)
y_train = know['UNS']
figsize = (6,5)
fig, ax = plt.subplots(1, 1, figsize=figsize)
ctreeviz_bivar(ax, X_train, y_train, max_depth=max_depth, features=[4,3],
               feature_names = ['PEG','LPR'],
               class_names=class_names,
               target_name='Knowledge')
plt.tight_layout()
plt.savefig(f"/tmp/knowlege-bivar-classtree-depth-{max_depth}.svg", bbox_inches=0, pad_inches=0)
plt.show()