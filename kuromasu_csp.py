#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented.

'''
Construct and return kuromasu CSP models.
'''

from cspbase import *
import itertools

def kuromasu_csp_model_1(initial_futoshiki_board):
    
       domain = ['w','b']
       
       var_2d_list = []
       domain_2d_list = []
       constraints = []
       #generate Variables and corresponding domains:
       
       for row in range(0,len(initial_futoshiki_board)):
              var_row = []
              domain_row = []
              for col in range(0,len(initial_futoshiki_board[row])):
                     v = Variable(str(row) + "."+ str(col))         
                     if  (initial_futoshiki_board[row][col] == ''):
                            #if a square is empty, it can be b or w
                            v.add_domain_values(domain)
                            domain_row.append(domain)                     
                     else:
                            #if a square isnt empty, its a number and can only be white
                            v.add_domain_values(['w'])
                            
                            n = (int)(initial_futoshiki_board[row][col])
                            v.set_attribute(n)                                            
                            domain_row.append(['w'])
                            
                     var_row.append(v)
              var_2d_list.append(var_row)
              domain_2d_list.append(domain_row)
       
       
       #add constraints to make sure no two squares in a row are black
       for x in range(0, len(var_2d_list)):
            
              for y in range(0,len(var_2d_list[x]) -1):    
                     lhs = var_2d_list[x][y]
                     rhs = var_2d_list[x][y+1]
                     c = Constraint(lhs.name +"r_b/=" + rhs.name, [lhs,rhs])
                     tuple_list = []
                     for i in lhs.domain():
                            for j in rhs.domain():
                                   if (not( i=="b" and j=="b" )):
                                          tuple_list.append((i,j))
                                          
                     c.add_satisfying_tuples(tuple_list)                            
                     constraints.append(c)
       
       #add constraints in a col to make sure no two squares are black.
       
       for x in range(0, len(var_2d_list)):
              column = []
              for y in range(0,len(var_2d_list)):
                     column.append(var_2d_list[y][x])
              for i in range(0, len(column)-1):
                     lhs = column[i]
                     rhs = column[i+1]
                     c = Constraint(lhs.name +"c_b/=" + rhs.name, [lhs,rhs])
                     tuple_list = []
                     for i in lhs.domain():
                            for j in rhs.domain():
                                   if (not( i=="b" and j=="b" )):
                                          tuple_list.append((i,j))
                                          
                     c.add_satisfying_tuples(tuple_list)                            
                     constraints.append(c)
                            
                            
       #Make sure no white is surrounded by blacks                     
             
       surround_constraints = []
       for x in range(0, len(var_2d_list)):
              for y in range(0, len(var_2d_list[x])):
                     
                     if('w' in var_2d_list[x][y].domain()):                                   
                            var_list= []
                            var_list.append(var_2d_list[x][y])
                            #get the var to the left
                            if (y>0):
                                   var_list.append(var_2d_list[x][y-1])
                            #get the var to the right
                            if (y<len(var_2d_list[x])-1):
                                   var_list.append(var_2d_list[x][y+1])
                            if (x > 0):
                                   var_list.append(var_2d_list[x-1][y])
                            if (x < len(var_2d_list[x]) -1):
                                   var_list.append(var_2d_list[x+1][y])
                            
                            c = Constraint("c_surround constraint " + str(x) + str(y), var_list)
                            val_list = [var.domain() for var in var_list]
                            sat_tuples = []
                            for t in itertools.product(*val_list):
                                   allBlack = True
                                   for i in t[1:]:
                                          if (i != 'b'):
                                                 allBlack = False
                                   if (not(allBlack and t[0] == 'w')):
                                          sat_tuples.append(t)
                            
                            c.add_satisfying_tuples(sat_tuples)
                            surround_constraints.append(c)
       
       #add constraints for number squares       
       number_constraints =[]
       for x in range(0, len(var_2d_list)):
              for y in range(0, len(var_2d_list[x])):       
                     if (var_2d_list[x][y].attribute > 0):
                            #this variable is a number
                            col_var_list = []
                            #get all the variables in that column
                            for z in range(0,len(var_2d_list)):
                                   col_var_list.append(var_2d_list[z][y])                            
                            
                            var_list = var_2d_list[x] #get all the variables from that row
                            col_val_list = [var.domain() for var in col_var_list]
                            
                            val_list = [var.domain() for var in var_list]
                            
                            sat_tuples = []
                            total_var_list= []
                            total_var_list.extend(var_list)                            
                            total_var_list.extend(col_var_list[0:x] + col_var_list[x+1:]) #this makes sure the the number variable doesnt get added twice as it exists both in col_var_list and var_list
                            
                            c = Constraint("c_number_constraint_" + str(x) + str(y), total_var_list)
                            
                            for t in itertools.product(*val_list):
                                   for r in itertools.product(*col_val_list):
                                          row_sum =   return_longest_sequence(t,y) 
                                          col_sum= return_longest_sequence(r,x) -1 #since the function counts the variable also, subtracting one to make sure it doesnt get double counted 
                                          
                                          if (row_sum + col_sum == var_2d_list[x][y].attribute):                                          
                                                 sat_tuples.append(t + r[0:x] + r[x+1:])
                            
                            c.add_satisfying_tuples(sat_tuples)
                            number_constraints.append(c)
                     
                                          
                            
       _vars = []
       for i in var_2d_list:
              for j in i:
                     _vars.append(j)
       
       csp = CSP("board2", _vars)
       for c in constraints:
              csp.add_constraint(c)      
       for c in surround_constraints:
              csp.add_constraint(c)
              
       for c in number_constraints:
              csp.add_constraint(c)       
       return (csp,var_2d_list)


def return_longest_sequence(t,y):
       '''Returns the longest sequence of unbroken white squares from either side of the variable'''
       _sum = 0
       for i in range(y,len(t)):
              if (t[i] == 'w'):
                     _sum +=1
              else:
                     break
       for i in range(y-1,-1,-1):
              if (t[i] == 'w'):
                     _sum +=1
              else:
                     break
   
       return _sum
