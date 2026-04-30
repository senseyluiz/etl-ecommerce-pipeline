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
if __name__ == "__main__":
    products = extract_products()