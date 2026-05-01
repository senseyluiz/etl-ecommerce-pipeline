import json

def transform_sales():
    with open("../data/products.json", "r") as infile:
        products = json.load(infile)

    with open("../data/sales.json", "r") as infile:
        sales = json.load(infile)

    product_dict = {p["id"]: p for p in products}
    data = []
    for sale in sales:
        product = product_dict.get(sale["product_id"])
        if product:
            data.append({
                "cart_id": sale["cart_id"],
                "user_id": sale["user_id"],
                "product_id": sale["product_id"],
                "product_name": product["name"],
                "category": product["category"],
                "price": product["price"],
                "quantity": sale["quantity"],
                "date": sale["date"],
                "revenue": product["price"] * sale["quantity"]
            })
    return data

if __name__ == "__main__":
    sales = transform_sales()

    # Salva vendas transformadas
    with open("../data/sales_enriched.json", "w") as outfile:
        json.dump(sales, outfile, indent=4)

    print("\33[32m Dados transformados e salvos com sucesso! \33[m")