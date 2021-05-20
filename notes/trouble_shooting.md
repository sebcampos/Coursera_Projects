# Trouble Shooting

## Debuggers

- Debuggers let us follow the code line by line, inspect changes in variable assignments, interupt the program when a specific condition is met, and more

- `strace` a command that will show all the system calls that a program has made we can see this by calling `strace python_script.py`

- using `strace -o faliure.strace python_script.py` will send the output of the strace to a new file called faliure.strace

- when something is not behaving as it should, then the log files should be checked

- `ltrace` a command that will show all the library calls the program has made

- `itop` a tool for viewing input and output

## Binary Search

- In a sorted list we can compare the size of the item to the item in the middle of the sorted dataset. then we can decide to move up or down based on that value. ie if the middle value is less than our search criteria value then we have determined that our search criteria value exists in the higher range.
Then we partition the list / data structure again in the middle of this higher range and continue the process untill our search is over. This is a base 2 logarithm of the list /data 's length -- this is prefered for longer lists

## Linear Search

- Search the list or data top down for the given search criteria. Duration is dependant on the length of the list


## Bisecting

- Bisecting files is similar to binary search in the sense that we partition our issue and test our partitions in an attempt to find the faulty partition. 
