# Notes for python os module
# Functions
- `os.getcwd()`
- `os.mkdir(new_dir)`
- `os.chdir(new_dir)`
- `os.listdir()`
- `os.remane(old_dir, new_dir)`
- `os.remove(filename)` removes a file not a directory unless directory is not empty
- `os.path.join(directory, item_in_directory)` creates a full path for crosee platform management
- `os.path.abspath(file_and_or_directory)` returns a string of the absolute path of the passed parameter
- `os.path.basename(file_and_or_file_path)` returns the last part or file in the given path
- `os.path.commonpath(paths)` returns the longest common subpath of each path name in the sequence path
- `os.path.getmtime(file)` returns a timestamp of when the file was last modified
- `os.environ.get(var_name,"")` will return the path the the enviorment variable passed, if none exist an empty string will be returned 
-  `os.pathsep.join(["new/path", my_env["PATH"])` will add to our path env according to the os


## Using datetime module and os module to read in a file time stamp
```
file_timestamp = os.getmtime(filename)
python_dt_object = datetime.datetime.fromtimestamp(file_timestamp)
```

## Moving files in python
```
os.rename(path,new_path)
```


## Iterating over a directory to check for sub directories
```
dir = 'current_directory'
for name in os.listdir(dir):
	fullname = os.path.join(dir, name)
	if os.path.isdir(fullname):
		print(f'{fullname} is a directory'
	else:
		print(f'{fullname} is a file')
```

