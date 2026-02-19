import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (df)


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
counts.sort()

bar_labels = ['red', 'blue', '_red', 'orange']
#bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
bar_colors = ['#FF5733', '#3498DB', '#C70039', '#F1C40F']  # Example hex colors

#alpha=0.5 → 50% transparency. alpha=0.7 → 70% opaque. zorder brings the chart to the front
ax.bar(fruits, counts, label=bar_labels, color=bar_colors, alpha=0.8, zorder = 3) 
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

# Customize gridlines
ax.grid(color='#cecece', linestyle='-', linewidth=0.8, axis='both', zorder = 0)  # Gray dashed gridlines on y-axis

# Change the color of the box (spines) around the chart using a hex color
hex_color = '#cecece'  
for spine in ax.spines.values():
    spine.set_edgecolor(hex_color)  # Use the hex color
    spine.set_linewidth(1)          # Optional: Set the thickness of the spines

plt.show()

