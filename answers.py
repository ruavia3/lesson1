question = input("я соскучился!\n")
answers ={"привет": "ну привет!", "как дела?": "пока не родила", "пока": "пока пока"}
def get_answer(question):
	return answers [question]
print(get_answer(question))
while True:
    question = input("")
    print(get_answer(question))
    if question == "пока":
        break