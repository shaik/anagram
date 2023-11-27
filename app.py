import requests
from bs4 import BeautifulSoup
import re


def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML: {e}")
        return None


def extract_hebrew_words(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Use regular expression to find Hebrew words
    hebrew_words = re.findall(r'\b[\u0590-\u05FF\s]+\b', soup.get_text())

    # Filter out empty strings
    hebrew_words = [word.strip() for word in hebrew_words if word.strip()]



    return hebrew_words


def save_to_file(words, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')


if __name__ == "__main__":
    #url = input("Enter the URL of the HTML page: ").strip()
    url = "https://www.teachmehebrew.com/hebrew-frequency-list.html"
    #output_filename = input("Enter the output filename: ").strip()
    output_filename = "words.txt"

    if not url or not output_filename:
        print("Please provide a valid URL and output filename.")
    else:
        html_content = fetch_html(url)

        if html_content:
            hebrew_words = extract_hebrew_words(html_content)

            if hebrew_words:
                save_to_file(hebrew_words, output_filename)
                print(f"Hebrew words have been saved to '{output_filename}'.")
            else:
                print("No Hebrew words found on the page.")
        else:
            print("Failed to fetch HTML content from the provided URL.")
