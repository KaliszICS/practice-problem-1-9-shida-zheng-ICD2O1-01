

def q1(): 
  #Write Assignment code here
  print('"Hello World"')

def q2(): 
  #Write Assignment code here
  a = input("Input a word:")
  print(a.lower())
  print(a.upper())

def q3(): 
  #Write Assignment code here
  a = input("Input a word that is at least 5 letters long: ")
  if len(a) >= 5:
        print(a[1:4])
  else:
        print("The word is not long enough.")
  
def q4(): 
  #Write Assignment code here
  a = input("Input a word:")
  index = a.find('o')
  if index != -1:
        print(f"The first occurrence of 'o' is at index {index}.")
  else:
        print("The letter 'o' was not found.")
def q5(): 
  #Write Assignment code here
  a = input("Inout a word:")
  print(len(a))


#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
q3()
q4()
q5()
