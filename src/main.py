import requests

def get_data(url: str) -> dict:
    response = requests.get(url)
    response_data = response.json()
    product_title = response_data[0].get("title")
    return product_title


if __name__ == "__main__":
    url = "https://fakestoreapi.com/products"
    data = get_data(url)
    print(data)
