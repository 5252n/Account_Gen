import os
import time
import requests
from bs4 import BeautifulSoup

# Initialize the file and the total size
combolist_file = open("combolist.txt", "w")
combolist_size = 0

# Continuously generate new combos and save them to the file
while True:
    # Send a GET request to the website
    response = requests.get("https://combolist.org/generate")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the combolist
        combolist = soup.find("textarea", {"id": "combolist", "spellcheck": "false"}).get_text()

        # Add the new combos to the file
        combolist_file.write(combolist)
        combolist_size += len(combolist)

        # Check if the file size has reached 2 MB
        if combolist_size >= 2 * 1024 * 1024:
            # Ask the user if they want to save the Hotmail, Outlook, Live, and GMX combos

            # Reset the file size
            combolist_size = 0
            # Close the file and reopen it
            combolist_file.close()
            combolist_file = open("combolist.txt", "w")

        # Print a message indicating that the combos have been saved
        print("Combos saved to combolist.txt")
    else:
        print("Failed to fetch data from the website")

    # Check if the user pressed Ctrl + C
    if os.path.getsize("combolist.txt") == 0:
        if os.path.exists("Account_mail_access.txt") and os.path.getsize("Account_mail_access.txt") > 0:
            break

# Close the file
combolist_file.close()