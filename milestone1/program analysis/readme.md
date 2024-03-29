# Workspace

## python code instruction

### create codeql database
move to the directory with python code (in .py file) and use command
```
codeql database create --language=python --source-root <ur python code> <new codeql db>
```

After running the code a new folder will appear named "new codeql db" with all required files


### run and visualize control flow
copy the py_control_flow.ql to the directory with your codeql database and run
```
codeql database analyze <new codeql db> ./py_control_flow.ql --format=dot --output=<py control visualization...>
```
to rerun the ql file use this one:
```
codeql database analyze --rerun <new codeql db> ./py_control_flow.ql --format=dot --output=<py control visualization...>
```
without --rerun option codeql won't automatically rerun


A "py control visualization..." folder containing a null.dot file will appear if you do it correct. To visualize the result, simply:
```
dot -Tpng ./<py control visualization...>/null.dot -o <your png graph here..> 
```

And a png file with name "your png graph here.." will appear in your working directory.


### run and visualize data flow
copy the py_data_flow.ql to the directory with your codeql database and run
```
codeql database analyze <new codeql db> ./py_data_flow.ql --format=dot --output=<py data visualization...>
```
to rerun the ql file use this one:
```
codeql database analyze --rerun <new codeql db> ./py_data_flow.ql --format=dot --output=<py data visualization...>
```
without --rerun option codeql won't automatically rerun


A "py data visualization..." folder containing a null.dot file will appear if you do it correct. To visualize the result, simply:
```
dot -Tpng ./<py data visualization...>/null.dot -o <your png graph here..> 
```

And a png file with name "your png graph here.." will appear in your working directory.

## Java code instruction
### First: Create a CodeQL Database:
To create a CodeQL database, you can use the following command:
```
codeql database create --language=java --source-root /path/to/source/code/root  /path/to/ql_database
```

### Second: Install CodeQL Dependencies for Java Code:
The specific dependencies are written in the qlpack.yml
Use codeql pack install commands to install specific dependencies.

### Third: Analyze the CodeQL database by using command like:
```
codeql database analyze "/path/to/codeql_database" “path/to/xxx.ql”--format=dot --output=/output/path
```
In this command, replace /path/to/codeql_database with the path to your CodeQL database, and replace path/to/xxx.ql with the path to the CodeQL query you want to run. The --format=dot option specifies that the output should be in DOT format, which is a plain-text graph representation. Finally, the --output=/output/path option specifies where to save the output DOT file.

### Finally: Visualize the codeql output dot file
```
dot -Tpng ./<py data visualization...>/null.dot -o <your png graph here..> 
```
In this command, replace <path-to-your-dot-file>.dot with the path to the DOT file generated by CodeQL, and replace <path-to-your-output-png-file>.png with the path where you want to save the output PNG file. This command generates a graphical representation of the CodeQL analysis results.

By following these steps, you can analyze your Java code with CodeQL and visualize the results to gain insights into your codebase.


