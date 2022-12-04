# jioscrape
 
A web scraping project, which scrapes the data from JioMart website specifically the vegetables and grocery section. 

The folder structure of the project:

![folder tree](https://user-images.githubusercontent.com/46810093/205482778-eeafcfa9-53ce-4bb4-93ba-3f73aa163b73.png)

To start scraping right away type the following commands

```
# enter the directory
scrapy crawl jio -O mart.csv

# To install required dependencies
pip install -r requirements.txt 

# It will start fetching the given url and store the desired results in mart.csv file
scrapy crawl jio -O mart.csv 
```

You can view and modify the source code in /jioscrape/spiders/jiospyder.py.
