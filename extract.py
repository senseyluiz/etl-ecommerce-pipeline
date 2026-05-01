import requests
import json

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
        for sale_item in sale["products"]:
            sale_data = {
                "cart_id": sale["id"],
                "user_id": sale["userId"],
                "date": sale["date"][:10],
                "product_id": sale_item["productId"],
                "quantity": int(sale_item["quantity"])
            }
            sales.append(sale_data)
    return sales
if __name__ == "__main__":
    products = extract_products()
    cart_products = extract_cart_products()

    # Salvar Produtos
    with open("data/products.json", "w") as outfile:
        json.dump(products, outfile, indent=4)

    # Salvar vendas
    with open("data/carts.json", "w") as outfile:
        json.dump(cart_products, outfile, indent=4)

    print("\33[32m Dados extraídos e salvos com sucesso! \33[m")
