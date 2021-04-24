#Bash Commands

- `python_script.py > file_name` will redirect STDOUT to an output to a file (replace the file).
- `python_script.py >> file_name` will appends STDOUT to an ouptut to a file
- `python_script.py < file_with_error` will read the contents of a file to another
- `python_script.py < new_file.txt 2> error_file` will redirect the error output or STDERR to a file
- `echo "these are file contents" > seripuos_file.txt` 


## Pipes and Pipelines
- ```
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
``` 
gets contents of spider.txt file passed then to `tr` or translate action takes a " " into the character in the second parameter"\n" and replaces every space with a "\n". Then the sort command and sorts the contents alphabetically, sorted results are then passed to the uniq command with th -c flag displaying each match once and diplays number of times the match occured respectivley. Now this is passed to the sort command again with the -nr flag to sort results numerically and in reverse order then passed finally to the head command that prints the first 5 lines of a file.





## Misc
- 0 and 1 refer to the file descriptors for STDIN and STDOUT
  
