import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col = 'date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
(df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(df.index, df.value, color='red',lw=1,)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_ylabel("Page Views")
    ax.set_xlabel('Date')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month'] = pd.to_datetime(df.index).month
    df['year'] = pd.to_datetime(df.index).year
    df_bar = df.groupby(['year','month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot.bar(ylabel="Average Page Views", xlabel = 'Years', figsize=(10,7)).figure
    plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December'],title = "Months")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in pd.to_datetime(df_box['date'])]
    df_box['month'] = [d.strftime('%b') for d in pd.to_datetime(df_box.date)]

    # Draw box plots (using Seaborn)
    df_box['month_number'] = pd.to_datetime(df_box['date']).dt.month
    df_box =df_box.sort_values("month_number")

    fig, (ax1,ax2) = plt.subplots(1,2,figsize=(12,6))
    ax1 = sns.boxplot( x = df_box['year'], y= df_box['value'], ax=ax1)
    ax2 = sns.boxplot( x = df_box['month'], y= df_box['value'],  ax=ax2)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
