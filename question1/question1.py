# Retrieve the weather station data from the url below and print the total
# precipitation in February 2007 as reported by the data.
# https://www.wunderground.com/history/airport/KNUQ/2007/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2007&req_city=NA&req_state=NA&req_statename=NA&format=1
# Implement the solution entirely in python

# Run in ipython or bpython by 'import question1' followed by 'question1.main()'.
# Not the quickest solution, but it's easy to switch the month of interest this way in the if statement.

import requests
import numpy as np

def makedata():
	rawtext = requests.get('https://www.wunderground.com/history/airport/KNUQ/2007/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2007&req_city=NA&req_state=NA&req_statename=NA&format=1')

	Text = rawtext.text[402:]
	data = Text.encode('ascii')
	data = data.replace('<br />', '')
	data = data.replace(',', ', ')

	f = open('data.txt','w')
	f.write(data)
	f.close()
	return;

def main():
	makedata()

        g = open('data.txt', 'r')
        h = open('data.txt', 'r')
        data = h.read()

        precip = np.loadtxt(g, delimiter = ', ', usecols = (19,))
        rows = data.split('\n')

        #prepare loop
        total_precip = 0.0
        n = 0
        while rows[n] != '':
                if rows[n].startswith('2007-2'):
                        total_precip = total_precip + precip[n]
                n += 1

        print(total_precip)
        return (total_precip);
