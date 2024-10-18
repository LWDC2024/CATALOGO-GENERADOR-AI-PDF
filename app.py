from flask import Flask, render_template, request, send_file
import pdfkit
import io
import requests

app = Flask(__name__)

def get_products():
    # Aquí deberías implementar la lógica para obtener los productos de tu sitio web
    # Por ahora, usaremos datos de ejemplo
    return [
        {"name": "Producto 1", "price": "19.99"},
        {"name": "Producto 2", "price": "29.99"},
        {"name": "Producto 3", "price": "39.99"},
    ]

@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products)

@app.route('/generate_pdf')
def generate_pdf():
    products = get_products()
    
    rendered = render_template('catalog.html', products=products)
    
    pdf = pdfkit.from_string(rendered, False)
    
    return send_file(
        io.BytesIO(pdf),
        attachment_filename='catalogo.pdf',
        mimetype='application/pdf'
    )

@app.route('/view_pdf')
def view_pdf():
    products = get_products()
    
    rendered = render_template('catalog.html', products=products)
    
    pdf = pdfkit.from_string(rendered, False)
    
    return send_file(
        io.BytesIO(pdf),
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)