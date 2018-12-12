import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('CSE New Data.csv')

classes = df.groupby(['Dining Hall'])['School'].value_counts(normalize=False).rename('Count').reset_index()

print(classes)

that = sns.barplot(x="Dining Hall", y="Count", hue="School", data=classes)
plt.xticks(rotation=60)
plt.title('Dining Hall Attendance by School')
# plt.show()

years = df.groupby(['Dining Hall'])['Year'].value_counts(normalize=False).rename('Count').reset_index().sort_values(['Year'])

that = sns.barplot(x="Dining Hall", y="Count", hue="Year", data=years)
plt.xticks(rotation=60)
plt.title('Dining Hall Attendance by Year')

print(df.groupby('School').count())
print(df.groupby('Year').count())
# plt.show()



