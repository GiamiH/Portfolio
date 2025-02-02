from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Open and read file
script_dir = Path(__file__).resolve().parent
data_path = script_dir.parent / "Data" / "News.csv"
data = pd.read_csv(data_path, index_col=0)
#print(data.head())
#print(data.shape) #44,919 rows & 5 columns
data = data.drop(["title", "subject","date"], axis = 1)

# Shuffle data model to prevent bias
data = data.sample(frac=1)
data.reset_index(inplace=True)
data.drop(["index"], axis=1, inplace=True)

sns.countplot(data=data,
              x='class',
              order=data['class'].value_counts().index)
plt.show()
## change bar colors