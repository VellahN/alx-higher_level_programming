A list is an ordered set of values, where each value is identified by an index. The values that make up a list are called its elements. Lists are similar to strings, which are ordered sets of characters, except that the elements of a list can have any type. Lists and strings — and other things that behave like ordered sets — are called sequences.

A list within another list is said to be nested.

Finally, there is a special list that contains no elements. It is called the empty list, and is denoted [].

Like numeric 0 values and the empty string, the empty list is false in a boolean expression

The function len returns the length of a list, which is equal to the number of its elements. It is a good idea to use this value as the upper bound of a loop instead of a constant. That way, if the size of the list changes, you won’t have to go through the program changing all the loops; they will work correctly for any size list

in is a boolean operator that tests membership in a sequence. We used it previously with strings, but it also works with lists and other sequences:
