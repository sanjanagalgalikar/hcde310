### Nesting

print '=== 1 ==='

# 1: dictionaries in dictionaries (challenge)
# This may helpful for part 2 (depending how you do it)
# Recall that a dictionary's value can be any type of object -- even dictionaries.
# so, we might have:
#dinosaurs = {"carnivores":{"Velociraptor":3,"Coelophysis":1,"Tyranosaurus Rex":2},"herbivores":{"Avaceratops":3,"Brachiosaurus":1,"Diplodocus":2,"Stegosaurus":1}}


# for that dictionary, we can access our count of velociraptors with the following:
# raptorcount = dinosaurs['carnivores']['Velociraptor']
# or print it:
#print "raptors: "+str(dinosaurs['carnivores']['Velociraptor'])

# the first time we saw a Carnivore, we could have created a blank dictionary for
# for its value with the following:
#dinosuars['carnivores'] = {}
# or, instead, a dictionary with keys and zero values for raptors and Tyranosaurs,
# our favorite carnivorous dinosaurs, for the value with the following:
#dinosaurs['carnivores'] = {'Velociraptor':0,'Tyranosaurus Rex':0}

dinolist = [("carnivores","Velociraptor"),("herbivores","Diplodocus"),("carnivores","Coelophysis"),("herbivores","Avaceratops"),("carnivores","Velociraptor"),("carnivores","Velociraptor"),("carnivores","Tyranosaurus Rex"),("herbivores","Avaceratops"),("carnivores","Tyranosaurus Rex"),("herbivores","Avaceratops"),("herbivores","Brachiosaurus"),("herbivores","Stegosaurus")]
dinosaurs= {}

# iterate over the tuples in dinolist (above) to build the above dictionary
# note that dinosaurlist is a list of tuples (immutable lists). You can index items 
# in it just like you would with a list.
#
# You may assume that every dinosaur is a carnivore or herbivore, but for an extra challenge
# try to do this without that assumption. 
#
# put your code here
dinosaurs['carnivores']={}
dinosaurs['herbivores']={}
for dino in dinolist:
    dinotype = str(dino[1])
    if dino[0]=='carnivores':
        if dino[1] in dinosaurs['carnivores'].keys():
            dinosaurs['carnivores'][dinotype]= dinosaurs['carnivores'][dinotype]+1
        else:
            dinosaurs['carnivores'][dinotype]= 1
    else:
        if dino[1] in dinosaurs['herbivores'].keys():
            dinosaurs['herbivores'][dinotype]= dinosaurs['herbivores'][dinotype]+1
        else:
            dinosaurs['herbivores'][dinotype]= 1
print dinosaurs

### Objects

print '=== 2 ==='

# In these exercises, you will define a class for Book. This will be roughly based
# on the book dictionary from the lecture slides on dictionaries, but by adding
# methods, we will see why objects can be much more powerful.

print '=== 2a ==='

# define a class Book, whose constructor takes and assigns
# the following parameters:
#     title (string)
#     author (string)
#     year (integer)
#     publisher (string)

# Title and Author should be *required* parameters. Year and publisher should
# not be required and their default values should be None. 
# HINT: in methods, you can create default parameters the same as with functions.

# uncomment the next line define your Book class there
class Book():
    def __init__(self,title, author, year = None, publisher = None):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
    def cite(self):
        print self.author +". (" + str(self.year) + "). " + self.title + ". " + self.publisher + "."
    
# you can uncomment the following lines to see if this works
# you can compare the output with the output in the PDF
nudge = Book(title="Nudge",author="Thaler & Sunstein")
print nudge.title
print nudge.author
print nudge.year
print nudge.publisher

nudge = Book(title="Nudge",author="Thaler & Sunstein",year=2008,publisher="Penguin")
print nudge.title
print nudge.author
print nudge.year
print nudge.publisher

print '=== 2b ==='
# Now we will add a method to print the citation. The method should be called "cite".
# It should print a string in the format: "Author. (Year). Title. Publisher."

# Note: You will have to define the method above, in your class definition.

# Then, uncomment the next line to test. This should print the citation if you
# have properly defined the Book.cite() method.
nudge.cite()


### JSON 
print '=== 3 ==='
import json

#hw4example.json
# used http://www.deanclatworthy.com/imdb/?q=movie+title+here to generate data

print "--- 3a ---"
##1. load the JSON file 'hw4example.json' and print its contents. it's a list of metadata about movies.
## after you are done, comment out the print statement (so it no longer prints)
import json
post = json.load(open('hw4example.json'))
#print post


print "--- 3b ---"
##2. print the first element of the JSON file. it's metadata about a movie.
## after you are done, comment out this exercise (so it no longer prints)
#print post[0]

print "--- 3c ---"
##3. print the keys and values in the format key: value of the first element of the json file 
#   (so the attributes of the first movie get printed).
#e.g., Title: Little Miss Sunshine
for key in post[0].keys():
    print str(key) + ": " + str(post[0][key])  

print "--- 3d ---"
##4. write a *function* to print only the title, genres, and IMDB rating, and Metascore for a movie
def movieInfo(movie):
    print "Title: " + movie['Title']
    print "Genre: " + movie['Genre']
    print "imdbRating: " + movie['imdbRating']
    print "Metascore: " + movie['Metascore']


print "--- 3e ---"
##5. use the function from (3d) to print the data for each movie
for movie in post:
    movieInfo(movie)
    


