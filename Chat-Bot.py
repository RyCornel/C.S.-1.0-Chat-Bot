import random

def get_bot_response(user_response):

    chat_bot_response_happy = ["Noice!", "Happy to hear that!", "Awesome!"]
    chat_bot_response_sad = ["I'm sorry to hear that.", "Well, hopefully your day gets better", "Lifting weights will make you feel better."]

    happy_list = ["Happy", "Good", "Great", "Awesome", "Amazing"]
    sad_list = ["Sad", "Down", "Not great", "Not good", "Not well", "Upset"]

    for user_response in happy_list:
        return print(random.choice(chat_bot_response_happy))
    for user_response in sad_list:
        return print(random.choice(chat_bot_response_sad))
    else:
        return print("I hope your day imporves even more")


    print("Welcome to Chat Bot")
    print("Please enter how you are feeling today")


    user_response = ""
    
    while True:
        user_response = input("How are you feeling today?: ")

        if user_response == ["done", "stop it", "quit"]:
            break

        bot_response = get_bot_response(user_response)
        print(bot_response)
