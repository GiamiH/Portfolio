from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Get the absolute path of the current script
script_dir = Path(__file__).resolve().parent
data_path = script_dir.parent / "Data" / "News.csv"
data = pd.read_csv(data_path, index_col=0)
print(data.head())