import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    logging.info("Setting up Chrome driver")
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    # Set up preferences
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2, 'javascript': 2, 'plugins': 2, 'popups': 2, 'geolocation': 2,
            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
            'durable_storage': 2
        }
    }
    chrome_options.add_experimental_option('prefs', prefs)

    # Set up the driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def read_movie_data(filename):
    logging.info(f"Reading movie data from {filename}")
    movies = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movies.append((row['Movie Name'], row['Movie Link']))
        logging.info(f"Successfully read {len(movies)} movies from the CSV file")
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        raise
    return movies

def scrape_movie_data(driver, movies):
    logging.info("Starting to scrape movie data")
    data = []
    for index, (movie_name, link) in enumerate(movies):
        logging.info(f"Scraping movie {index + 1}/{len(movies)}: {movie_name}")
        movie_data = [movie_name]  # Start with the movie name from our CSV
        ratings_link = link + "ratings"
        
        try:
            driver.get(ratings_link)
            content = driver.page_source
            soup = BeautifulSoup(content, "html.parser")
            
            # Movie Score
            score_span = soup.find('span', attrs={'class': 'ipl-rating-star__rating'})
            movie_data.append(score_span.text if score_span else "N/A")
            
            # Score Distribution
            score_table = soup.find('table', attrs={'cellpadding': '0'})
            if score_table:
                score_divs = score_table.findAll('div', attrs={'class': 'leftAligned'})
                for score_div in score_divs:
                    movie_data.append(score_div.text)
            
            # Gender-based Ratings
            rating_divs = soup.findAll('div', attrs={'class': 'bigcell'})
            rating_count_divs = soup.findAll('div', attrs={'class': 'smallcell'})
            for i in range(len(rating_divs)):
                rating = rating_divs[i].text
                if rating != '-':
                    movie_data.append(rating)
                    movie_data.append(rating_count_divs[i].find('a').text.replace(" ", ""))
                else:
                    movie_data.extend(["0", "0"])
            
            data.append(movie_data)
        except Exception as e:
            logging.error(f"Error scraping {movie_name}: {e}")
            data.append([movie_name, "Error"] + ["N/A"] * 20)  # Placeholder for error cases
    
    return data

def main():
    driver = setup_driver()
    
    # Read movie data
    movies = read_movie_data('movie_data.csv')
    
    # Scrape data
    data = scrape_movie_data(driver, movies)
    
    # Save to Excel
    logging.info("Saving data to Excel")
    df = pd.DataFrame(data=data)
    df.to_excel("output_movie.xlsx", index=False)
    
    logging.info("Scraping completed. Data saved to output_movie.xlsx")
    driver.quit()

if __name__ == "__main__":
    main()