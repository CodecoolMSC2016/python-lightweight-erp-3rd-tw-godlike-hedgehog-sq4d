# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader(
    "data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader(
    "common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    table = data_manager.get_table_from_file('accounting/items.csv')
    title = 'Accounting'
    tool_manager_options = ['Show table', 'Add', 'Remove', 'Update',
                            'Most profitable year', 'Average profit of an item per year']
    while True:
        type_list = ["int"]
        ui.print_menu(title, tool_manager_options, 'Back to main menu')
        inputs = ui.get_submenu_inputs(
            ["Please enter a number: "], "", type_list)
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            type_list = "str"
            list_labels = ['Add an id you want to remove: ']
            inputs = ui.get_submenu_inputs(list_labels, '', type_list)
            inputs = inputs[0]
            remove(table, inputs)
        elif option == "4":
            list_labels = ['Add an id you want to update: ']
            type_list = ["str"]
            inputs = ui.get_submenu_inputs(list_labels, '', type_list)
            inputs = inputs[0]
            update(table, inputs)
        elif option == "5":
            which_year_max(table)
        elif option == "6":
            list_labels = ['Enter the year']
            type_list = ["int"]
            inputs = ui.get_submenu_inputs(list_labels, '', type_list)
            result = avg_amount(table, int(inputs[0]))
            ui.print_result(result, '')
        elif option == "0":
            break

    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "month", "day", "year", "type", "amount"]
    ui.print_table(table, title_list)

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    id = common.generate_random(table)
    list_labels = ["month", "day", "year", "type", "amount"]
    title = "Enter the details"
    inputs = []
    inputs = ui.get_submenu_inputs(list_labels, title, type_list)
    inputs.insert(0, id)
    table.append(inputs)
    data_manager.write_table_to_file('accounting/items.csv', table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for nested_list in table:
        if id_ == nested_list[0]:
            table.remove(nested_list)
    data_manager.write_table_to_file('accounting/items.csv', table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    for nested_list in table:
        if id_ == nested_list[0]:
            element = ui.get_submenu_inputs(
                ['Which elements index you want to modify: '], '', type_list)
            element = int(element[0])
            modification = ui.get_submenu_inputs(
                ['Change element: '], '', type_list)
            nested_list[element] = modification[0]

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    max_value = 0
    years_dict = {}
    most_profitable_year = 0
    for line in table:
        if line[3] not in years_dict:
            years_dict.update({line[3]: int(line[5])})
        else:
            if line[4] == "out":
                years_dict[line[3]] -= int(line[5])
            if line[3] in years_dict:
                years_dict[line[3]] += int(line[5])
    for value in years_dict.values():
        if int(value) > max_value:
            max_value = int(value)
    for key, value in years_dict.items():
        if value == max_value:
            key = int(key)
            return key


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    avg = 0
    counter = 0
    for item in table:
        if int(item[3]) == year:
            if item[4] == 'in':
                avg += int(item[5])
            elif item[4] == 'out':
                avg -= int(item[5])
            counter += 1

    if counter == 0:
        result = 0
    else:
        result = avg / counter

    return(result)
