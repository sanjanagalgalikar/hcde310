######################################
# part 2: contributor counts

#Your next task is to extend the functionality from last week's homework
#assignment using functions.  In the last assignment, you read in the contents
#of a file, computed the poster contribution frequencies using a dictionary, and
#printed out the contents of that dictionary.

#This week, you'll write a function that computes the poster frequencies and
#returns the dictionary as a value. The dictionary will then be passed as a
#parameter to two more functions that will do something with it.

#### is_field() tests if the line represents the given kind of field
# you don't have to modify this function.
# inputs:
#   field_name: a string that specifies the kind of field
#   s: the string we are testing
# returns: True if s starts with field, False otherwise
def is_field(field_name, s):
    if s[:len(field_name)] == field_name:
        return True
    else:
        return False

#### contributor_counts() should return post and comment frequency for each user
# in the specified file
# input:
#   file_name: name of file being read
# returns: a dictionary of post and comment counts
# e.g., if we we had two posters, Alice (0 comments, 2 posts) and Bob (1 post, 2 comments), 
# our dictionary would look like
# cc = {"Alice":{"posts":2,"comments":0},"Bob":{"posts":1,"comments":2}}

# define contributor_counts() here.
# in this function, you MUST make at least one call to the function is_field
def contributor_counts(file_name):
    cc={}
    f = open(file_name, 'r')
    fstring = f.read()
    file = fstring.split('\n') #array storing each line
    
    for line in file: 
        if is_field("from", line):
            name = line[6:]
            if not name in cc.keys():
                cc[name]={"posts":0,"comments":0}
        if is_field("post", line):
            cc[name]["posts"] = cc[name]["posts"] + 1
        if is_field("comment", line):
            cc[name]["comments"] = cc[name]["comments"] + 1
    return cc
        
 

#### print_contributors() should print out the number of times each
# person posted and commented.
# The implementation should be similar to what was done in hw3 to print out
# contributor counts, but will use an if statement so that contributor counts of
# 1 will be printed as "once" and higher or zero counts will be "X times". For
# example:
#   "John Smith posted once and commented 2 times"
#   "Jane Smythe posted 4 times and commented 0 times"
#
# input parameter:
#   counts: dictionary of contributor counts

# define print_contributors() here.
def print_contributors(counts):
    for key in counts:
        name= key + " posted "
        if counts[key]["posts"]== 1:
            name += "once "
        else:
            name += str(counts[key]["posts"]) + " times "
        name += "and commented "
        if counts[key]["comments"]== 1:
            name += "once "
        else:
            name += str(counts[key]["comments"]) + " times"
        print name
#### save_contributors() should save a comma separated value (CSV) formatted
# file where the first item is the key of a dictionary and the second item is
# the value (e.g. name,postcount,commentcount).
# input parameters:
#   counts: dictionary of contributor counts
#   output_file_name: name of the file being saved to

# the first line in the file should be a header row:
# name,post_count,comment_count 

# define save_contributors() here.
def save_contributors(counts, output_file_name):
    f = open(output_file_name, 'w')
    for key in counts.keys():
        f.write(str(key) + ',' + str(counts[key]["posts"]) + ',' + str(counts[key]["comments"]))
        f.write('\n')
    f.close()

# the following code runs your functions to make sure they work properly
# uncomment all valid lines of python code to test your functions

# read in and count contributions
contributions = contributor_counts("hw4feed.txt")

#print the human readable version
print '------'
print_contributors(contributions)

# write the computer readable version
save_contributors(contributions, 'contributors.csv')


######################################
def stripWordPunctuation(word):
    return word.strip(".,()<>\"\\'~?!;*:[]-+")


######################################
# part 3: word counts

# To do this, we will write two functions. The first wordFreqs() which
# should take a file name as a parameter and generate a dictionary of
# words and their frequencies in posts and comments. 
#
# That is, the output should be a dictionary in the form:
# {'word':{'comments':3,'posts':5},'anotherword':{'comments':0,'posts':5}
# .... and so on. That is, it's another nested dictionary. 
#
# uncomment the next line and define wordFreqs() there
def wordFreqs(fname):
    f = open(fname,'r')
    fstring = f.read()#
    file = fstring.split('\n')
    wordCounts={}
    for line in file: 
        words = line.split(' ')
        words = words[1:]#get rid of "post"/"comment"
        if is_field("post", line):
            for word in words:
                word = stripWordPunctuation(word).lower()
                if not word in wordCounts.keys():
                    wordCounts[word]={'comments':0,'posts':1}
                else:
                    wordCounts[word]['posts'] = wordCounts[word]['posts']+1
        if is_field("comment", line):
            for word in words:
                word = stripWordPunctuation(word).lower() 
                if not word in wordCounts.keys():
                    wordCounts[word]={'comments':1,'posts':0}
                else:
                    wordCounts[word]['comments'] = wordCounts[word]['comments']+1
    return wordCounts




# Next, we will write your writeFreqs() function, which takes, as a parameter
# a dictionary of the format output by wordFreqs() and writes a CSV file, freqs.csv.
# The first line of your file should be:
# word,postcount,commentcount
# and subsequent lines should contain the data.
#
# You must remove stopwords (the words in stopwords.txt). You may remove
# them in either wordFreqs() or in writeFreqs(). The decision is up to you.
# 
# uncomment the next line and define writeFreqs() there.
def writeFreqs(freqdict):
    f = open('freqs.csv', 'w')
    f.write('word,postcount,commentcount')
    f.write('\n')#doesn't work
    for key in freqdict.keys():
        if not key in open('stopwords.txt').read():
            f.write(str(key) + ',' + str(freqdict[key]["posts"]) + ',' + str(freqdict[key]["comments"]))
            f.write('\n')
    f.close()


