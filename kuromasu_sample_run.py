from kuromasu_csp import *
from propagators import *


def print_sudo_soln(var_array):
    for row in var_array:
        print([var.get_assigned_value() for var in row])

puzzle1 = [['', '', '', ''],
           ['3', '', '2', ''],
           ['', '3', '', '4'],
           ['', '', '', '']]

puzzle2 = [['', '', '4', ''],
           ['3', '', '', ''],
           ['', '', '', '2'],
           ['', '7', '', '']]

puzzle3 = [ ['', '', '', '2', ''],
            ['6', '', '4', '', ''],
            ['', '5', '', '3', ''],
            ['', '', '6', '', '8'],
            ['', '5', '', '', '']]


puzzle4 = [['', '', '', '', '', ''],
            ['', '', '', '5', '', ''],
            ['', '2', '', '', '5', ''],
            ['', '', '', '', '', ''],
            ['2', '', '3', '', '', ''],
            ['', '', '', '', '', '4']]

puzzle5 = [['', '2', '6', '', '', '', '3'],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['3', '', '', '5', '', '', '4'],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['2', '', '', '', '7', '4', '']]

puzzle6 = [['', '', '', '8', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '3'],
            ['6', '', '', '', '', '', '', ''],
            ['', '', '', '3', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '2', '', '', '', '', '', '4'],
            ['', '', '', '', '', '', '', '2']]

puzzle7 = [['9', '', '', '8', '', '9', '', '8', ''],
           ['', '', '', '', '', '', '9', '', ''],
           ['', '', '', '', '', '', '', '3', ''],
           ['3', '', '', '', '', '4', '', '', '3'],
           ['', '', '4', '', '', '', '9', '', ''],
           ['4', '', '', '6', '', '', '', '', '4'],
           ['', '15', '', '', '', '', '', '', ''],
           ['', '', '7', '', '', '', '', '', ''],
           ['', '7', '', '5', '', '4', '', '', '4']]

tescases = [puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6, puzzle7]

print("\n\n\nNow testing heuristic 1, removing variable with min sized cur domain.\n\n\n")
for test in tescases:
    csp, var_array = kuromasu_csp_model_1(test)
    solver = BT(csp)
    print("GAC")
    solver.bt_search(prop_GAC, False)
    print("Solution")
    print_sudo_soln(var_array)
    print("===========")

print("\n\n\nNow testing heuristic 2, removing variable with maximum number of contraints.\n\n\n")
for test in tescases:
    csp, var_array = kuromasu_csp_model_1(test)
    solver = BT(csp)
    print("GAC")
    solver.bt_search(prop_GAC, False)
    print("Solution")
    print_sudo_soln(var_array)
    print("===========")
