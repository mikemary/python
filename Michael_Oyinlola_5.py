str = "The quick brown fox jumps over the lazy dog"
#print(str)
#length=(len(str))
#print(length)
#upper_str= str.upper()
#print(upper_str)
#lower_str=str.lower()
#print(lower_str)
#title_str=str.title()
#print(title_str)
#reverse_str=str
#reverse_str=(reverse_str[::-1])
#print(reverse_str)
#reverse_str_title=(reverse_str.title())
#print(reverse_str_title)
#letter_to_count="a"
#str.lower is to make the string all lower case i.e make it case insensitive.
#count=str.lower().count(letter_to_count)
#print(count)
#letter_to_count="the"
#count=str.lower().count(letter_to_count)
#print(count)
#old_word="the"
#new_word="a"
#new_string=str.lower().replace(old_word, new_word)
#print(new_string)
words=str.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] +=1
    else:
        frequency[word] =1

print(frequency)


