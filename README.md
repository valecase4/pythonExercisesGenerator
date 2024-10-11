# Python Exercises Generator

### Built with Flask Python Framework, HTML, CSS, JavaScript

This program consists of a random generator of Python Exercises.

### How it works

_src_ directory contains all the exercises.
Each exercise consists of a specific directory that contains its track (_.txt_ file) and its solution (_.py_ file).
The program chooses one of these directories (i.e., it chooses an exercise) randomly.
After that, the backend reads the content of the exercise track and sends it to the frontend.

Example:

ex_1/
    
    ex_1.py --> Python solution 
    ex_1.txt --> track of the exercise

### How the .txt file is structured
