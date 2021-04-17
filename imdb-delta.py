from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

data = []

chrome_options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'images': 2, 'javascript': 2,
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
                                                    'durable_storage': 2}}

chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument("start-minimized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(r"C:/Users/eledah/PycharmProjects/jumpy-ext/chromedriver.exe", chrome_options=chrome_options)

startLinks = [
    "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&view=simple&count=250",
    "https://www.imdb.com/search/title/?groups=top_1000&view=simple&sort=user_rating,desc&count=250&start=251",
    "https://www.imdb.com/search/title/?groups=top_1000&view=simple&sort=user_rating,desc&count=250&start=501",
    "https://www.imdb.com/search/title/?groups=top_1000&view=simple&sort=user_rating,desc&count=250&start=751",
]
movieLinks = []
score = []
scoreDist = []
ratingDist = []
rantingDistCount = []
tags = ""
movieNum = 0

# All Brands Page
for link in startLinks:
    driver.get(link)
    print("Crawling Brands Page Link:", link)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    # Brand Page
    for nextMovieSpan in soup.findAll('span', attrs={'class': 'lister-item-header'}):
        nextMovieLink = ("https://www.imdb.com" + nextMovieSpan.find('a')['href']).replace("?ref_=adv_li_tt", "")
        movieLinks.append(nextMovieLink)

print(movieLinks)

for link in movieLinks:
    data.append([])
    link = link + "ratings"
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    data[movieNum].append(soup.find('a', attrs={'itemprop': 'url'}).text)

    scoreSpan = soup.find('span', attrs={'class': 'ipl-rating-star__rating'})
    # score.append(scoreSpan.text)
    data[movieNum].append(scoreSpan.text)

    scoreTable = soup.find('table', attrs={'cellpadding': '0'})
    scoreDivs = scoreTable.findAll('div', attrs={'class': 'leftAligned'})
    scores = []
    for scoreDiv in scoreDivs:
        data[movieNum].append(scoreDiv.text)
        # scores.append(scoreDiv.text)
    # scores.pop(0)  # drop the "Votes"
    # scoreDist.append(scores)

    ratingDivs = soup.findAll('div', attrs={'class': 'bigcell'})
    ratingCountDivs = soup.findAll('div', attrs={'class': 'smallcell'})

    ratings = []
    for ratingDiv in ratingDivs:
        data[movieNum].append(ratingDiv.text)
    #     ratings.append(ratingDiv.text)
    # ratingDist.append(ratings)

    ratingCounts = []
    for ratingCountDiv in ratingCountDivs:
        data[movieNum].append(ratingCountDiv.find('a').text.replace(" ", ""))
    #     ratingCounts.append(ratingCountDiv.find('a').text)
    # rantingDistCount.append(ratingCounts)

    movieNum += 1

df = pd.DataFrame(data=data)
df.to_excel("output_movie.xlsx")

