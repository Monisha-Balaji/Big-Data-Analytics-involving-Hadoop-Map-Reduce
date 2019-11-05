#!/usr/bin/env python
"""mapper.py"""

import sys

list = ['said','the','i','one','year','he','a','case','new','state','it','people','two','would','but','officer','time','also','like','court','told','last','day','city','say','home','jayme',"official","school","she","could","judge","persico","american","man","first","month","three","charge","country","group","life","even","we","former","made","many","later","member","public","right","patterson","found","according","know","make","may","week","they","this","united","work","since","without","night","day","a","said","the","u","v","http","https","jackson","would","year","time","one","he","new","but","it","two","also","last","people","like","could","say","cardinal","many","part","united","even","first","film","former","charge","week","told","including","get","we","make","according","boy","de","la","le","in","en","et","un","you","que","and","in","i"]
common_words = set(list)

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
	if not word in common_words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        	print '%s\t%s' % (word, 1)
        
