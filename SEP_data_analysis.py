#Description!
from SEP_dates import *

from statistics import mean, median, mode, stdev

from numpy import quantile


UrlFile = 'SEP_URLs.txt'
outFile = 'SEP_data_summary.txt'
outFile2 = 'SEP_data_full.txt'

#outFile is a CSV (seperated with ;)
#Structure of outFile: link;year count; mean; median; mode; mode frequency;
#SD; 1st Quartile; 3rd Quartile; Min; Max; filter min; filter max

#get URL list
#URLlist = []
#with open(UrlFile, 'r') as f:
#    line = f.readline()
#    while line != '':
#        line = line.replace('\n', '')
#        URLlist.append(line)
#        line = f.readline()

#for testing new code:
URLlist = ['https://plato.stanford.edu/entries/delmedigo/']

counter = 1
for URL in URLlist:
    print('EXTRACTING #', counter, ' : ', URL)
    counter += 1

    #get the data
    yearList, title = extractYears(URL)
    yearList.sort()

    ##all the stats
    #Number of different "years" references
    count = len(yearList)
    #Mean
    MEAN = round(mean(yearList))
    #Median
    MED = round(median(yearList))
    #Mode
    try:
        MODE = mode(yearList)
    except:
        MODE = 'XXXX' #no unique mode
    #Mode frequency
    if MODE != 'XXXX':
        modeF = yearList.count(MODE)
    else:
        modeF = 'XXXX'
    #Standard Deviation
    try:
        SD = round(stdev(yearList))
    except:
        SD = 'XX' #single data point
    #1st Quartile
    QT1 = int(round(quantile(yearList, .25)))
    #3rd Quartile
    QT3 = int(round(quantile(yearList, .75)))
    #Inter quartile range
    IQR = QT3 - QT1
    #Min
    MIN = yearList[0]
    #Max
    MAX = yearList[-1]

    #prepare out text (summary)
    outText = URL + ';' + title + ';' + str(count) + ';' + str(MEAN) + ';'
    outText += str(MED) + ';' + str(MODE) + ';' + str(modeF) + ';'
    outText += str(SD) + ';' + str(QT1) + ';' + str(QT3) + ';' + str(IQR) + ';'
    outText += str(MIN) + ';' + str(MAX) + ';' + str(year1) + ';' + str(year2)
    with open(outFile, 'a') as f2:
        f2.write(outText)
        f2.write('\n')

    #out text (raw data)
    outText2 = URL + ';' + str(yearList)
    with open(outFile2, 'a') as f2:
        f2.write(outText2)
        f2.write('\n')
