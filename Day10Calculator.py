from Day10logo import logo

def add(first_num, second_num):
    return first_num + second_num
def subtract(first_num, second_num):
    return first_num - second_num
def multiply(first_num, second_num):
    return first_num * second_num
def divide(first_num, second_num):
    return first_num / second_num

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
print(logo)
restart_calculation = False
while not restart_calculation:
    first_num = float(input("What's the first number?: "))
    print('+\n-\n*\n/')
    operation = str(input('Pick an operation: '))
    second_num = float(input("What's the next number?: "))
    calculation = operations[operation]
    first_answer = calculation(first_num, second_num)
    print(f'{first_num} {operation} {second_num} = {first_answer}')
    continue_calc = str(input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation:\n"))
    while continue_calc == 'y':
        second_operation = str(input('Pick an operation: '))
        calculation = operations[second_operation]
        third_num = float(input("What's the next number?: "))
        second_answer = calculation(first_answer, third_num)
        print(f'{first_answer} {second_operation} {third_num} = {second_answer}')
        first_answer = second_answer
        continue_calc = str(input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to start a new calculation:\n"))
        if continue_calc == 'n':
             continue






