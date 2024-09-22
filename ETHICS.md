# Ethical Considerations

## Purpose of Data Collection
The purpose of this data collection is to gather publicly available information about freelance photographers and their contact details, as well as sunrise and sunset times for specific locations. This data will help me apply cleaning data techniques, web scraping techniques, and analyze photographer information in a structured format.

## Why We Are Collecting This Data
We are collecting this data to:
- **Learn**: Understand and practice web scraping techniques.
- **Analyze**: Examine the availability of freelance photographers in relation to sunrise and sunset times, aiding in the planning of golden hour photography sessions.
- **Demonstrate**: Showcase practical applications of data collection and processing.

## Data Sources and robots.txt
- **Data Source**: The data is collected from https://onmessage.nd.edu/photo-and-video/freelance-photography/, which provides a directory of photographers.
- **Compliance**: The robots.txt file does allow scraping of the photography directory pages. We have verified compliance by reviewing the robots.txt file located at https://onmessage.nd.edu/robots.txt.

## Collection Practices
- **Limit Scraping**: We limit our scraping to avoid disrupting the website’s normal operations. This is achieved by implementing rate limiting.
- **Password Protection**: We do not attempt to bypass any password protection or access restricted areas of the site.

## Data Handling and Privacy
- **No PII Collection**: We do not collect personally identifiable information (PII). The data collected includes public information such as names, contact information, and general photography availability.
- **Secure Storage**: Currently, the script does not store any data. The data is only printed to the console.
- **If Data Storage Is Implemented**: Should data storage be introduced in the future, sensitive files should be added to .gitignore to prevent accidental exposure.

## Data Usage
- **Educational and Research Purposes**: The data collected is used solely for educational and research purposes. It is intended to demonstrate data set and web scraping techniques and analyze public information in a structured way.

