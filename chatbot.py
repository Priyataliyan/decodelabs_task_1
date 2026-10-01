print("===================================")
print("            AI CHATBOT             ")
print("====================================")

print("Hello! I'm your AI assistant.")
print("How can I help you today?")


dict={
   "hello":" hello! how can i assist you today?",
   "hi": "Hi there! What can i do for you?",
   "how are you":"I am just a program, but I'm functioning as experted! How about you?",
   "What can you do ":"I can answer your questions and have a conversation with you. ",
   "thank you":"You're welcome! If you have any more questions, feel free to ask",
    "add": "Sure! Please provide the numbers you want to add, separated by spaces.",        
     "subtract": "Sure! Please provide the numbers you want to subtract, separated by spaces.", 
    "multiply": "Sure! Please provide the numbers you want to multiply, separated by spaces.", 
    "divide": "Sure! Please provide the numbers you want to divide, separated by spaces."
}

while True:
    user_input = input("You:").lower().strip()

    if user_input in dict:
        print("Bot:",dict[user_input]) 

    elif user_input.startswith("add"):
        try:
            numbers = list(map(float,user_input.split()[1:]))

            if not numbers:
                print("Bot: Please provide numbers to add.")
            else:
                result = sum(numbers)
                print("Bot:The sum is",result)

        except ValueError:
            print("Bot: Please provide valid numbers.")

    elif user_input.startswith("subtract"):
        try:
               numbers = list(map(float,user_input.split()[1:]))
   
               if len(numbers)<2:
                   print("Bot: Please provide at least two numbers to subtract.")
               else:
                   result = numbers[0]-sum(numbers[1:])
                   print("Bot:The sum is",result)
   
        except ValueError:
               print("Bot: Please provide valid numbers.")

    elif user_input.startswith("multiply"): 
        try: 
            numbers = list(map(float, user_input.split()[1:])) 
 
            if not numbers: 
                print("Bot: Please provide numbers to multiply.") 
            else: 
                result = 1 
 
                for num in numbers: 
                    result *= num 
 
                print("Bot: The product is", result) 
 
        except ValueError: 
            print("Bot: Please provide valid numbers.") 
 
    elif user_input.startswith("divide"): 
        try: 
            numbers = list(map(float, user_input.split()[1:])) 
 
            if len(numbers) < 2: 
                print("Bot: Please provide at least two numbers to divide.") 
            else: 
                result = numbers[0] 
 
                for num in numbers[1:]: 
                    if num == 0: 
                        print("Bot: Division by zero is not allowed.") 
                        break 
 
                    result /= num 
 
                else: 
                    print("Bot: The result is", result) 
 
        except ValueError: 
            print("Bot: Please provide valid numbers.") 
 
    elif user_input in ["exit", "bye", "quit"]: 
        print("Bot: Goodbye! Have a great day!") 
        break 
 
    else: 
        print("Bot: I'm sorry, I don't understand that. Can you please rephrase?") 
 
print("========================================")
   
