words = {}
words['large'] = {'definition':'Having much size.', 'synonyms':['big','volumous','grande'],'UseCount':5}
words['small'] = {'definition':'Having low size.', 'synonyms':['little','mini'],'UseCount':10}
words['gray'] = {'definition':'A neutral color that is neither black nor white.', 'synonyms':['grey','ash'],'UseCount':15}

def averageWordUse():
   total = 0
   for word in words:
      currentWord = words[word]
      # I was a little lost on this problem. I don't know what I've done here, but I've done something.
      total = total + currentWord['UseCount']
   return total / len(words)

print(averageWordUse())