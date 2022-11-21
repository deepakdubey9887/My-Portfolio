
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:/Learning/AV/python for data science/dataset module1/big_mart_sales.csv')
df=df.pivot_table(index='Item_Fat_Content',columns="Outlet_Size",values="Item_Outlet_Sales")
df.to_html("templates/pivot_table.html",justify='left')
plt.plot(df)

app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
@app.route('/market')
def market_page():
    global items
    return render_template('market.html', items=items)
@app.route('/tables')
def tables():
    return render_template("pivot_table.html")
@app.route("/home/pandas-notebook")
def pandas():
    return render_template("Python For Data Science [Pandas].html")

@app.route("/home/Covid-19-Notebook")
def covid19():
    return render_template("covid-19-analysis-visualization-comparisons.html")

  