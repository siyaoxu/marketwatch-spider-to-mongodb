This program is a scrapy spider extracting headlines, timestamp, and url to full news from the 'Latest News' scrolling tab of marketwatch.com
at http://www.marketwatch.com/newsviewer.

1. Documents
requirements.txt: stores the python environment.
001-scraping-marketwatch-latestnews-to-MongoDB.ipynb is a brief document of the program.
a third document will be added to explore scraped data in the MongoDB database.

2. What's Next?
The current web crawler only extract 80 news headlines a time, which is the page limit of the infinite scrolling 'Latest News' tab. The next version will be able to handle this.
