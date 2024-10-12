###################
# LISTS IN PYTHON #
###################

# A list, as you might imagine, is a collection of items. Here's how you make
# an empty list:

empty_list = list()
myList = [] # Another way

# We now have two empty lists. Now it's time to start adding things to our
# lists. A handy function to do this is append(). This adds things to the end
# of a list. This function is unlike anything we've seen as of yet. It's what
# we call a METHOD

# We'll get back to this idea later. For now, just know that methods are used
# like so:

myList.append(1)

# Basically, you take the list you want to do things with, and you "attach"
# the append() method to it using the "dot operator"
# Now, myList is no longer empty. It contains an the integer 1.
print(myList) # [1]

# In Python, there are not very many restrictions on what you may add to a list.

myList.append("two") # string
myList.append(3.0)   # float
myList.append(empty_list) # another list
# You can add most things to a list

print(myList) # [1, 'two', 3.0, []]

# Given a list with items in it, we can access its contents using the
# same indexing as Strings!
# Don't forget indices start at zero!

one = myList[0] # Read as: "myList at the index zero"
print(one) # 1

# Knowing that there's an empty_list in the THIRD index of myList, I can even
# add some stuff in there

myList[3].append(4)
print(myList) # [1, 'two', 3.0, [4]]

# You can imagine that the whole ensemble "myList[3]" is another name for the
# inner list. Recall that this inner list already had a name "empty_list". What
# does it look like now?

print(empty_list) # [4]

# Sometimes, we also want to change an entry in our list altogether.
# We can also use the indices to do this.

myList[3] = 4 # Set the value at index 3 to 4
print(myList) # [1, 'two', 3.0, 4]

# Behind the scenes, lists are like a shelf in your computer's memory bank. The
# objects in a list live next to one another (kinda) and have addresses. You
# can access the data at these addresses using their index. When we wrote
# myList[3] = 4, we simply evicted the empty_list from its address, and allowed
# the integer 4 to move there.

# Of course empty_list still exists, but we can't call it according to it's
# address in myList anymore.

# This is getting a little technical, so let's take a step back. Just know I'm
# bringing this all up for a good reason. One day we will dive back into this
# and talk about pointers. Now is not the time...

# So we have two lists. What happens if we add them together?

newList = empty_list + myList # [4] + [1, "two" , 3.0, 4]
print(newList) # [4, 1, 'two', 3.0, 4]

# This added empty_list to the start of myList.
# This is exactly how string concatenation works!
# This gives us a handy way to add things at the beginning of a list.

# So we can add at the start and the end of a list. How about some arbitrary
# middle index?
# We can do this using the insert() method.
# This method takes two inputs:
    # * The first: An index to insert an item at.
    # * The second: The item in question.

newList.insert(2, "HELP")
print(newList) # [4, 1, 'HELP', 'two', 3.0, 4]

# This forces the item at index 2 to be "HELP", and pushes everything else
# one spot to the right.

# Let's look at another way to create a list.
# There is nothing forcing us to start with an empty list

anotherList = [1,2,3,4,5,6,5]

# So if you know what you want to have in your list from the beginning, you can
# simply create it with these from the start. 

# How do I remove items?
anotherList.remove(5)
print(anotherList) # [1, 2, 3, 4, 6, 5]

# This searches for the number 5 and removes the first occurence of it.
# What happens if you try to remove an item that isn't there? Try it.

# We can remove the last item from a list using the pop() method.
# This one doesn't need an input, and returns the removed item so you
# can store it in a variable if needed.

last_element = anotherList.pop()
print(last_element) # 5
print(anotherList) # [1, 2, 3, 4, 6]
# 
# Sort of undoes the work that append() does.

# We can also give an index as input to pop() and it will target the item
# at that index, doing the opposite of insert().

third_element = anotherList.pop(2) # Indices start at zero!!!
print(third_element) # 3
print(anotherList) # [1, 2, 4, 6]

#################
# SLICING LISTS #
#################

# The way to get slices of lists is exactly the same as how we do it for
# strings. It follows the same [start:stop:step] notation we saw earlier.

# EXAMPLE: Reversing a list
myList = [1, 2, 3, 4]
reversedList = myList[::-1]
print(reversedList) # [4, 3, 2, 1]
# Easy as.

# Everything else is exactly the same as string slicing.

#############################
# ENHANCED FOR LOOP (AGAIN) #
#############################

# In the same way we were able to loop over characters of a string using
# indices, we can loop over items in a list. This is because lists are another
# iterable object.

for i in range(len(myList)): # len() works on lists too!
    print(myList[i])

# But with the enhanced for-loop:

for item in myList:
    print(item)

# That's it! No need to use indices, no need to figure out what the length of
# your list is. Just jump from one item to the next until you get to the last
# item!
