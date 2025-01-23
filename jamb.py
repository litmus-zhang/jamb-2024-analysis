import pandas as pd
import os

import kagglehub
import matplotlib.pyplot as plt
import seaborn as sns


# Download latest version
path = kagglehub.dataset_download("idowuadamo/students-performance-in-2024-jamb")


# read data from path using pandas
df = pd.read_csv(os.path.join(path, 'jamb_exam_results.csv'))

df.describe().T
df.isnull().sum()
df.info()
df[df['JAMB_Score'] == df['JAMB_Score'].max()]

df.dropna(inplace=True)
# parental educational level on jamb score
import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(10,8))
sns.histplot(data=df, x='JAMB_Score', hue='Parent_Education_Level')
plt.show()

df['Parent_Education_Level'].unique()


# group the parental education by jamb score average
data_pel = df.groupby('Parent_Education_Level')['JAMB_Score'].mean()

grouped_data = df.groupby('Study_Hours_Per_Week')['JAMB_Score'].mean().reset_index()
