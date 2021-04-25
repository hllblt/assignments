age = input("Are you a cigarette addict older than 75 years old? (can be assigned only True/False)").title().strip()
choronic = ""
immune = ""
if age == "True" :
  print ("Risk")  
if age != "True" :
  choronic = input("Do you have a severe chronic disease?  (can be assigned only True/False)").title().strip()
  if choronic == "True" :
      print("Risk")
if age != "True" and choronic != "True" :
    immune = input("Is your immune system too weak? (can be assigned only True/False) ").title().strip()
    if immune == "True" :
      print("Risk")
    else :
      print("You are not risky group")
