import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots()
    plt.scatter(x, y)
    
    # Create first line of best fit
    res = linregress(x,y)
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = res.slope*x_pred + res.intercept
    plt.plot(x_pred,y_pred,"r")

    # Create second line of best fit
    sec_df = df.loc[df['Year'] >= 2000]
    sec_x = sec_df['Year']
    sec_y = sec_df['CSIRO Adjusted Sea Level']
    sec_res = linregress(sec_x,sec_y)
    sec_x_pred = pd.Series([i for i in range(2000,2051)])
    sec_y_pred = sec_res.slope*sec_x_pred + sec_res.intercept
    plt.plot(sec_x_pred,sec_y_pred,"green")

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()