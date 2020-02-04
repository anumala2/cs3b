from re import findall

"""
#1
def frequency(content):
    pattern = '[a-z]+'
    words = re.findall(pattern, content)
    dictionary = {}
    for w in words:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1
    return dictionary


#2
def frequency(content):
    pattern = '[A-Z]+'
    words = re.findall(pattern, content)
    dictionary = {}
    for w in words:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1
    return dictionary

#3
def frequency(content):
    pattern = '[a-zA-Z]'
    words = re.findall(pattern, content)
    dictionary = {}
    for w in words:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1
    return dictionary
"""
#4
def frequency(content):
    pattern = '[a-zA-Z]+'
    words = findall(pattern, content)
    dictionary = {}
    for w in words:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1
    return dictionary


content = 'In a land far far away called never land'
print(frequency(content))
