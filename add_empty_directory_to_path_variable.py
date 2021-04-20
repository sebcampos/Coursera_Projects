import os
import subprocess

my_env = os.enviorn.copy() #creates a dictionary of env variables
my_env["PATH"] = os.pathsep.join(["/opt/add_empty_directory_to_path_variable/, my_env["PATH"])

result = subprocess.run(["add_empty_directory_to_path_variable"], env=my_env) 

