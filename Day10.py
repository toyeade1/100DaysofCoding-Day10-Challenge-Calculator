
play_again = True
while play_again:
    print('+\n-\n*\n/')
    first_num = int(input("What's the first number?: "))
    operation = str(input('Pick an operation: '))
    second_num = int(input("What's the second number?: "))

    if operation == '+':
        answer = first_num + second_num
    elif operation == '-':
        answer = first_num - second_num
    elif operation == '*':
        answer = first_num * second_num
    elif operation == '/':
        answer = first_num / second_num
    else:
        print("Error in operator, please use '+' '-' '*' or '/' " )
    print(answer)

    user_prompt = str(input("Type 'y' to conitnue calculating with 2.5, or type 'n' to start a new calculation.\n"))
    if user_prompt == 'n':
        play_again = False