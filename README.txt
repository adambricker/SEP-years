##Project Overview:
My aim here was to write some quick code, which does its best to pull out every
reference to a year in Stanford Encyclopedia of Philosophy (SEP) entries
(https://plato.stanford.edu/index.html). In addition to the raw data this code
scraped, this project also contains some basic descriptive stats on this data,
along with code to visualize the data using raster plots and histograms.

#Creator: Adam Michael Bricker
#Date: 13 December 2020


##Project Contents

#Python Files

SEP_dates.py
This is the code for vizualizing the year distibution over some specified list
of SEP pages.

SEP_data_analysis.py
This is the code for extracting complete year data from every SEP page and doing
some basic descriptive stats on them. NOTE: This uses the extractYears function
from SEP_dates.py, so the temporal filter set there will also be applied here.

SEP_get_URLs.py
This is the code I used to get a list of the links to every SEP article.
Since that list is included here, you probably won't need this code.


#Txt, csv, and other data files

SEP_data_full.txt
This contains the full year data extracted from every SEP page. It is
structured: link;[year1, year2, year3, . . . ]

SEP_data_summary.txt
This contains summary statistics for the year data extract from every SEP page.
It is structured: page link; page title;year count;mean;median;mode; mode frequency;
standard deviation;1st Quartile;3rd Quartile;IQR;minimum value;maximum value;
filter min;filter max
NOTE: No unique mode --> XXXX

SEP_data_summary.csv
Same data summary as above, but a csv file.
NOTE: it still uses a ; delimiter!

SEP_data_summary
Same data summary as above, but as a Microsoft Excel file.

SEP_URLs.txt
This is a list of a link to every SEP page (all 1704 of them).

SEP_URLs_by_median.txt
Exactly what it sounds like. I sorted the links by median (ascending) to use
for the plot of every data point.


##Method/Limitations
This code functions by searching through whatever SEP pages you specify for
4-digit numbers. It of course cannot tell the difference between years and
other 4-digit numbers (e.g. page 1902), so it doesn't provide perfectly clean
data. However, there are a two basic features in the code to try to limit false
positives: (1) It only counts 4-digit numbers that are preceded by (, [, a space,
or a line feed. (2) You can specify a temporal filter to exclude any numbers
outside of a target range. As this of course isn't a perfect solution, it is
important to keep in mind that the "years" it presents aren't perfectly accurate,
although they do appear to be pretty close in most instances.
