import requests
from bs4 import BeautifulSoup
import re
import html2text

# Function to fetch HTML content from a URL
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch HTML from URL: {url}")
        return None

# Function to convert HTML content to Markdown
def html_to_markdown(html):
    soup = BeautifulSoup(html, 'html.parser')
    markdown = html2text.html2text(str(soup), bodywidth=0)
    return markdown

# Function to convert URL to Markdown
def url_to_markdown(url):
    html = fetch_html(url)
    if html is not None:
        markdown = html_to_markdown(html)
        return markdown
    else:
        return None

# Main function
if __name__ == '__main__':
    url = "https://github.com/Subham-Maity/docker_tutorial#-stop-running-all-containers"
    markdown = url_to_markdown(url)
    if markdown is not None:
        print("Converted Markdown:")
        print(markdown)
