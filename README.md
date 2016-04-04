# kuromasu

To run the program, you have to use the file titled kuromasu_sample_run, which already contains several unsolved puzzles. 

Each puzzle is a 2d matrix array, similar tothe way the futoshiki grids were structured. 
Each array inside the array is a row in the grid, and each block can either hold a value or a blank. 

To test a puzzle to solve, create a 2d matrix array which holds number values for the number blocks and blanks everywhere else and add the puzzle to the testcases list. 
Now run the program. This will produce the solution to the puzzle. 

To switch hueristics, when you call bt_search in kuromasu_sample_run, you have to pass in a boolean which determines whether to use the new hueristic. 

If the parameter for newheuristic in bt_search is true, it runs the new heuristic which is based on the constaints for each variable. 


Currently, the sample program is setup to run all the unsolved puzzels with all heuristic functions (Domain and constraint based.).
