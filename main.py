from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = []
bidders = True

def winner(list):
  majorValue = 0
  name = ""
  for index in range(len(list)):
    for key in list[index]:
      if list[index][key] > majorValue:
        majorValue = list[index][key] 
        name = key
  print(f"The winner is {name} with a bid of {majorValue}")      

while bidders:
  print("Welcome to the secret auction program.")
  name = input("What is your name?: ")
  bid = float(input("What's your bid?: $"))
  person = {}
  person[name] = bid

  bids.append(person)
  response = input("Are there any other bidders? Type 'yes or 'no'.")
  if response == 'no':
    bidders = False
  elif response == 'yes':
    clear()  
print()    
winner(bids)    




