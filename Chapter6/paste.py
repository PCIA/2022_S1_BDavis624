Amazon = "Help! Help! I'm being eaten alive by piranhas."

def countSentences(theText):
   sentenceCount = 0
   
   terminals = '.!?;'
 
   for char in theText:
      if char in terminals:
         sentenceCount = sentenceCount + 1

   return sentenceCount

print( countSentences(Amazon))