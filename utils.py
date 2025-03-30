# Fetches JSON data from a given URL
import requests

def fetch_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"❌ Error fetching data from {url}: {e}")
        return None
