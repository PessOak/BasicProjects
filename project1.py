# string concatenation (how to put strings together)

# a few ways of writing: "subscribe to _____" :
# youtuber = "Pessoa Humana"
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It drives me crazy all the time because I like to \
{verb1}. Stay up until the end and {verb2} like you are {famous_person}!"

print(madlib)

