#Bash Commands

- `python_script.py > file_name` will redirect STDOUT to an output to a file (replace the file).
- `python_script.py >> file_name` will appends STDOUT to an ouptut to a file
- `python_script.py < file_with_error` will read the contents of a file to another
- `python_script.py < new_file.txt 2> error_file` will redirect the error output or STDERR to a file
- `echo "these are file contents" > seripuos_file.txt`
- `ps` returns a list of running process, if arguement ax is passed `ps ax` it will return all for the current computer
- `ping dest_arg` will send packet(s) to the designated argument 

- `arguement_file | grep 'string'` will return the line in arguemnt file containing the word string 

- `echo` prints message to standart output
- `date` returns date
- `file` returns file type
- `head` returns first ten lines and `tail` returns last ten
- `sort` sorts a file alphabetically by line
- `less` allows for a scrollable output
- `cut -d -f` for each line in a given file splits the line according to the given separator and prints the given fields starting from 1
- `who` retunrs the list of currently logged into the computer users

- `man` shows the manual page of the given command like help function

- `uptime` shows how long the computer has been running
- `free` shows the amount of unused memory on the current system 

## Pipes and Pipelines
- ```
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
``` 
gets contents of spider.txt file passed then to `tr` or translate action takes a " " into the character in the second parameter"\n" and replaces every space with a "\n". Then the sort command and sorts the contents alphabetically, sorted results are then passed to the uniq command with th -c flag displaying each match once and diplays number of times the match occured respectivley. Now this is passed to the sort command again with the -nr flag to sort results numerically and in reverse order then passed finally to the head command that prints the first 5 lines of a file.

- `ps ax | grep ping` lists currently running process, then ax lists all currently running on this comupter then grep filters the output by searching for the line with the word ping in it. then the number at the begining of this ping process can be used to kill the process from a different terminal window


## Misc
- 0 and 1 refer to the file descriptors for STDIN and STDOUT
- Ctrl-C == SIGINT shuts off program
- Ctrl-Z == SIGSTOP stops program and can be continued by typeing fg
- the kill command == SIGTERM and is a seperate program and must be run on a seperate terminal

```
kill <PID>
```
  
