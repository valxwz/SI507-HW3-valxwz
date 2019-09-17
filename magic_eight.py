import random

answer_list = ['It is certain.', 'As I see it, yes.', 'It is decidedly so.','Without a doubt.','Yes - definitely.','You may rely on it.','Most likely.','Outlook good.','Yes.','Signs point to yes.','Reply hazy, try again.','Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again.','Don not count on it.','My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.']

ask_question = True

while ask_question:
	question=input("What's your question? ")
	if question == "quit":
		print('Bye bye.')
		ask_question =False
	elif question[-1] != "?":
		print('Sorry, I can only answer a question.')
	else: 
		print(random.choice(answer_list))
