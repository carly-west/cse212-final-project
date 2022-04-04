# The Set Data Structure

## Introduction
One of the main characteristics of sets is that they do not allow duplicate values. It also doesn't care about the order of the items in the set, so it might print it out differently each time. You might ask, when should I use a set? The main purpose of choosing a set over any other data structure is ensuring that repeat values are not added to a set. Searching quickly and efficiently through a set to see if a value has already been added is also an an advantage of sets.

### Printing Sets
One important thing to note about sets is that the order of items that are added isn't taken into consideration when printing a set out. Here is an example of what the output might be of printing this set. Notice how the order of printing is different than the order they were added.

```
my_set = {"apple", "banana", "cherry"}

print(my_set) 

# Output: {'apple', 'cherry', 'banana'}

```

### Dealing with Duplicates
If a duplicate is added to a set, Python just ignores it and doesn't add it. There also isn't an error thrown when it is added. Here is what that might look like. Notice how the duplicate item, "apple", was not added into the set:

```
my_set = {"apple", "banana", "cherry"}

my_set.add("apple")

print(my_set) 

# Output: {'apple', 'cherry', 'banana'}
```

## Set Operations

### Creating a Set 
Here is how a set is created:
```
my_set = {1, 2, 3, 4}
```

### Adding Items to a Set
This is how an item is added to a set. If the item is already in the set, it will be ignored. This is an O(1) performance.

```
my_set.add(5)

# The set now looks like this: {1, 2, 3, 4, 5}
```


### Removing Items from a Set
Removing values from a set can be done like this. It is an O(1) performance.

```
my_set.remove(3)

# Remaining set: {1, 2, 4, 5}
```


### Set Intersections
Set intersections can be used to return a new set with the common elements of both sets. It can be used with as many sets as needed. This would have the performance of O(n). Here is an example of finding the intersection of two sets:

```
first_set = {"apple", "banana", "cherry", "watermellon"}
second_set = {"cherry", "watermellon", "lemon", "cherry"}

# Here is the sytax for intersecting sets
set_intersection = first_set & second_set

print(set_intersection)

# Output: {'cherry', 'watermellon'}
```

Cherry and watermellon were the only two values that were included in both sets.

### Set Unions
Unions with sets do the opposite of intersections, they return a new set with all of the distinct and unique values of the sets. This would be O(n) performance. Here is how this can be done:

```
first_set = {"apple", "banana", "cherry", "watermellon"}
second_set = {"cherry", "watermellon", "lemon", "cherry"}

# This is the syntax for finding the union of sets
set_union = first_set | second_set

print(set_union)

# Output: {'banana', 'watermellon', 'apple', 'cherry', 'lemon'}
```
The output are the values that were not in both sets.

### Finding the Size of Set
To find the number of items in the set, you can use the len() funciton. This has an O(1) performance. It would be done like this:

```
my_set = {"apple", "banana", "cherry"}

set_length = len(my_set)

print(set_length)

# Output: 3
```

### Finding if Item is in a Set
In order to check for an item in a set, you can us an "if" block. This ins O(1) performance. It will look like this:

```
my_set = {"apple", "banana", "cherry"}

if "orange" in my_set:
  print("Orange is in the set!")

if "apple" in my_set:
  print("Apple is in the set!"

#  Output: "Apple is in the set!"
```


## Code Example
Let's say that there is a user that wants to add a song to a playlist. They wouldn't want the same song in the playlist more than once! This can be done with sets!


Here is how they add a song to a playlist:
```
playlist = {"Don't Stop Believing", "Eye of the Tiger", "Livin' on a Prayer", "Imagine", "Hey Jude", "Billie Jean"}

# This is the unique song they would like to add
new_song = "Hotel California"

# Here is a repeat song
repeat_song = "Imagine"

# Add the songs to the playlist
playlist.add(new_song)
playlist.add(repeat_song)

print(playlist)

# Output: {'Eye of the Tiger', "Livin' on a Prayer", 'Billie Jean', 'Imagine', "Don't Stop Believing", 'Hotel California', 'Hey Jude'}
```

Notice how the order of the playlist is all mixed up! Luckily, our user doesn't care about the order of the songs. Also notice how the repeat song "Imagine" was already in the playlist, so it wasn't added again.


Now let's say they have two different playlists, and they would like to find all of the songs that are in both playlists. They can do this by using an intersection:

```
playlist_1 = {"Let it Go", "A Whole New World", "You're Welcome", "Colors of the Wind", "Be our Guest", "Hakuna Matata"}

playlist_2 = {"Circle of Life", "We Don't Talk About Bruno", "Into the Unknown", "Hakuna Matata", "Let it Go"}

playlist_intersection = playlist_1 & playlist_2

print(playlist_intersection)

# Output: {'Let it Go', 'Hakuna Matata'}
```

It looks like there were two songs that repeated, "Let it Go", and "Hakuna Matata". Our use can now go through their playlists and clean them all up.


## Problem for you to solve!

You are tasked with creating a system for users to sign up for a website. Create a program following these steps:
1. Use the following list that already have accounts:
  a. user232@abc.com, email1211@email.com, user909@yahoo.com, email@gmail.com, email1231@yahoo.com, user10101@outlook.com, user123@yahoo.com
2. Create a new set with the following emails:
  a. email@gmail.com, user123@yahoo.com, testing222@outlook.com, tests1233@yahoo.com, snailmail@gmail.com, user10101@outlook.com
3. Check to see if there are any repeat emeails using an intersection
4. Create a new set using intersection with all of the unique emails.
5. Find the number of accounts added to the new set looping through the old email list, and counting the emails that were added.

[Link to the solution](set_code_solution.py)



[Back to Welcome Page](0-welcome.md)
