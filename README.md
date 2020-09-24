# Analysis of Physics Discoveries

In this project I made some data analysis and visualization on some of the most important physics discoveries in history.         
I tryed to see how physics discoveries changed over time, how they changed based on the country, the correlations between the countries and the number of discoveries, and how international collaboration has increased in the years.


### Data Scraping
```scrape_data.py``` scrapes data from the internet and saves them in a csv file called ```physics_discoveries.csv```.          
I added the "Country of Origin" column (using the information on wikipedia) because there wasn't any website that included them along with the discoveries. And some data were also formatted by hand dued to the bad form on the website scraped.


### Analysis of data
- Line chart of physics discoveries over time
- Bar Chart of physics discoveries per century
- Histogram of the locations of physics discoveries
- How the number of discoveries moved from Europe to United States over time
- How the number of discoveries made through international collaboration increased over time
- Number of physics discoveries made by groups of people with different nationalities over time


#### Requirements
```
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
```