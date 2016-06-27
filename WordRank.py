
# this script demonstrates the use of regular expressions
# it ranks the words from a source text according to their frequency of occurrence

import re
import operator
import urllib

# get text from Alice's Adventures in Wonderland
fin = urllib.urlopen('http://www.gutenberg.org/cache/epub/11/pg11.txt')

s=fin.read()

m = re.findall(r"([\w\d_]+)",s)

for i in range(len(m)):
    m[i] = m[i].lower()

aa = set(m) # extract unique elements from the list "m"

print '\nWord Count:', len(m)
print
print 'Unique Words: ',len(aa)
print

theDict={}
for i in aa:
    theDict.update({i: m.count(i)})

sortDict = sorted(theDict.items(), key=operator.itemgetter(1)) # sort by word count

# print the number of times each word appears in the text
for i in sortDict:
    print i[0], i[1]
print
