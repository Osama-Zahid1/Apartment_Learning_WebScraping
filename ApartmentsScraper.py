from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Initialize WebDriver with options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)  # Set your chromedriver path
url = "https://www.apartments.com/chicago-il/?bb=3m-u2sm-xJxzoq58H"
driver.get(url)
time.sleep(5)  # Wait for the page to fully load

# Get property links and ensure uniqueness using a set
property_links = driver.find_elements(By.CSS_SELECTOR, '.property-info a')
property_urls = list(set([link.get_attribute('href') for link in property_links]))  # Convert to set and back to list to ensure uniqueness

property_data = []

# Loop through each unique property link and scrape details
for url in property_urls:
    driver.get(url)
    time.sleep(3)  # Wait for the property page to load
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Scrape the property name
    property_name_tag = soup.find("div", class_="propertyName")
    if property_name_tag:
        # Clean up the property name to exclude unwanted parts like "media gallery unit"
        property_name = property_name_tag.get_text(strip=True)
        if "media gallery" in property_name.lower():
            property_name = property_name.replace("media gallery unit", "").strip()
    else:
        property_name = "N/A"
    
    # Initialize rent, beds, baths, and sqft with default values
    price_bed_info = soup.find("ul", class_="priceBedRangeInfo")
    
    rent = beds = baths = sqft = "N/A"
    if price_bed_info:
        # Extract rent, beds, baths, and square feet details
        price_columns = price_bed_info.find_all("li", class_="column")
        
        if len(price_columns) >= 4:
            # The first column contains rent info
            rent = price_columns[0].find("p", class_="rentInfoDetail").get_text(strip=True)
            
            # The second column contains bedrooms info
            beds = price_columns[1].find("p", class_="rentInfoDetail").get_text(strip=True)
            
            # The third column contains bathrooms info
            baths = price_columns[2].find("p", class_="rentInfoDetail").get_text(strip=True)
            
            # The fourth column contains square feet info
            sqft = price_columns[3].find("p", class_="rentInfoDetail").get_text(strip=True)
    
    # Scrape the property manager phone number
    phone_tag = soup.find("div", class_="phoneNumber")
    phone_number = phone_tag.get_text(strip=True) if phone_tag else "N/A"
    
    # Store the data in a list
    property_data.append({
        "Property Name": property_name,
        "Rent": rent,
        "Beds": beds,
        "Baths": baths,
        "Square Feet": sqft,
        "Phone Number": phone_number
    })

# Create a Pandas DataFrame and save it to an Excel file
df = pd.DataFrame(property_data)
df.to_excel('property_data_unique.xlsx', index=False)

# Close the WebDriver
driver.quit()

print("Data scraped and saved to property_data_unique.xlsx")
