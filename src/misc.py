import requests

def fetch_image(topic: str, api_key: str) -> str:
    endpoint = 'https://api.pexels.com/v1/search'
    headers = {'Authorization': api_key}

    # Make the API request
    response = requests.get(endpoint, params={'query': topic, 'per_page': 1}, headers=headers)
    data = response.json()

    # Get the compressed url
    photo_url = data['photos'][0]['src']['original']
    compressed_url = photo_url + '?auto=compress&cs=tinysrgb&fit=crop&h=400&w=650'

    return compressed_url
       
if __name__ == "__main__":
    fetch_image("", "")