from kuromasu_csp import *
from propagators import *

def print_sudo_soln(var_array):
    for row in var_array:
	        print([var.get_assigned_value() for var in row])
puzzle1 =[['9','','','8','','9', '', '8',''],['','','','','','','9', '', ''],
          ['','','','','','', '', '3',''],['3','','','','','4', '', '','3'],
          ['','','4','','','','9', '',''],['4','','','6','','', '', '','4']
          ,['','15','','','','', '', '',''], ['','','7','','','', '', '',''],['','7','','5','','4', '', '','4']]
          
csp,var_array = kuromasu_csp_model_1(puzzle1)
solver = BT(csp)
print("GAC")
solver.bt_search(prop_GAC)
print("Solution")
print_sudo_soln(var_array)
print("===========")

csp,var_array = futoshiki_csp_model_2(puzzle1)
solver = BT(csp)
print("GAC")
solver.bt_search(prop_GAC)
print("Solution")
print_sudo_soln(var_array)
print("===========")
