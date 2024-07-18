import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options (optional)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome (without GUI)

# Initialize the WebDriver (ChromeDriver in this case)
driver = webdriver.Chrome()

def findEle(ele):
    return driver.find_element(By.XPATH, ele)

def get_fraternity_info(url):
    driver.get(url)
    

    # Create a dictionary to store the fraternity info
    fraternity_info = {}
    time.sleep(2)
    try:
        #get all xpaths to each variable 
        ratings = findEle('//*[@id="main-container"]/div/div[3]/div[1]/div[2]/div[3]/ul/li[1]/span').text
        overall_average = findEle('//*[@id="main-container"]/div/div[3]/div[1]/div[2]/div[3]/ul/li[2]/span/span').text
        reputation = findEle('//*[@id="main-container"]/div/div[3]/div[1]/div[2]/div[4]/div[2]/div/ul/li[1]/span[2]/span').text
        friendliness = findEle('//*[@id="main-container"]/div/div[3]/div[1]/div[2]/div[4]/div[2]/div/ul/li[2]/span[2]/span').text
        popularity = findEle('//*[@id="main-container"]/div/div[3]/div[1]/div[2]/div[4]/div[2]/div/ul/li[3]/span[2]/span').text
        classiness = findEle('//*[@id="main-container"]/div/div[3]/div[1]/div[2]/div[4]/div[2]/div/ul/li[4]/span[2]/span').text
        involvment = findEle('//*[@id="main-container"]/div/div[3]/div[1]/div[2]/div[4]/div[2]/div/ul/li[5]/span[2]/span').text
        social_life = findEle('//*[@id="main-container"]/div/div[3]/div[1]/div[2]/div[4]/div[2]/div/ul/li[6]/span[2]/span').text
        brotherhood = findEle('//*[@id="main-container"]/div/div[3]/div[1]/div[2]/div[4]/div[2]/div/ul/li[7]/span[2]/span').text
        
        
        fraternity_info = {
            "ratings": ratings, 
            "overall_average": overall_average, 
            "reputation":reputation, 
            "friendliness": friendliness, 
            "popularity": popularity, 
            "classiness": classiness,
            "involvment": involvment,
            "social_life": social_life,
            "brotherhood": brotherhood
            
            }
    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")

    return fraternity_info

def scrape_fraternities(urls):
    all_fraternities_info = {}

    for url in urls:
        info = get_fraternity_info(url)
        all_fraternities_info[url] = info

    return all_fraternities_info

# List of URLs to scrape
urls = [
    'https://www.greekrank.com/uni/490/fraternity/AGS-Alpha-Gamma-Sigma/36/rating/',
    'https://www.greekrank.com/uni/490/fraternity/KA-Kappa-Alpha/58/rating/',
    'https://www.greekrank.com/uni/490/fraternity/KS-Kappa-Sig/65/rating/',
    'https://www.greekrank.com/uni/490/fraternity/Phi-Deltas-Phi-Delts/73/rating/',
    'https://www.greekrank.com/uni/490/fraternity/FIJI/74/rating/',
    'https://www.greekrank.com/uni/490/fraternity/Pikes-Pikas/84/rating/',
    'https://www.greekrank.com/uni/490/fraternity/Pi-Kapp-Pi-Kappa-Phi/85/rating/',
    'https://www.greekrank.com/uni/490/fraternity/SAE-Sigma-Alpha-Epsilon/88/rating/',
    'https://www.greekrank.com/uni/490/fraternity/Sig-Chi-Sigma-Chis/90/rating/',
    'https://www.greekrank.com/uni/490/fraternity/SigEp/94/rating/',
    'https://www.greekrank.com/uni/490/fraternity/Teke-TKE/100/rating/',
    'https://www.greekrank.com/uni/490/sorority/ADPi-Alpha-Delta-Pi/108/rating/',
    'https://www.greekrank.com/uni/490/sorority/DG-Delta-Gamma/118/rating/',
    'https://www.greekrank.com/uni/490/sorority/DPhiE-Delta-Phi-Epsilon/119/rating/',
    'https://www.greekrank.com/uni/490/sorority/KD-Kappa-Delta/123/rating/',
    'https://www.greekrank.com/uni/490/sorority/ophia/230/rating/',
    'https://www.greekrank.com/uni/490/sorority/PM-Phi-Mu/125/rating/'
]

# Scrape information from each URL
fraternities_info = scrape_fraternities(urls)

# Write the dictionary to a JSON file
with open('greek_info.json', 'w') as json_file:
    json.dump(fraternities_info, json_file, indent=4)

# Close the WebDriver
driver.quit()


#TODO Change this to using bs4 for less overhead and time consumption
#TODO create clean function to append the names of frats or soros instead of url