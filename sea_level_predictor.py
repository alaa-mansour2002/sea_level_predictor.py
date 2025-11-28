
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit (all data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(df['Year'].min(), 2051))
    plt.plot(years_all, res.intercept + res.slope * years_all, 'r', label='Best fit all data')

    # Second line of best fit (from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, 'g', label='Best fit from 2000')

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot
    plt.savefig('sea_level_plot.png')
    plt.show()
    
    return plt.gca()  # For testing purposes
