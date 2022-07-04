import random

answer_dictionary = {1 : "Yes - definitely.", 2 : "It is decidedly so.", 3 : "Without a doubt.", 4 : "Reply hazy, try again.", 5 : "Ask again later.", 6 : "Better not tell you now.", 7 : "My sources say no.", 8 : "Outlook not so good.", 9 : "Very doubtful.", 10 : "It is certain.", 11 : "You may rely on it.", 12 : "As I see it, yes.", 13 : "Most likely.", 14 : "Outlook good.", 15 : "Yes.", 16 : "Signs point to yes.", 17 : "Cannot predict now.", 18 : "Concentrate and ask again.", 19 : "Don't count on it.", 20 : "My reply is no."}

name = input("Please enter your name: ")
counter = 0

while counter == 0:

  question = input("\nPlease enter a question: ")
  answer = random.randint(1,20)

  if question == "":
    print("\nPlease enter a valid question.")
  elif name == "":
    print("\nQuestion: " + question)
    print("\nMagic 8-Ball's answer:", answer)
  else:
    print("\n" + name, "asks:", question)
    print("\nMagic 8-Ball's answer:", (answer_dictionary[answer]))