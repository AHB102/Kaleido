import matplotlib as plt 
import seaborn as sns
import pandas as pd 


def generate_bar_chart(df, x_parameter, y_parameter):
    # Discretize data for the bar chart
    df_discretized = df[[x_parameter, y_parameter]].copy()
    df_discretized[x_parameter] = pd.cut(df_discretized[x_parameter], bins=10)  # Adjust the number of bins as needed

    # Calculate mean of Y parameter for each category
    df_grouped = df_discretized.groupby(x_parameter, as_index=False)[y_parameter].mean()

    # Create bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_parameter, y=y_parameter, data=df_grouped)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.xlabel(x_parameter)
    plt.ylabel('Mean ' + y_parameter)
    plt.title('Mean ' + y_parameter + ' by ' + x_parameter)
    plt.tight_layout()
    plt.savefig('static/chart.png')
    plt.close()

import numpy as np

def generate_line_chart(df, x_parameter, y_parameter):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_parameter, y=y_parameter, data=df)
    plt.xticks(rotation=45) 
    plt.xlabel(x_parameter)
    plt.ylabel(y_parameter)
    plt.title('Line Chart')
    plt.tight_layout()
    plt.savefig('static/chart.png')
    plt.close()

def generate_scatter_plot(df, x_parameter, y_parameter):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_parameter], df[y_parameter])
    plt.xlabel(x_parameter)
    plt.ylabel(y_parameter)
    plt.title('Scatter Plot')
    plt.tight_layout()
    plt.savefig('static/chart.png')
    plt.close()

def generate_histogram(df, x_parameter):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[x_parameter], kde=True)
    plt.xlabel(x_parameter)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.tight_layout()
    plt.savefig('static/chart.png')
    plt.close()

