import requests

BASE = "http://127.0.0.1:5000/"
TOKEN = "my_secure_token"
headers = {"Authorization": f"Bearer {TOKEN}"}

# Test PUT request to create a new order
response = requests.put(BASE + "order/1", json={"product_name": "Laptop", "quantity": 3, "price": 1200.50, "order_date": "2024-08-12"}, headers=headers)
print("PUT /order/1:", response.text)

# Test GET request to retrieve the order
response = requests.get(BASE + "order/1", headers=headers)
print("GET /order/1:", response.text)

# Test PATCH request to update the order
response = requests.patch(BASE + "order/1", json={"product_name": "Gaming Laptop", "price": 1350.00}, headers=headers)
print("PATCH /order/1:", response.text)

# Test GET request again to see the updated order
response = requests.get(BASE + "order/1", headers=headers)
print("GET /order/1:", response.text)

# Test DELETE request to delete the order
response = requests.delete(BASE + "order/1", headers=headers)
print("DELETE /order/1:", response.status_code)

# Test GET request again to see if the order is deleted
response = requests.get(BASE + "order/1", headers=headers)
if response.status_code == 404:
    print("GET /order/1: Order not found (as expected)")
else:
    print("GET /order/1:", response.text)

# Test GET request to search for orders by product name
response = requests.get(BASE + "ordersearch/Laptop", headers=headers)
print("GET /ordersearch/Laptop:", response.text)
