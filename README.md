FBI Unified Crime Data Scraper :chart_with_upwards_trend:
============

The FBI releases Unified Crime Data that shows crime stats broken down by city.
Unfortunately, it is only available as an HTML table. Even data.gov just links to the table.

This is focusing on "Offenses Known to Law Enforcement by State by City"

This is a basic scraper to create CSV files, broken down by year and state. 

Source -- [FBI: Crime in the U.S.](https://ucr.fbi.gov/crime-in-the-u.s)

From there, click on a year, then click "Crime in the U.S." and find "Table 8," which often is listed under something 
like "How many crimes came to the attention of law enforcement in my city in 20xx?"

For some reason, Hawaii is missing from 2011 through 2014.

1995 - 2004 are available in Excel files, and will be imported later.

2015 isn't available yet, as of August 8, 2016.

Everything in the output/ directory comes from running the python script

>scrape_offenses_by_state_by_city_2005-2014.py

You can run it yourself if you really want, but prolly easiest to just use what's here. :)

