# Zerochan Image Downloader

Simple python CLI for downloading Zerochan images from query utilizing python requests and Zerochan's public API.

## Installation:
```bash
git clone https://github.com/ikmalk/zerochan-image-downloader.git
cd zerochan-image-downloader
pip install -r requirements.txt 
```

## Run the CLI
After Installation you can run:  
```bash
python zerochan.py
```

Output
```bash
Your project name (e.g 'My Image Downloader'): My Image Downloader # First time run
Your Zerochan Username: Username1234 # First time run
Your search query: warashiZ 
# Your search query: Star+Rail // query with space
# Your search query: Lumine,Flower // query with multiple tags
```
Images will be saved in the `images` folder


Please follow Zerochan's API Policy when using the CLI i.e. running more CLI instances than the rate limit is allowed. For more info, read at [here](https://www.zerochan.net/api)

