print("What is your name")
name = input()
print("Hello " + name +", how are you today(happy/sad)")
feeling=input()
if feeling=="happy":
  print("That is very good then")
elif feeling =="sad":
  print("That's not good then")
else:
  print("OK")
print("What is your favourite sport")
sport=input()
if sport=="football":
  print("What team do you support")
  team=input()
if team=="Scotland" or team=="scotland" :
  print("You aren't very good are you?")