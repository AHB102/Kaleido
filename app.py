from flask import Flask, render_template, request, send_file
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
from transformers import pipeline
from flask import Flask, render_template, request
# from visualize import   generate_line_chart, generate_scatter_plot, generate_histogram
from analysis import classifier

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return "Empty file uploaded"

    # Check if the file is a CSV
    if file and file.filename.endswith('.csv'):
        # Read the CSV file
        df = pd.read_csv(file)
        
        # Get form data
        x_parameter = request.form['x_parameter']
        y_parameter = request.form['y_parameter']
        chart_type = request.form['chart_type']
        
        # Generate chart based on selected chart type
        if chart_type == 'line':
            generate_line_chart(df, x_parameter, y_parameter)
            return render_template('line_chart.html')
        elif chart_type == 'scatter':
            generate_scatter_plot(df, x_parameter, y_parameter)
            return render_template('scatter_plot.html')
        elif chart_type == 'histogram':
            generate_histogram(df, x_parameter)
            return render_template('histogram.html')

    return "Unsupported file format"


@app.route('/classify', methods=['GET', 'POST'])
def classify_tweet():
    if request.method == 'POST':
        tweet = request.form.get('tweet', '')
        if tweet:
            # Classify the tweet
            sentiment_label = classifier(tweet)[0]
            label = sentiment_label['label']
            return render_template('classify.html', tweet=tweet, sentiment=label)

    return render_template('classify.html', tweet='', sentiment='')


# Add functions to generate other types of charts here
import matplotlib as plt 
import seaborn as sns
import pandas as pd 
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



if __name__ == '__main__':
    app.run(debug=True)
