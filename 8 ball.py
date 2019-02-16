import random

def readData():
    response_file = open('8_ball_responses.txt', 'r')
    responses = response_file.readlines()
    
    input('Press enter to continue')
     
    input('What is your question:\n')
   
 # I need to make sure to through it through a while loop for this part    
    response_file.close()   

    return responses

def stripLineFeed(responses):
    for i in range(len(responses)):
        responses[i] = responses[i].rstrip('\n')
    print(responses[i])
     
    return responses

def randomAnswers(responses):
    for i in range(responses):
        responses[i].append(random.randint(responses)) 
    return responses

responses = readData()
responses = stripLineFeed(responses)
again=1
while again==1:
    readData()
    again=int(input('\n\nrun again? 1=yes 0=no '))


        
        
   
             
            
        
        
       
    
    