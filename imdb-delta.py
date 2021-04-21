from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

data = []
tags = ""
score = []
movieNum = 0
scoreDist = []
ratingDist = []
movieLinks = []
rantingDistCount = []

# Webdriver stats
chrome_options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'images': 2, 'javascript': 2,
            'plugins': 2, 'popups': 2, 'geolocation': 2,
            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
            'media_stream_mic': 2, 'media_stream_camera': 2,
            'protocol_handlers': 2,
            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
            'push_messaging': 2, 'ssl_cert_decisions': 2,
            'metro_switch_to_desktop': 2,
            'protected_media_identifier': 2, 'app_banner': 2,
            'site_engagement': 2,
            'durable_storage': 2
        }
}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument("start-minimized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(r"C:/Users/eledah/PycharmProjects/jumpy-ext/chromedriver.exe", chrome_options=chrome_options)

# # Go over the list and find all movie links
# startLinks = []
# for i in range(1, 1752, 250):
#     link = "https://www.imdb.com/search/title/" \
#            "?at=0&num_votes=25000,&sort=user_rating,desc&title_type=feature&count=250" + "&start=" + str(i)
#     startLinks.append(link)
#     print(link)


# for link in startLinks:
#     driver.get(link)
#     print("Crawling Link:", link)
#     content = driver.page_source
#     soup = BeautifulSoup(content, "html.parser")
#
#     for nextMovieH3 in soup.findAll('h3', attrs={'class': 'lister-item-header'}):
#         nextMovieLink = ("https://www.imdb.com" + nextMovieH3.find('a')['href']).replace("?ref_=adv_li_tt", "")
#         movieLinks.append(nextMovieLink)
#
# with open('movie_links.txt', 'w') as f:
#     for link in movieLinks:
#         f.write("%s\n" % link)
# f.close()

# Open the file with all the links instead
with open('movie_links.txt') as f:
    movieLinks = [line.rstrip() for line in f]
f.close()

# Start digging out the information
for link in movieLinks:
    data.append([])
    link = link + "ratings"
    # Opening the ratings page
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    # Movie Name
    data[movieNum].append(soup.find('a', attrs={'itemprop': 'url'}).text)

    # Movie Score
    scoreSpan = soup.find('span', attrs={'class': 'ipl-rating-star__rating'})
    data[movieNum].append(scoreSpan.text)

    # Score Table
    scoreTable = soup.find('table', attrs={'cellpadding': '0'})
    scoreDivs = scoreTable.findAll('div', attrs={'class': 'leftAligned'})
    # Score Distribution
    scores = []
    for scoreDiv in scoreDivs:
        data[movieNum].append(scoreDiv.text)

    ratingDivs = soup.findAll('div', attrs={'class': 'bigcell'})
    ratingCountDivs = soup.findAll('div', attrs={'class': 'smallcell'})

    # Gender-based Ratings
    ratings = []
    for i in range(0, len(ratingDivs)):
        # If a rating is non-existent, IMDb will replace the score with "-" and remove the rating
        ratingDiv = ratingDivs[i]
        if ratingDiv.text != '-':
            data[movieNum].append(ratingDiv.text)
            data[movieNum].append(ratingCountDivs[i].find('a').text.replace(" ", ""))
        else:
            ratingCountDivs.insert(i, 0)
            data[movieNum].append(0)
            data[movieNum].append(0)

    movieNum += 1

# Save everything to excel
df = pd.DataFrame(data=data)
df.to_excel("output_movie.xlsx")
