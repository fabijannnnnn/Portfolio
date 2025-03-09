import requests
import os


def download_images(query, num_images, api_k):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={num_images}"

    headers = {
        "Authorization": api_k
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        directory = os.path.join("docs/images", query)
        data = response.json()

        if not os.path.exists(directory):
            os.makedirs(directory)

        for i, photo in enumerate(data['photos']):
            image_url = photo['src']['original']
            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                image_name = os.path.join(directory, f"{query}_{i + 1}.jpg")
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
download_images("dog", 10, api_key)
