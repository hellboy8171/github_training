def add(stuff):
    sum = 0
    #stuff = list(stuff)
    #stuff[0] = 0
    for i in stuff:
        sum += i
        return sum


def validate_and_execute():
    try:
        user_input_number = int(user_input_element)
        if user_input_number > 0:
            calculated_value = add(user_input_number)
            print(calculated_value)

        elif user_input_number == 0:
            return "you entered a 0, please check the value again"

        else:
            print("you enter a negative value! so, no conversion for you")

    except ValueError:
        print("your input is not a valid number, don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user! give me a comma separated list and i will add them\n")
    list_of_numbers = user_input.split(",")

    for user_input_element in list_of_numbers:
        validate_and_execute()
