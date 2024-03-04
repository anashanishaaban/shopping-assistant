from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Selenium setup
options = Options()
options.headless = True  # Run Chrome in headless mode (without GUI)
options.add_argument("--window-size=1920,1200")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

driver_path = '/Users/anasshaaban/chromedriver_mac64'
driver = webdriver.Chrome(options=options)


# Use Selenium to get the page's dynamic content
url = "https://www.bestbuy.com/site/searchpage.jsp?st=mouse&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"
driver.get(url)

# Wait for the dynamic content to load (adjust the sleep time as necessary)
time.sleep(5)  # Example: wait for 5 seconds; consider using more robust waiting methods

# Now that the page is loaded, get the page source
html = driver.page_source
driver.quit()  # Don't forget to close the browser

# Use BeautifulSoup to parse the page source
doc = BeautifulSoup(html, "html.parser")
product_items = doc.findall("div", class_="shop-sku-list-item")

product_names = []
for item in product_items:
    h4 = item.h4  # Access the h4 element of each item
    if h4:  # Check if the h4 element exists
        product_names.append(h4.text)  # Add the text of the h4 element to the product_names list

# Process the product names as before
if product_names:
    print("Found product names:")
    for product in product_names:
        print(product.text.strip())
else:
    print("Product names not found - check if the content is dynamically loaded or the class name has changed.")
