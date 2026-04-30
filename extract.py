import requests

def extract_products():
    PRODUCTS_URL = "https://fakestoreapi.com/products"
    response = requests.get(PRODUCTS_URL)
    response.raise_for_status()
    data = response.json()

    # Extrair dados dos produtos a serem utilizados
    products = []
    for product in data:
        product_data = {
            "id": product["id"],
            "name": product["title"],
            "category": product["category"],
            "price": float(product["price"])
        }
        products.append(product_data)
    return products

def extract_cart_products():
    SALES_URL = "https://fakestoreapi.com/carts"
    response = requests.get(SALES_URL)
    response.raise_for_status()
    data = response.json()
    sales = []
    # Extrair dados necessários do carrinho
    for sale in data:
        sale_data = {
            "cart_id": sale["id"],
            "user_id": sale["userId"],
            "date": sale["date"],
            "products":[
                {
                    "product_id": product["productId"],
                    "quantity": int(product["quantity"])
                }
                for product in sale["products"]
            ]
        }
        sales.append(sale_data)
    return sales
if __name__ == "__main__":
    products = extract_products()
    cart_products = extract_cart_products()
