import json

###################
### utility functions-- don't edit these; just call them as needed
### the first two should be familar from  hw5-buildingblocks.py
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

def shortname(username):
    """returns the abbreviated version of a username"""
    ss = username.split()
    return '%s %s.' % (ss[0], ss[-1][0])


def genPhotoPage(post_objects, filename):
    """generates a web page from a list of photo objects
     inputs:
       post_objects: a list of Post objects
       filename: output html file
    """
    out = open(filename, 'w')
    out.write('<html><head><title>HCDE310 Photos</title></head>\n') 
    out.write('<body>\n')

    img_template = '<a href="%s" title="%s"><img src="%s"/></a>\n'
    for post in post_objects:
        if isinstance(post, Photo):  # only write out Photo posts
            out.write(img_template % (post.photo_url, post.name, post.preview_url))

    out.write('</body></html>')
    out.close() 


###################
### Class 1: the Post class
class Post():
    """object representing status update"""
    def __init__(self, postdict):
        # self.message is the instance variable containing the post's message
        # some posts do not have messages so we set it to a blank string.
        self.message = postdict.get('message','')

        # if the post dictionary has a 'comments' key, set self.comments to the
        # corresponding comments dictionary. otherwise, set self.comments to None
        if 'comments' in postdict:
            self.comments = postdict['comments']
        else:
            self.comments = None
     
        # if the post dictionary has a 'likes' key, set self.likes to
        # the corresponding likes dictionary.  otherwise, set self.likes to None
        if 'likes' in postdict:
            self.likes = postdict['likes']
        else:
            self.likes = None

    # (a): fill in code here to initialize the name instance variable
    #      to the short name of the user in the post dictionary. 
    #      Hint: see your poster() function from hw5-buildingblocks.py
    #      then uncomment the testing line in the main block at the end of the file


    # (b): Write a method to return the comments count.
    #      Uncomment the following two lines, and also the
    #      corresponding line in the main block (below)
#    def commentCount(self):
#        """returns the number of comments"""
        # (b): fill in code here.  hint: None is a value, just like 0 or 'foo'
     
    # (c): Write a method to return the likes count.
    #      Uncomment the following two lines, and also the
    #      corresponding line in the main block (below)
#    def likeCount(self):
#        """returns the number of likes"""
        # (c): fill in code here.

    # (d): Some messages are longer than 140 characters. If so, write a
    #      method to return a short message that consists of the first
    #      140 characters of the message plus elipses, e.g.
    #      "the first 140 characters..."
    #      Uncomment the following two lines, and also the
    #      corresponding line in the main block (below)
#    def shortMessage(self):
#        """returns the shortened (<=140 character) message"""
        # (d) fill in code here.

    def __str__(self):
        """string representation of the post"""
        s = '--- status update ---------\n'
        # uncomment the following lines after you write and test (a-d) [e]
        #s += 'name: %s\n' % self.name                  # (a)
        #s += 'comments: %s\n' % self.commentCount()  # (b)
        #s += 'likes: %s\n' % self.likeCount()        # (c)
        #s += 'message: %s\n' % self.shortMessage()    # (d)
        return s

#     uncomment the following two lines
#    def hasQuestion(self):
#        """returns True if the message contains a '?'."""
#        (f) fill in code here



### Building Block 2: the Link class
class Link(Post):
    """object representing a Link post"""
    ## The init method for Link() calls the init method 
    ## from Post, but also sets an instance variable for 
    ## url.

    def __init__(self, postdict):
        Post.__init__(self, postdict)
        self.url = postdict['link']

#     uncomment the following two lines
#    def __str__(self):
#        """string representation of the Link post"""
#        fill in code here (2.a)
#        the string being returned should be similar to that of Post.__str__()
#        except it should also print out the linked url (see PDF for details)

### Building Block 3: the Photo class
class Photo(Post):
    """object representing a Photo post"""
    ## The init method for Phooto() calls the init method 
    ## from Post, but also sets instance variables for
    ## the photo URL and a preview URL.
    
    def __init__(self, postdict):
        Post.__init__(self, postdict)
        self.preview_url = postdict['picture']
        self.photo_url = postdict['link']

#    def __str__(self):
#         fill in code here. (3.a)
#         the string being returned should be similiar to that of Post.__str__()
#         except it should also print out the linked photo (see PDF for details)


### Main block
if __name__ == '__main__':  
    # this loads the facebook group data as a list of dictionaries
    postdicts = json.load(open('hw5feed.json'))['data']

    print "-- TEST 1 --"
    ### Test 1: polymorphism with  __str__() methods
    # sample Posts to print
    # this post is short (< 140 chars)
    my_post_short = Post(postdicts[72])
    # this post is long (> 140 chars)
    my_post_long = Post(postdicts[24])

    print "- elements -"
    # uncomment the following lines as you implement building block 1a-d:
    print "my_post_short poster:        %s"%my_post_short.name             # tests (1a)
    print "my_post_short comment count: %s"%my_post_short.commentCount()   # tests (1b)
    print "my_post_short like count:    %s"%my_post_short.likeCount()      # tests (1c)
    print "my_post_short message:       %s"%my_post_short.shortMessage()   # tests (1d)
    print "my_post_long  message:       %s"%my_post_long.shortMessage()    # tests (1d)
    
    # uncomment the following two lines to test (1e)
    print "- short post -"
#    print my_post_short
    print "- long post -"
#    print my_post_long
    
    ## testing building block 2
    # sample Link to print
    # uncomment the next two lines to test 2a
#    my_link = Link(postdicts[34])
#    print my_link            # tests (2a)
    
    # testing building block 3
#    my_photo = Photo(postdicts[1])
#    print my_photo                     # tests (3a)

    # convert all dictionaries to Post, Photo, and Link objects
    postobjects = []  # start off with empty list of objects
    for postdict in postdicts:
        # make a Post, Photo, or Link object from the post dictionary depending
        # on the value of the "type" key in the post dictionary
        if postdict['type']=='status':
            postobject = Post(postdict)
        elif postdict['type']=='link':
            postobject = Link(postdict)
        elif postdict['type']=='photo':
            postobject = Photo(postdict)
           
        # add the post object to the list
        postobjects.append(postobject)

    ### Test 2: Outputting Photo objects as a web page: (testing 3a,b)
#    uncomment the following line of code and verify that hcde310photos.html
#    displays thumbnail images that link back to the respective facebook photo
#    include hcde310photos.html in your Canvas upload

#    genPhotoPage(postobjects, 'hcde310photos.html')


    ### Task 1: printing questions
    print ";;;;; Task: printing questions ;;;;;;;"
    first10 = postobjects[:10]  # sample set of posts
    # fill in code here that prints just the questions and number of
    # comments received in the first 20 post objects
    # Print your output as (also see PDF):  
    #    Name received # replies to their question:
    #    short message
    # hint: use your .hasQuestion() method


    ### Task 2: counting and printing totals  (this is optional but strongly recommended for review)
    print ";;;;; Post, Comment, and Like counts per person ;;;;;;;"
    # Loop through postobjects and count the number of posts made by each person
    # and the number of comments and likes they *received*
    # You may either use a dictionary for this or create a new class for a person
    # If you create a dictionary (you are most familiar with these), you 
    # it should be in the format {Name:  {'posts':n,'comments':y,'likes':z},
    #                             Name2: {'posts':n,'comments':y,'likes':z},
    #                            ... }
    
    
    # then, write code to loop through your posters and print their totals
    # in the format:
    # Name posted n times and received y comments and z likes.
  
