# Python Exercises Generator

### Built with Flask Python Framework, HTML, CSS, JavaScript

This program consists of a random generator of Python Exercises.

### How it works

_src_ directory contains all the exercises.

First, implemented a blueprint view using a test exercise. You can find it at test/exercise.txt

This file is structured as follow:

File contains a given input for the exercise (i.e., a dictionary). This part should displayed in a different way in the frontend
since it represents Python Code. Therefore, each line that contains Python code within the file starts with the _*py*_ operator.
To better represent Python Code in the frontend, each line contains _*tab*_ operator. This operator is converted to 4 whitespaces in the frontend using Jinja. 

Jinja is used to render the frontend based on the content of each line within the input file.

Example: 
Consider this line: 

*py**tab*"first_name": "Valerio",

The backend knows that's Python Code since the presence of _*py*_ operator. 
Then, the backend knows that 4 whitespace are required since the presence of *_tab_* operator.

Other operators within the file:

- _*copy*_: it means that this line contains a button "Copy" in the frontend. If a given input (i.e., Python Code) exists, user can copy it by clicking this button and paste it in his code editor to solve the exercise.