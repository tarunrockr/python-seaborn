import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Existing datasets 
print(sns.get_dataset_names())

# Loading the dataset
tips_dataset = sns.load_dataset('tips')
print(tips_dataset)


# # Drawing a bar chart 
# sns.barplot(x='day', y='total_bill', data=tips_dataset)

# -----------------------------------------------------------------------

# # Hue attribute
# sns.barplot(x='day', y='total_bill', hue='sex', data=tips_dataset)

# -----------------------------------------------------------------------

# # Available color palette values 
# print(sns.color_palette('deep', 10))
# palette1 = sns.color_palette('deep', 10)

# # Setting the palette
# sns.barplot(x='day', y='total_bill', hue='sex', data=tips_dataset, palette=palette1)

# -------------------------------------------------------------------------

# # Creating custom color palettes 
# custom_colors = ['red', 'green', 'blue']
# sns.set_palette(custom_colors)
# palette1 = sns.palplot( sns.color_palette() )
# plt.show()

# # Seting the median as estimator instead of mean
# sns.barplot(x='day', y='total_bill', hue='sex', data=tips_dataset, palette=palette1, order = ['Sat', 'Sun', 'Thur', 'Fri'], estimator=np.median)

# # Drawing the plot
# plt.show()

# ------------------ Using confidence interval --------------------------

# # Size of confidence intervals to draw around estimated values.  If “sd”, skip bootstrapping and draw the standard deviation of the observations. If “None“, no bootstrapping will be performed, and error bars will not be drawn.
# sns.barplot( x='day', y='total_bill', data=tips_dataset, ci=60)

# # setting the capsize
# sns.barplot( x='day', y='total_bill', data=tips_dataset, ci=60, capsize=0.4)

# # Using same color for all bins
# sns.barplot( x='day', y='total_bill', data=tips_dataset, ci=60, capsize=0.4, color='red')

# Setting the color saturation level
sns.barplot( x='day', y='total_bill', data=tips_dataset, ci=60, capsize=0.4, color='red', saturation=0.5)

# Saving the plot as image
fig = sns_plot.get_figure()
fig.savefig(fname = 'figure1.png')

# Drawing the plot
plt.show()


# sns.palplot(sns.color_palette('deep',10))



