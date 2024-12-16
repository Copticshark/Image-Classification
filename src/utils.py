import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/image_labels_raw.csv')

# generate bar graph with category counts
label_counts = df['label'].value_counts()
label_counts.plot(kind='bar', color='#30D5C8')
plt.title('Distribution of Items by Category')
plt.xlabel('Category')
plt.ylabel('Number of Items')
plt.show()

# generate pie chart with categories that need to be checked
