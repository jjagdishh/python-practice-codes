def break_words(stuff):
#This function will break up words into list.
 words = stuff.split(' ')
 return words

n=break_words('hello there')
print (n)


def sort_words(words):
#Sorts the words.
 return sorted(words)

n=sort_words('hello')
print(n)

# Prints the first word after popping it off.
def print_first_word(words):
      word = words[0]
      return word

print (print_first_word("Hello"))



def print_last_word(words):
#Prints the last word after popping it off.
 word = words[-1]
 return word

n=print_last_word('hello')
print(n)


def sort_sentence(sentence):
#Takes in a full sentence and returns the sorted words.
 words = break_words(sentence)
 return sort_words(words)

n=sort_sentence('there hello A')
print (n)

def print_first_and_last(sentence):
#Prints the first and last words of the sentence.
 words = break_words(sentence)
 print_first_word(words)
 print_last_word(words)

n=print_first_and_last("hello there i am here")
print(n)


def print_first_and_last_sorted(sentence):
#Sorts the words then prints the first and last one.
 words = sort_sentence(sentence)
 print_first_word(words)
 print_last_word(words)

n=print_first_and_last_sorted("z hello there i am here")
print(n)
