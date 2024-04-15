# Importing the necessary libraries
import requests
import os  #python library to interect with operating systems awais



# The URL of the website you want to scrape
url = 'https://en.wikipedia.org/wiki/Data_analysis'

# Function to fetch content from URL and save it as a text file
def fetch_and_save_to_file(url, path):
    # Send HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Write the content to a file
        with open(path, 'w', encoding='utf-8') as file:
            file.write(response.text)
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Calling the function with the specified URL and file path
fetch_and_save_to_file(url, "data/wikipedia_data_analysis.html")

#a new line added
#one more line added

