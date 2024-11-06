

def q1(): 
  #Write Assignment code here
  print('"Hello World"')

def q2(): 
  #Write Assignment code here
  word = input("Input a word: ")
  print(word.lower())
  print(word.upper())
def q3(): 
  #Write Assignment code here
  word = input("Input a word that is at least 5 letters long: ")
  if len(word) >= 5:
    print(word[1:4])
  else:
    print("The word is too short")

def q4():
  #Write Assignment code here
  word = input("Input a word: ")
  if "o" in word:
    print(word.index("o"))
  else:
    print("The letter 'o' is not in the word.")

def q5(): 
  #Write Assignment code here
  word = input("Input a word: ")
  print(len(word))


#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()
#q4()
#q5()
