# sys module

## functions
- `sys.argv` returns a list of arguemts in `sys` ie 
	```
	~$python_script first_arg second_arg

	sys.argv[2] == second_arg
	```
- `sys.exit(1)` will cause the exit code of the script to return 1, usually exit codes 0 represents a True or successful script while another number such as 1 2 etc would be a False or unsucessful script

#Bash Misc

- using the `echo` command with the `$?` arguement will return the exit code of the last run process
	```
	echo $?
	```
- using the `export` command will create a new enviornemt variable with the arguement given
	```
	export $VARIBLE = 'path_to_var'
	```

