#This is a simple code that outputs a visualization of the distributions of
#years included in SEP articles. What you make of these distributions is up
#to you, but they're certainly fun to look at.

#NOTE: This code of course can't tell the difference between 4-digit numbers
#that are and aren't years. I've included basic precautions to exclude numbers
#that mostly likely aren't years, but it will still include (e.g.) a reference
#to page 1940 as the year 1940. In short, this is only reliable if you can
#assume that most of the numbers within your filter correspond with years.

#Author: Adam Michael Bricker (@ERPistemology). 11.12.2020


import requests
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

#This takes a link to an SEP article and outputs a list of every "year" in it
#(it also returns the title from the page you give it)
def extractYears(link):
    #A list for all the years you find
    yearList = []

    #open the link --> get the URL text
    file = requests.get(link)
    text = file.text

    #itterate over every position in the text
    for i in range(0,len(text)):
        #the next four are numbers
        if text[i] in nums:
            if text[i+1] in nums:
                if text[i+2] in nums:
                    if text[i+3] in nums:
                        if text[i+4] not in nums: #only want 4 digit numebers
                            #limit preceding position --> filter out false alarms
                            if text[i-1] in [' ', '(', '\n', '[']:
                                year = int(text[i:i+4])
                                if year in range(year1, year2 + 1):
                                    yearList.append(year) #only years inside filter

    #get the title while you're at it
    title = titler(text)
    return yearList, title


#takes a year list and returns a frequency list
def yearToFreq(yearList):
    freqList = [] #this will be the data set you're left with
    for year in range(year1, year2 +1): #loop over all the years in range
        frequency = yearList.count(year)
        freqList.append(frequency)
    return freqList

#takes the URL text and returns the title (just a string)
def titler(text):
    for i in range(0,len(text)):
        if text[i:i+7] == '<title>':
            index = i + 8
            title = ''
            while text[index] != '(':
                title += text[index]
                index += 1
    return title

#This will be useful later
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#Temporal filtering parameters: You'll only get results between year1 and year2,
#which is good for excluding numbers that likely aren't years, but can also
#exclude genuine data if you filter too agressively.
#Also, pretty sure this only works on 4-digit years?
year1 = 1850
year2 = 2020


#the variable for the SEP pages you want to look at

##Olds
#link1 = 'https://plato.stanford.edu/entries/materialism-eliminative/'
#link2 = 'https://plato.stanford.edu/entries/content-teleological/'
#link3 = 'https://plato.stanford.edu/entries/fictionalism-modal/'
#link4 = 'https://plato.stanford.edu/entries/logic-infinitary/'

##Phil Hist
#link1 = 'https://plato.stanford.edu/entries/history/'
#link2 = 'https://plato.stanford.edu/entries/hermeneutics/'
#link3 = 'https://plato.stanford.edu/entries/critical-theory/'
#link4 = 'https://plato.stanford.edu/entries/postmodernism/'

##News
#link1 = 'https://plato.stanford.edu/entries/ethics-ai/'
#link2 = 'https://plato.stanford.edu/entries/disagreement/'
#link3 = 'https://plato.stanford.edu/entries/fundamentality/'
#link4 = 'https://plato.stanford.edu/entries/science-big-data/'

##Epistemology1
#link1 = 'https://plato.stanford.edu/entries/epistemology/'
#link2 = 'https://plato.stanford.edu/entries/knowledge-analysis/'
#link3 = 'https://plato.stanford.edu/entries/epistemology-naturalized/'
#link4 = 'https://plato.stanford.edu/entries/experimental-philosophy/'

##Epistemology 2
#link1 = 'https://plato.stanford.edu/entries/knowledge-value/'
#link2 = 'https://plato.stanford.edu/entries/religion-epistemology/'
#link3 = 'https://plato.stanford.edu/entries/epistemology-social/'
#link4 = 'https://plato.stanford.edu/entries/formal-epistemology/'

##Epistemology3
#link1 = 'https://plato.stanford.edu/entries/reliabilism/'
#link2 = 'https://plato.stanford.edu/entries/contextualism-epistemology/'
#link3 = 'https://plato.stanford.edu/entries/epistemology-virtue/'
#link4 = 'https://plato.stanford.edu/entries/justep-intext/'

##Consciousness
link1 = 'https://plato.stanford.edu/entries/consciousness/'
link2 = 'https://plato.stanford.edu/entries/consciousness-animal/'
link3 = 'https://plato.stanford.edu/entries/consciousness-higher/'
link4 = 'https://plato.stanford.edu/entries/consciousness-neuroscience/'

#To specify individual links and scrape the data from SEP
links = [link1, link2, link3, link4]


#titles for graphs later
#titles = titler(links)

if __name__ == "__main__":

    #######################
    ##EXTRACTING THE DATA##
    #######################

    ##To run it off of a list of the URLs + data you already scraped
    #Note: I only used this when vizualizing the data from every page.

    #with open('SEP_URLs_by_median.txt', 'r') as f: #all of them
    #    links = []
    #    link = f.readline()
    #    while link != '':
    #        link = link.replace('\n', '')
    #        links.append(link)
    #        link = f.readline()

    #with open('SEP_data_full.txt', 'r') as f: #the data file
    #    dataDic = {} #it's gonna be a dictionary
    #    line = f.readline()
    #    while line != '':
    #        line = line.replace('\n', '')
    #        link = line.split(';')[0]
    #        data = [int(i) for i in line.split(';')[1].replace('[', '').replace(']', '').split(',') if int(i) in range(year1, year2 + 1)]

    #        dataDic[link] = data


    #        line = f.readline()


    #yearListList = [dataDic[i] for i in links]
    #freqListList = [yearToFreq(yearList) for yearList in yearListList]


    ##Running it the normal way, directly scraping SEP with the links from above

    #the list of lists of years, one for each SEP article
    yearListList = []

    #the list of lists of year frequences, one for each SEP article
    freqListList = []

    #same idea but titles
    titles = []

    counter = 1
    for link in links:
        print('Extracting #', counter, ': ', link)
        counter += 1
        tempYearList, title = extractYears(link)
        yearListList.append(tempYearList)
        titles.append(title)
        tempFreqList = yearToFreq(tempYearList)
        freqListList.append(tempFreqList)



    #################
    ##VIZUALIZATION##
    #################


    dta = np.array(freqListList)


    ##raster diagram (fixed scales)

    #just for the everything plot
    #plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True


    #make the plot (use 8x30 for the everything plot)
    fig, ax = plt.subplots(constrained_layout=True, figsize = (8,3))



    ax.set_xlabel('Year')

    #make nicer ticks
    x, y = np.meshgrid(np.arange(dta.shape[1] + 1), np.arange(dta.shape[0] + 1))
    xx = x + year1 #rescale to number of pages
    yy = y - .5 #shift up half so graph looks nicer

    #plot using linear color scaling
    im = ax.pcolormesh(xx, yy, dta)

    #plot using log color scaling
    #im = ax.pcolormesh(xx, yy, dta, norm=colors.LogNorm(vmin=1, vmax=dta.max()))

    #yticks to labels
    ax.set_yticks(np.arange(len(titles)))
    ax.set_yticklabels(titles)
    #ax.yaxis.set_visible(False)


    fig.colorbar(im, ax = ax, shrink = .6, label = "Occurrances/year")

    #fig.colorbar(im, ax = ax, shrink = .4, label = "Occurrances/year", location='top')

    #ax.set_title('Years Referenced in Every SEP Article (vertical axis)', fontsize=20, pad = 40)

    #fig.savefig('everything6.png')

    plt.show()


    #need to end things here if you're using the data for every page at once
    #quit()

    ##histograms
    fig, ax = plt.subplots(len(links), 1, constrained_layout=True, figsize = (8,6))

    for i in range(0,len(links)):
        im = ax[i].hist(yearListList[i], bins = 50)
        ax[i].set_title(titles[i])

    plt.show()

    #v2 raster (multiple scales)
    fig, ax = plt.subplots(len(links), 1, constrained_layout=True, figsize = (8,6))
    for i in range(0,len(links)):
        #make nicer ticks
        dta = np.array([freqListList[i]]) #data for just one link = [one year list]
        x, y = np.meshgrid(np.arange(dta.shape[1] + 1), np.arange(dta.shape[0] + 1))
        xx = x + year1 #rescale to number of pages
        yy = y - .5 #shift up half so graph looks nicer

        im = ax[i].pcolormesh(xx, yy, dta)
        fig.colorbar(im, ax = ax[i], shrink = 1.2, label = "Occurrances/year")
        ax[i].set_title(titles[i])
        ax[i].yaxis.set_visible(False)

    plt.show()
