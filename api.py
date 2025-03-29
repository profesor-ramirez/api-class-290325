from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, reqparse, Resource, fields, marshal_with, abort
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)
CORS(app, resources={r"/api/*": {"origins":"*"}})

class ProductModel(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    name= db.Column(db.String(50), unique=True, nullable=False)
    price= db.Column(db.Integer, nullable=False)
    description= db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"Product( name = {self.name}, price = {self.price}, description = {self.description})"

product_args = reqparse.RequestParser()
product_args.add_argument("name", type=str, required=True, help="El name no puede ser nulo")
product_args.add_argument("price", type=int, required=True, help="El precio no puede ser nulo")
product_args.add_argument("description", type=str, required=True, help="La descripcion no puede ser nula")

product_fields = {
    'id':fields.Integer,
    'name':fields.String,
    'price':fields.Integer,
    'description':fields.String,
}

class Products(Resource):
    @marshal_with(product_fields)
    def get(self):
        products = ProductModel.query.all()
        return products
    
    @marshal_with(product_fields)
    def post(self):
        args = product_args.parse_args()
        product = ProductModel(name = args["name"], price = args["price"], description = args["description"])
        db.session.add(product)
        db.session.commit()
        products = ProductModel.query.all()
        return products, 201

class Product(Resource):
    @marshal_with(product_fields)
    def get(self, id):
        product = ProductModel.query.filter_by(id=id).first()
        if not product:
            abort(404, message="Producto no encontrado")
        return product
    
    @marshal_with(product_fields)
    def patch(self, id):
        product = ProductModel.query.filter_by(id=id).first()
        if not product:
            abort(404, message="Producto no encontrado")
        args = product_args.parse_args()
        product.name = args["name"]
        product.price = args["price"]
        product.description = args["description"]
        db.session.commit()
        return product
    
    @marshal_with(product_fields)
    def delete(self, id):
        product = ProductModel.query.filter_by(id=id).first()
        if not product:
            abort(404, message="Producto no encontrado")
        db.session.delete(product)
        db.session.commit()
        products = ProductModel.query.all()
        return products
    
    #PUT  y PATCH -> PATCH
    
api.add_resource(Products, "/api/products/")
api.add_resource(Product,"/api/products/<int:id>")

@app.route("/")
def inicio():
    return "<h1>Esto es el inicio del api</h1>"

if __name__ == '__main__':
    app.run(debug=True)