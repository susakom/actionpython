# Susak Oleksandr 
import argparse
import re

from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, inputs
from flask_cors import CORS
from db import (ProductModel,
                create_product,
                get_product_by_id,
                update_product,
                delete_product)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)


# Define the resources
class Products(Resource):
    def get(self):
        return [product.to_dict() for product in ProductModel.select()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("price", type=float, required=True)
        args = parser.parse_args()

        data = {
            "name": args["name"],
            "price": args["price"]
        }
        product = create_product(**data)

        return {"message": "Product added successfully.", "productId": product.id}, 201


class Product(Resource):
    def get(self, product_id):
        product = get_product_by_id(product_id)
        if product:
            return product.to_dict()
        else:
            return {"error": "Product not found."}, 404

    def patch(self, product_id):
        product = get_product_by_id(product_id)
        if not product:
            return {"error": "Product not found."}, 404

        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        parser.add_argument("price", type=float)
        args = parser.parse_args()
        data = {
            "product_id": product_id
        }
        if args["name"]:
            data["name"] = args["name"]
        if args["price"]:
            data["price"] = args["price"]
        update_product(**data)
        return {"message": "Product updated successfully."}, 200

    def delete(self, product_id):
        product = get_product_by_id(product_id)
        if not product:
            return {"error": "Product not found."}, 404
        delete_product(product_id)

        return {"message": "Product deleted."}, 200


# Add the resources to the API
api.add_resource(Products, "/api/products")
api.add_resource(Product, "/api/products/<int:product_id>")



if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))  # Получаем порт из переменной окружения, по умолчанию 5000
   app.run(host="0.0.0.0", port=port, debug=True)
