import random
import string


adjectives = ['sleepy', 'slow', 'fast', 'white', 'purple', 'big', 'fluffy',  'green', 'smelly', 'proud', 'blue',
                    'wet', 'fat', 'red', 'black', 'brave', 'telephone', 'banana', 'teacher', 'hairy']

nouns = ['apple', 'panda', 'dragon', 'panther', 'steven', 'hammer', 'goat', 'toaster', 'ball','case', 'mouse', 'spain',
             'joy', 'potatoes', ]

print("Welcome to password picker!")

for num in range(4):
             chosen_adjectives = random.choice(adjectives)

             chosen_nouns = random.choice(noun)
             
             number = random.randrange(0, 100)
             
             special_character = random.choice(string.punctuation)

             password = chosen_adjectives + chosen_nouns + str(number) + special_character

             print('Your new password is: %s ' % password)

             response = input('Would you like another  password? Type y or n: ')

             if response.lower() =='n':
                break
          

print('Password Picker finished')   
      

    


   
    

  

   

   
   


   

















