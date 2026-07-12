'''
utils.py    Reusable helper functions for Healthcare Analysis Project
'''

from pathlib import Path 
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGE_DIR = BASE_DIR / "Images"
IMAGE_DIR.mkdir(exist_ok = True)


# Plot Style

plt.style.use('ggplot')
sns.set_theme(style='whitegrid')

# Save Figure

def save_plot(filename):
    '''Save current matplotlib figure'''
    plt.tight_layout()
    plt.savefig(IMAGE_DIR / filename, dpi=300, bbox_inches= 'tight')
    print(f'plot saved ->{filename}')
    plt.show()
    

'''Bar Chart Function'''

def bar_plot(data,column, title, xlabel, ylabel, color='steelblue'):
    plt.figure(figsize=(10,6))
    sns.countplot(data=data, x=column, color=color, order=data[column].value_counts().index)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    save_plot(f'{column.lower().replace(' ', '_')}.png')
  
  
'''Histogram Function'''  

def histogram(data, column, bins=30, color="skyblue"):
    plt.figure(figsize=(10,6))
    sns.histplot(data[column], bins = bins, kde=True, color=color)
    plt.title(f"{column} Distribution")
    plt.xlabel(column)
    plt.ylabel('Frequency')
    
    
    save_plot(f"{column.lower().replace(' ', "_")}_disribution.png")

'''Pie Chart'''

def pie_chart(data, column):
    plt.figure(figsize=(8,8))
    data[column].value_counts().plot(kind='pie', autopct="%1.1f%%")
    plt.ylabel("")
    plt.title(column)

    save_plot(f"{column.lower().replace(' ', '_')}_pie.png")
    
'''Box Plot'''

def box_plot(data, column, color = 'orange'):
    plt.figure(figsize=(8,5))
    sns.boxplot(x=data[column], color=color)
    plt.title(f"{column} Box Plot")
    save_plot(f"{column.lower().replace(' ', '_')}_boxplot.png")
    
    
'''Value Counts'''

def print_value_counts(data, column):
    
    print("="*60)
    print(column.upper())
    print("="*60)
    
    
    print(data[column].value_counts())