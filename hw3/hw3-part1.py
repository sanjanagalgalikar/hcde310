### part 1: exercises
pet_count = {'dog': 3, 'cat': 2, 'rabbit': 7, 'fish': 5}

print "== 1 =="
# 1: accessing values at a specified key in a dictionary.

# Write code to print the number of rabbits in the pet store (the value
# associated with key 'rabbit' in the dictionary pet_count). Hint: this is just
# one simple line of code.
print pet_count['rabbit']

print "== 2 =="
# 2: incrementing the value of a dictionary at a key.

# Write code to increment the number of rabbits in the store by one (add 1 to the
# existing value of pet_count at key 'rabbit').  Then, print out the number of rabbits
# in the store.
pet_count['rabbit']= pet_count['rabbit']+1
print pet_count['rabbit']

print "== 3 =="
# 3: adding an entry to a dictionary. 

# Our HCDE 310 pet store just got in a shipment of gerbils. 
# Write code to insert a new key, 'gerbil' into the dictionary, with a value of 6.
# Verify that it worked by printing out the value associated with the key 'gerbil'
animal = 'gerbil'
pet_count[animal]=6
print pet_count['gerbil']

print "== 4 =="
# 4: concatenating strings and integers. 

# Write code that creates a string that says 'There are X cats.', where X is the
# number of cats extracted from the pet_count dictionary.  Print the string.
# Hint: you will need to use the + string concatenation operator in conjunction
# with str() or another string formatting instruction.
say = 'There are ' + str(pet_count['cat']) + ' cats.'
print say

print "== 5 =="
# 5: iterating over keys in a dictionary.  

# Write code that prints each kind of pet (key), one line at a time using a for
# loop.
for key in pet_count:
    print key

print "== 6 =="
# 6: iterating over keys to access values in a dictionary. 

# Write code that prints each kind of pet (key), followed by a colon and the
# number of pets (e.g., cat: 2), one line at a time using a for loop.
for key in pet_count:
    print key + ": " + str(pet_count[key])

print "== 7 =="
# 7: testing membership in a dictionary.

# Write code to test whether 'gerbil' is in the pet_count dictionary.  If the test
# yields true, print "there are <x> gerbil", where <x> is the current number of
# gerbils in the household.  Do the same thing for the key 'chinchilla'.
if 'gerbil' in pet_count.keys():
    print 'there are ' + str(pet_count['gerbil']) + ' gerbil'
if 'chinchilla' in pet_count.keys():
    print 'there are ' + str(pet_count.get('chinchilla', 0)) + ' chinchilla'
else:
    print 'there are no chinchilla'

print "== 8 =="
# 8: default values

# this code asks about whether the list we have any of the potential pets (in
# the list potential pets) in our dictionary. but the code has errors.
# change the line below ##change the next line so that it prints 0 when we 
# have no animals of that type (i.e., that animal is not a key in our dictionary)
# rather than generating an error. 

# you can do this in one line or more lines. If you use more than one line,
# that is okay.

potentialpets = ['cat','mouse','pig','velociraptor','frog','fish','hamster','gerbil']
for animal in potentialpets:
    ## change the next line
    if animal in pet_count.keys():
        print animal+": "+str(pet_count[animal])
    else:
        print animal + ': 0'
    
print '=== 9 ==='
# 9: printing comma separated data from a dictionary.
# You may have worked with comma separated values before: they are basically 
# spreadsheets or tables represented as plain text files, with each row
# represented on a new line and each cell divided by a comma.
#
# Print out the keys and values of the dictionary stored in variable d. The keys
# and values you print should be separated only by commas (there should be no
# spaces). Print each key,value pair on a different line. Your output should
# match the screenshot in the PDF document, although the order of the keys may
# differ.
d = {'a':1, 'b':2, 'c':3, 'd':4}
# put your code here
for key in d:
    print str(key) + "," + str(d[key])


print '=== 10 ==='
# 10: saving a dictionary to a CSV file
# Write key and value pairs from d out to a file named 'exercise.csv'. (hint: the
# procedure is very close to that of (9), but you will need to make a small
# modification to the string you are writing out to the file, to add linebreaks)
# put your code here
f = open('exercise.csv', 'w')
for key in d:
    f.write(str(key) + ',' + str(d[key]))
    f.write('\n')
f.close()
