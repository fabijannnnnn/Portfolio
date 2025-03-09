import requests
import os

def download_images(query, num_images, api_key):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={num_images}"

    headers = {
        "Authorization": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if not os.path.exists(query):
            os.makedirs(query)

        for i, photo in enumerate(data['photos']):
            image_url = photo['src']['original']
            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                image_name = os.path.join(query, f"{query}_{i + 1}.jpg")
                with open(image_name, 'wb') as f:
                    f.write(image_response.content)
                print(f"Downloaded {query}_{i + 1}.jpg")
            else:
                print(f"Failed to download image {i + 1}")
    else:
        print(f"Error: Unable to retrieve images for {query}")

api_key = "IvLrAJCAjkbH8b0QuZNAdsjkseWzNB2Jl1IfxX5fyH1DWA3PFfECHen9"

# Download 10 images of cats and snakes
download_images("cat", 10, api_key)
download_images("snake", 10, api_key)



























# import requests
# from duckduckgo_search import DDGS
# from pprint import pprint
#
# url = "https://duckduckgo.com/?t=h_&q=cat&iax=images&ia=images"
# # url = "https://www.google.com/search?tbm=isch&q=cat&tbs=imgo:1"
# r = requests.get(url)
# print(r.content)  # obecný obsah (bytes)
# print(r.text)  # dekódovaný text
# print("<img" in r.text.lower())
#
# with DDGS() as ddgs:
#     results = [r for r in ddgs.images("cat", max_results=5)]
#     pprint(results)
