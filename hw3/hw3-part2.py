

###############################################################
## part 2: exercises

print '=== 1 ==='
# 1: function with one parameter
#### questioning_print() prints a string with a question mark (?) at the end
# input parameter:
#   s: the string to print
# define questioning_print() here.
def questioning_print(s):
    print s + '?'
# to help you understand the format of instructions for these exercises, we have
# given you a starter template below. Modify it. Note how the instructions
# mention a parameter, s, which becomes the parameter name in the function
# definition.




# uncomment the next two lines to check if you correctly defined excited_print():
questioning_print('a word')
questioning_print('nice job')

print "=== 2 ==="
# 2: returning a value
#### questioning_string() returns a string with an question mark added to the end
# input parameter:
#   s: the string to question
# returns: a string

# define questioning_string() here
def questioning_string(s):
    return s + '?'
    
# uncomment the next two lines of code to check if you correctly defined the function
print questioning_string('may I have a word')
print questioning_string('nicer job')

print "=== 3 ==="
# 3: function with two parameters that returns a value
#### chars_after() returns a substring beginning at the specified position,
#chopping off all the characters before start_position
# input parameters:
#   start_position: index of first character to include
#   s: the string to take a slice of

# define chars_after() here
def chars_after(position, s):
    return s[position:]
    
# uncomment the following two lines of code to check if you correctly defined the function
#try it with different values for X and Y
X = 5
Y = 4
print chars_after(Y, 'not fun')
print chars_after(X, 'from: Aravind Ravi')
