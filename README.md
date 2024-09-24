# Sunset Seekers

## Description

Sunset Seekers is a Python application that identifies sunrise and sunset times based on user-provided geographic coordinates (latitude and longitude) and a specified date. It also scrapes contact information for freelance photographers from the following site: https://onmessage.nd.edu/photo-and-video/freelance-photography/. This website was chosen due to its focus on freelance photography and the variety of photographers listed, making it an ideal resource for anyone looking to capture the perfect golden hour pictures. Together these two sources work together to help users save time when communicating to their photograpghers. By having acesses to the ideal photgraghy times (sunset/sunrise) users will be able to request these times in their inital outreach to their photograpghers without the hassel of searching for things like ideal times, contact info, ect.  

# Features
- Identifies sunrise and sunset times based on user-provided latitude, longitude, and date using the Sunrise-Sunset API.
- Scrapes contact information for freelance photographers from the University of Notre Dame's freelance photography page.
- Provides a combined dataset that includes the names, emails, phone numbers, websites, and the ideal photography times for each photographer.

## Data Gathered

1. **Sunrise and Sunset Times**:
   - Data is fetched from the Sunrise-Sunset API, which provides accurate sunrise and sunset times in UTC format. The data includes:
     - Sunrise Time
     - Sunset Time

2. **Photographer Information**:
   - The application scrapes the following details for each photographer:
     - Name
     - Email addresses
     - Phone numbers
     - Website links (if available)

## Prerequisites
To run this application, you need to have:
- Python installed on your machine.
- The following libraries, which can be installed via pip:
  - requests
  - beautifulsoup4
  - pandas
  - regex
  - time

Make sure to add these libraries to a requirements.txt file in your project.

## Value to Users

- **Convenience**: Users can quickly access both the ideal times for photography and a list of photographers who can assist them.
- **Time-Saving**: Instead of searching for photographers and calculating sunrise/sunset times individually, this tool provides all the information in one place.
- **Enhanced Creativity**: Understanding the golden hour can greatly improve the quality of photographs, as lighting is crucial in photography.

## Why is this dataset not publicly available for free already?

While sunrise and sunset data can be found individually, combining this information with local freelance photographer contacts is unique. Most platforms focus on either providing astronomical data or photographer listings, but not both in conjunction. This dataset fills that gap, making it easier for users to plan their photography sessions.

## Running the Application

To run this application, follow these steps:

1. Clone the repository:
 - git clone https://github.com/Marian-CA/SunsetSeekers.git
 - cd SunsetSeekers

2. **Install Dependencies**

    - Install the required Python libraries using pip.

    - Then, install the dependencies:

        - pip install -r requirements.txt

3. **Run the Script**

    - Execute the script using Python:

        python main.py

    - When prompted, enter your latitude, longitude, and date. The program will fetch sunrise and sunset times, scrape freelance photographer data, and save the results to a CSV file.
   
## Note
This application is designed for educational purposes and as a prototype. In a real-world application, additional features such as a user interface, robust error handling, and the ability to customize search parameters would be implemented.
