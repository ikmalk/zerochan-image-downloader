import json
import os
from urllib.parse import urlparse

import requests

def save_image_from_url(url, folder_path):
    # Parse the file name from the URL
    file_name = os.path.basename(urlparse(url).path)

    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Full path for saving the file
    file_path = os.path.join(folder_path, file_name)

    # Headers to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36'
    }

    try:
        # Download the image
        response = requests.get(url, stream=True, headers=headers)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

        else:
            print(
                f"Failed to download image. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# START
have_creds_file = os.path.isfile("creds.json")
project_name = "My Image Downloader"
username = ""
valid = False

if have_creds_file:
    with open('creds.json', 'r') as file:
        data = json.load(file)
        p_name = data.get("project_name")
        u_name = data.get("username")
        valid = p_name and u_name
        if valid:
            project_name = p_name
            username = u_name

if not valid:
    project_name = input("Your project name (e.g 'My Image Downloader'): ")
    username = input("Your Zerochan Username: ")
    with open('creds.json', 'wt') as file:
        json.dump({
            "project_name": project_name,
            "username": username
        }, file)
search_query = input("Your search query: ")

headers = {
    "User-Agent": f"{project_name} - {username}"
}
page = 1
limit = 250
while True:
    req = requests.get(
        f"https://www.zerochan.net/{search_query}?json&p={page}&l={limit}", headers=headers)
    data = req.json()
    items = data.get("items")
    if items:
        print(f"Downloading images for page {page}: {len(items)} images")
        for it in items:
            # print(it)
            url = it["thumbnail"]
            folder_path = f"images"
            save_image_from_url(url, folder_path)
        page = page + 1
    else:
        print("Reached the end of page")
        break
