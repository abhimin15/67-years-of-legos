import pandas as pd
import matplotlib.pyplot as plt


colors = pd.read_csv('colors.csv')

# How many distinct colors are available?
num_colors = len(colors['name'].unique())

# colors_summary: Distribution of colors based on transparency
colors_summary = colors.groupby('is_trans').count()
print(colors_summary)

# Read sets data as `sets`
sets = pd.read_csv('sets.csv')

# Create a summary of average number of parts by year: `parts_by_year`
sets['part'] = sets.groupby('year')['num_parts'].mean()
parts_by_year = sets[['year','part']].sort_values('year')
# Plot trends in average number of parts by year
plt.scatter(parts_by_year['year'],parts_by_year['part'])
plt.show()

# themes_by_year: Number of themes shipped by year
themes_by_year = sets[['year','theme_id']].groupby('year',as_index=False).agg({'theme_id':'count'})
print(themes_by_year.head(5))
