import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas  as pd

# # Existing datasets 
# print(sns.get_dataset_names())

penguins = sns.load_dataset('penguins') 

print(penguins.head(5))

# # Printing the statistics data 
# print(penguins.describe())

# # Plotting a boxplot 
# sns.boxplot(penguins['bill_length_mm'])

# # Plotting a boxplot with x and y axis data
# sns.boxplot(x = penguins['island'] , y = penguins['bill_length_mm'] )

# # Plotting a boxplot with x and y axis data with hue 
# sns.boxplot(x = penguins['island'] , y = penguins['bill_length_mm'] , hue=penguins['sex'])

# # Plotting a boxplot with x and y axis data with hue and order and color
# sns.boxplot(x=penguins['island'], y=penguins['bill_length_mm'], hue=penguins['sex'], order=['Dream', 'Torgersen', 'Biscoe'], color='r')

# # Plotting a boxplot with x and y axis data with hue and order and color and width
# sns.boxplot(x=penguins['island'], y=penguins['bill_length_mm'], hue=penguins['sex'], order=['Dream', 'Torgersen', 'Biscoe'], color='r', width=0.5)

# # Changing the viscos line width using 'whis' property
# sns.boxplot(x=penguins['island'], y=penguins['bill_length_mm'], hue=penguins['sex'], order=['Dream', 'Torgersen', 'Biscoe'], color='r', width=0.5, whis=0.5)

# We can hide the viscos line using 'showcaps' property to False
sns.boxplot(x=penguins['island'], y=penguins['bill_length_mm'], hue=penguins['sex'], order=['Dream', 'Torgersen', 'Biscoe'], color='r', width=0.5, showcaps=False)

# Showing the box plot
plt.show()

