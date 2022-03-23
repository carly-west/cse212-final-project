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


### Set Unions


### Finding the Size of Set


### Finding if Item is in a Set



