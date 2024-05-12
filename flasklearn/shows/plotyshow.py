from flask import Flask, render_template
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris.csv')
    data = [
        go.Scatter(
            x=df[df['Name'] == cls]['SepalWidth'],
            y=df[df['Name'] == cls]['SepalLength'],
            mode='markers',
            name=cls
        ) for cls in df['Name'].unique()
    ]
    layout = go.Layout(
        xaxis=dict(title='Sepal Width'),
        yaxis=dict(title='Sepal Length')
    )
    fig = go.Figure(data=data, layout=layout)
    return render_template('index.html', plot=fig.to_html(full_html=False))

if __name__ == '__main__':
    app.run(debug=True)