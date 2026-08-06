print(".......Welcome to Car Bidding 2026.......")
repeat=1
bidders=[]

while(repeat==1):
  print("\n"*10)
  details={}
  name=input("Enter Your Name:")
  bid=int(input("Enter the Bidding Amount:"))
  details["Name"]=name
  details["Bid"]=bid
  bidders.append(details)
  repeat=int(input("If there is any other bidder '0' for no and '1' for yes :"))
  if(repeat==1):
    print("\n"*50)
  
  
winner=""
highest_bid=0  
 
for bidder in bidders:
  if bidder["Bid"]>highest_bid:
    highest_bid=bidder["Bid"]
    winner=bidder["Name"]
 
print(f"\nWinner is {winner}") 
print("The bidding amount is {highest_bid}")