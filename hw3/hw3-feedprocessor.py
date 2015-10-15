
### you will need this function later in the homework
def stripWordPunctuation(word):
    return word.strip(".,()<>\"\\'~?!;*:[]-+")


print "== part 3 =="
### part 3: fieldType() function
# In hw3feed.txt, note that there are both posts and comments in this feed. There are also posters.
# These lines each start with post:, comment:, and from: respectively.
# You are probably thinking "wow, it would be really helpful if we had a function to tell the type of line wit
# which I am working." The good news is that now you will write one. Find the part 3 line in hw3-feedprocessor.py
# We have included some starter code to define a function fieldType(). This function should take a line as
# parameter and return the field type (either post, comment, or from).

def fieldType(line):
    # fill in your code here
    store = line.split() #multiple worlds
    store = stripWordPunctuation(str(store[0]))#first word without punctuation
    store = store.lower()
    return store
# You can uncomment and test your function with these lines
print fieldType("from: Sean")
print fieldType("post: Hi everyone")
print fieldType("comment: Thanks!")

print "== part 4 =="
### part 4: printing users

# Your job is to extract the names and print them out, exactly as it is shown in
# the screenshot in the PDF file. Hint: if you want to remove "from:"  you can
# use string slicing operations or the replace method.
# You may use the fieldType() function but you do not have to. You may also define
# another function, such as fieldContents() to help you but that optional. 
# Duplicate names are expected for this part!

fname = "hw3feed.txt"
f = open(fname,'r')
#fill in code here
fstring = f.read()
file = fstring.split('\n')
for line in file:
    parts = line.split(' ')
    first = stripWordPunctuation(parts[0]).lower()
    if first == 'from':
        print line[6:]


print "== part 5 =="
### part 5: counting poster contribution frequency
# see the instructions in the PDF file. They are easier to follow with
# formatting

post_count = {}
f = open(fname,'r')

# read in and count the number of posts per user
# note that this should not include comments

#fill in code here
fstring = f.read()
file = fstring.split('\n')
for line in file:
    parts = line.split(' ')
    first = stripWordPunctuation(parts[0]).lower()
    if first == 'from':
        name = line[6:]
        if name in post_count:
            post_count[name]= post_count[name]+1
        else:
            post_count[name]=1

# print the number of times each user posted

#fill in code here
for key in post_count.keys():
    print key + ': ' + str(post_count[key])

print "== part 6 =="
### part 6: counting word frequency
# This is similar to post count in part 6 and you might
# even re-use some of your code. Count the number of
# times each word appears in all posts, but *not* comments

# use the stripWordPunctuation() function to get rid of punctuation.
# note that it is not perfect so some extra punctuation may remain.

post_word_count = {}
f = open(fname,'r')

# read in and count of times each word appeared

#fill in code here
fstring = f.read()
file = fstring.split('\n')
for line in file: 
    parts = line.split(' ') #all words with punctuation
    first = stripWordPunctuation(parts[0]).lower()
    parts = parts[1:] #now working w/ stuff after post type
    if first == 'post':
        for word in parts:
            word = stripWordPunctuation(word).lower()
            if word in post_word_count.keys():
                post_word_count[word]= post_word_count[word]+1
            else:
                post_word_count[word] = 1
        

# print the number of times each word appeared
#fill in code here
for key in post_word_count:
    print key + ': ' + str(post_word_count[key])

print "== part 7 =="
### part 7: counting word frequency in comments and posts
# for this part, write a function, wordFreq() that will return
# the word frequency in either posts or comments as a dictionary

# As parameters, it must take a file name and the field type
# (either post or comment) as a parameter

# for example, if I want to get a dictionary of word counts in
# the posts in hw3feed.txt, I should be able to call:
# wordFreq('hw3feed.txt','post')

# you can use your code from part 6 as a starting point, or
# if you wrote part 6 using a function, you may simply edit it
# to meet the requirements for this part.

# uncomment and begin editing from the next line:
def wordFreq(file, posttype):
    f = open(file, 'r')
    fstring = f.read()
    file = fstring.split('\n')
    dictToReturn = {}
    for line in file:
        parts = line.split(' ')
        first = stripWordPunctuation(parts[0]).lower()
        parts = parts[1:]
        if first== posttype:
            for word in parts:
                word = stripWordPunctuation(word).lower()
                if word in dictToReturn.keys():
                    dictToReturn[word]= dictToReturn[word]+1
                else: 
                    dictToReturn[word]=1
    return dictToReturn
        
        

# to test ,you can uncomment and run these  lines:
if wordFreq(fname,'post')["anyone"] == 4 and wordFreq(fname,'post')["eclipse"] == 11:
   print "Looks like wordFreq() works fine for posts"
else:
    print "We got some errors with wordFreq() for posts."
  
if wordFreq(fname,'comment')["file"] == 7 and wordFreq(fname,'comment')["if"] == 23:
    print "Looks like wordFreq() works fine for comments"
else:
    print "We got some errors with wordFreq() for comments."

