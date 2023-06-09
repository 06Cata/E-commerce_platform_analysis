from selenium import webdriver
from selenium.webdriver.edge.options import Options

# Set Edge options
edge_options = Options()
edge_options.add_argument("--headless")  # Optional: Run in headless mode

# Set path to msedgedriver.exe executable
webdriver_path = r'C:\path\to\msedgedriver.exe'  # Replace with the actual path to msedgedriver.exe

# Initialize Edge WebDriver
driver = webdriver.Edge(executable_path=webdriver_path, options=edge_options)

# Example: Open YouTube and search for a keyword
keyword = input("Enter the keyword to search on YouTube: ")
search_url = f"https://www.youtube.com/results?search_query={keyword}"
driver.get(search_url)

# Further processing of the search results
# Extract information, click on videos, retrieve comments, etc.

# Remember to close the driver after you're done
driver.quit()
