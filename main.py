import requests
from bs4 import BeautifulSoup
import pandas as pd
import time  # Import time module for sleep function

# Introductory statement
print("Looking for the perfect golden hour pictures? This program will help you identify sunrise and sunset times and produce a list of freelance photographers and their contacts so that you can get the perfect golden hour pictures wherever you are!")

# Ask for user input for location (latitude, longitude)
latitude = input("Please enter your latitude: ")
longitude = input("Please enter your longitude: ")

# Ask for the date
date_input = input("Please enter a date (YYYY-MM-DD): ")

# Fetch sunrise and sunset data from the API
api_url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"
response = requests.get(api_url)
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

# Scrape photographer data from the freelance photography page
url = 'https://onmessage.nd.edu/photo-and-video/freelance-photography/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

photographers = []

# Extract photographer information from the <li> tags
for photographer_info in soup.select('ul.no-bullet.grid.grid-md-2.grid-lg-3 li'):
    # Extract the name
    name = photographer_info.find('strong').text.strip() if photographer_info.find('strong') else "Unknown"
    
    # Extract the email addresses
    email_tags = photographer_info.find_all('a', href=True)
    emails = ', '.join([email.get('href').replace('mailto:', '').replace('%20', '').strip() for email in email_tags if 'mailto:' in email.get('href')]) or "No email"
    
    # Extract phone number from the second <br> tag, if available
    br_tags = photographer_info.find_all('br')
    phone = br_tags[1].next_sibling.strip() if len(br_tags) > 1 and br_tags[1].next_sibling else 'No phone number'
    
    # Extract the website, if available
    website = next((email.get('href') for email in email_tags if 'http' in email.get('href')), 'No website')
    
    # Split the sunrise and sunset into date and time
    sunrise_date, sunrise_time = sunrise.split('T')
    sunset_date, sunset_time = sunset.split('T')
    
    photographers.append({
        'Name': name,
        'Email': emails,
        'Phone': phone,
        'Website': website,
        'Date': date_input,  # Use the user-input date
        'Sunrise Time': sunrise_time.split('+')[0],  # Remove the timezone part
        'Sunset Time': sunset_time.split('+')[0]  # Remove the timezone part
    })
    
    # Sleep for 2 seconds to be ethical
    time.sleep(2)

# Create a DataFrame with the data
df = pd.DataFrame(photographers)

# Reorder columns (optional)
df = df[['Name', 'Email', 'Phone', 'Website', 'Date', 'Sunrise Time', 'Sunset Time']]

# Clean the DataFrame by replacing missing values
df = df.fillna("Unknown")

# Export the DataFrame to a CSV file
csv_file = 'formatted_sunrise_sunset_photographers.csv'
df.to_csv(csv_file, index=False)

print(f"Data has been saved to '{csv_file}'")



















