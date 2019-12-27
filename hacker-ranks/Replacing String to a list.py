i = "1 2 3 4 5 6".rstrip().split()
print (list(map(int, i)))
# A map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.) .
# rstrip() method returns a copy of the string with trailing characters removed (based on the string argument passed). If no argument is passed,
# it removes trailing spaces. Parameters : chars (optional) – a string specifying the set of characters to be removed.