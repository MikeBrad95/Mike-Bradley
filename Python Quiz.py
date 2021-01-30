name = input("Name: ")
print("Hello ",name)
print()
print("Quiz Time")

question = 0
points = 100
wrong = 16.666

while(question !=6):
  
  print("Question 1: What is the 3rd Month of the year?")
  print("a.","May")
  print("b.","October")
  print("c.","January")
  print("d.", "March")
  user_input = input("Answer is: ")
  if(user_input != 'd'):
    print("Incorrect")
    points = points - wrong
    question = question +1
  else:
    print("Correct")
    question = question +1
    
  print()
  
  print("Question 2: What day is Air Max Day?")
  print("a.","23rd")
  print("b.","10th")
  print("c.","31st")
  print("d.", "26th")
  user_input = input("Answer is: ")
  if(user_input != 'd'):
    print("Incorrect")
    points = points - wrong
    question = question +1
  else:
    print("Correct")
    question = question +1
    
  print()
  
  print("Question 3: How many days are in a year?")
  user_input = input("Answer is: ")
  if(user_input != '365'):
    print("Incorrect")
    points = points - wrong
    question = question +1
  else:
    print("Correct")
    question = question +1
    
  print()
  
  print("Question 4: What year was the Air Max III created?")
  user_input = input("Answer is: ")
  if(user_input != '1990'):
    print("Incorrect")
    points = points - wrong
    question = question +1
  else:
    print("Correct")
    question = question +1
            
  print()
  
  print("Question 5: T/F I am doing this for a grade?")
  user_input = input("Answer is: ")
  if(user_input != 'T'):
    print("Incorrect")
    points = points - wrong
    question = question +1
  else:
    print("Correct")
    question = question +1

  print()
  
  print("Question 6: T/F Buying sneakers is a waste of money?")
  user_input = input("Answer is: ")
  if(user_input == 'T'):
    print("Incorrect")
    points = points - wrong
    question = question +1
  else:
    print("Correct")
    question = question +1
    
  print()

  print("Your point total is:", round(points))
  print("Want to play again: Yes or No")
  user_input = input(" ")
  if(user_input == 'Yes'):
    question =0
  else: 
    print("Have a good day")
    break