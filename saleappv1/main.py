from flask import render_template
from saleappv1 import app, utils


@app.route("/")
def hello_world():
    products = utils.read_data()
    return render_template('index.html', products=products)


@app.route('/products')
def products_list():
    products = utils.read_data()
    return render_template('product-list.html', products=products)


if __name__ == "__main__":
    app.run(debug=True)
