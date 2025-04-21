from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)
api = Api(app)
auth = HTTPTokenAuth(scheme='Bearer')

# Modèle de la base de données
class OrderModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.String, nullable=False)

# Vérification du jeton d'authentification
@auth.verify_token
def verify_token(token):
    return token == "my_secure_token"

# Arguments des requêtes pour les commandes
order_parser = reqparse.RequestParser()
order_parser.add_argument('product_name', type=str, required=True, help='Product name cannot be blank!')
order_parser.add_argument('quantity', type=int, required=True, help='Quantity cannot be blank!')
order_parser.add_argument('price', type=float, required=True, help='Price cannot be blank!')
order_parser.add_argument('order_date', type=str, required=True, help='Order date cannot be blank!')

# Champs de réponse pour la sérialisation
resource_fields = {
    'id': fields.Integer,
    'product_name': fields.String,
    'quantity': fields.Integer,
    'price': fields.Float,
    'order_date': fields.String
}

# Gestion des commandes
class Order(Resource):
    @auth.login_required
    @marshal_with(resource_fields)
    def get(self, order_id):
        order = OrderModel.query.get_or_404(order_id)
        return order

    @auth.login_required
    @marshal_with(resource_fields)
    def put(self, order_id):
        args = order_parser.parse_args()
        order = OrderModel(id=order_id, **args)
        db.session.add(order)
        db.session.commit()
        return order, 201

    @auth.login_required
    @marshal_with(resource_fields)
    def patch(self, order_id):
        args = order_parser.parse_args()
        order = OrderModel.query.get_or_404(order_id)
        if 'product_name' in args:
            order.product_name = args['product_name']
        if 'quantity' in args:
            order.quantity = args['quantity']
        if 'price' in args:
            order.price = args['price']
        if 'order_date' in args:
            order.order_date = args['order_date']
        db.session.commit()
        return order

    @auth.login_required
    def delete(self, order_id):
        order = OrderModel.query.get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return '', 204

# Recherche de commandes par nom de produit
class OrderSearch(Resource):
    @auth.login_required
    @marshal_with(resource_fields)
    def get(self, product_name):
        orders = OrderModel.query.filter(OrderModel.product_name.like(f'%{product_name}%')).all()
        if not orders:
            abort(404, message="No orders found with the product name containing '{}'".format(product_name))
        return orders

# Ajout des ressources à l'API
api.add_resource(Order, '/order/<int:order_id>')
api.add_resource(OrderSearch, '/ordersearch/<string:product_name>')

# Initialisation de la base de données dans le bon contexte
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
