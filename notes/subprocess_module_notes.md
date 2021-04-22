# subprocess module

## functions
- `subprocess.run(["sleep","3"])` takes a list with the first arguement being the name of the command and the next argument(s) being the arguments for that command or process.
when adding the capture_output arguement we can see the actual output of the process ie 
```
subprocess.run(["host","8.8.8.8"], capture_output = True)
```
- we can save the result of the subprocess.run function and we are returned a class object with usefull attributes
```
result = subprocess.run(["host","8.8.8.8], catpure_output = True)
result.returncode -> 0
result.stdout -> b'8.8.8.in-addr.arpa domain name pointer dns.google.\n'
result.stderr -> returns the error returned if an error occurs
``` 

- `decode` function will convert any non python 'byte' or b'this type of thing' string into a usable string. decode by default will return in UTF-8 code
```
print(result.stdout.decode().split())
```  


