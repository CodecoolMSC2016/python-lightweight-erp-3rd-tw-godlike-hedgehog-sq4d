

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    # címsor maximális oszlopszélessége
    for item in title_list:
        max_len =  len(max(title_list, key = len))
    # az oszlopszélesség meghatározása
    max_lenght_list = [max(len(str(item)) for item in line) for line in zip(*table)]
    print(max_lenght_list)
    # tábla szélesség meghatározása
    table_lenght = 0
    for item in max_lenght_list:
        table_lenght += int(item)
    table_lenght = table_lenght + int(len(title_list))*2
    print(table_lenght)

    print("/", "-"*table_lenght, chr(92))
    print("|", end = "")
    for index in range(0, len(title_list)):
        print(title_list[index].center(max_lenght_list[index]+2), "|", end = "")
    print('\n')   
    print("|", end = "")
    for index in range(0, len(title_list)):
        print("-"*(max_lenght_list[index]+2), "|", end = "")
    print('\n')

    
                
    #pass


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

    # your code

    pass


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    counter = 0
    print(title, ':')
    for item in list_options:
        counter += 1
        print('(', counter, ')', item)
    print('( 0 )', 'Exit')
    # your code

    pass


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for label in list_labels:
        label = label + " : "
        usr_in = input(label)
        inputs.append(usr_in)

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    # your code

    pass
