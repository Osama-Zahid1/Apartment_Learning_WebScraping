### **README: Web Scraping Apartment Details**


### **Purpose**
This project demonstrates web scraping with **Selenium** and **BeautifulSoup** to extract apartment data (e.g., rent, beds, baths, and contact details) from [apartments.com](https://www.apartments.com). It is created solely for **learning purposes** and as a **portfolio project**.

### **Disclaimer**
1. **For Educational Use Only**: This script is for learning and not for commercial purposes.  
2. **Respect Website Policies**: Check and adhere to website Terms of Service before scraping.  
3. **Ethical Use**: Avoid overloading the server by adding delays or limiting requests.

### **What the Code Does**
1. **Imports Tools**: Uses Selenium for automation, BeautifulSoup for parsing HTML, and Pandas to save data.
2. **Navigates to the Website**: Opens the Apartments.com page for Chicago and extracts unique property links.
3. **Scrapes Data**: Retrieves details such as:
   - Property Name
   - Rent, Beds, Baths, Square Feet
   - Contact Phone Number
4. **Saves Data**: Stores extracted data in an Excel file (`property_data.xlsx`).

### **How to Run**
1. Install required libraries: `selenium`, `beautifulsoup4`, and `pandas`.  
   ```bash
   pip install selenium beautifulsoup4 pandas
   ```
2. Install **ChromeDriver** and configure its path.
3. Run the script in Python:  
   ```bash
   python script_name.py
   ```
4. The data will be saved in `property_data.xlsx`.

### **Learning Goals**
- Automating browser tasks with Selenium.
- Extracting structured data using BeautifulSoup.
- Respecting ethical web scraping practices.

