def coffee_bot():
  print("Welcome to the cafe!")

  size = get_size()
  drink_type = get_drink_type()
  print("Alright, that's a {} {}!".format(size, drink_type))
  hot_cold()
  name = input("Can I get your name please? ")
  another_drink()
#  extra_drink = another_drink()
#  print("Okay {}, so it's a {} {} for your other drink!".format(name, size, extra_drink))
  print("Thanks, {}! Your drink will be ready shortly.".format(name))

def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")

  if res == "a":
    return "small"
  elif res == "b":
    return "medium"
  elif res == "c":
    return "large"
  else:
    print_message()
    return get_size()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n")
  
  if res == "a":
    return "Brewed Coffee"
  elif res == "b":
    return "Mocha"
  elif res == "c":
    return order_latte()
  else:
    print_message()
    return get_drink_type()

# def another_drink():
#   res = input("Would you like to order another drink? \n[a] Yes, please \n[b] No, that would be all \n")
#   if res == "a":
#     return get_size(), get_drink_type(), 
#   elif res == "b":
#     return "No, that would be all"
#   else:
#     print_message()
#     return another_drink()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n")

  if res == "a":
    return "2% milk"
  elif res == "b":
    return "Non-fat milk"
  elif res == "c":
    return "Soy milk"
  else:
    print_message()
    return order_latte()

def hot_cold():
  res = input("How would you like your drink? \n[a] Hot \n[b] Cold")
  if res == "a":
    print("Ohoho that's hot... that's hot!")
  elif res == "b":
    print("Ice ice baby!")
  else: 
    print_message()
    return hot_cold()

def another_drink():
  res = input("Would you like to order another drink? \n[a] Yes, please \n[b] No, that would be all \n")
  if res == "a":
    return get_size(), get_drink_type(), 
  elif res == "b":
    return "No, that would be all"
  else:
    print_message()
    return another_drink()


# python3 script.py
coffee_bot()
