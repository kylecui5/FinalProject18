# Intro to Programming Final Project - Fall 2018

Kyle's "Slow, Scribble"

Based on Google's "Quick, Draw!", this game serves to identify a
simple drawing drawn by the user from a short list of possible
drawings. Possible drawings include an apple, a bird, a candle,
a clock, a coffee mug, a finger, a moustacahe, and a smiley face.
It guesses the drawing by comparing the coordinates drawn with a
set of baseline drawings and choosing the baseline drawing that
has the least average distance to a closest point per coordinate.
It does not use machine learning or artificial intelligence to
change future guesses based on previous user drawings.

Flowchart:
https://drive.google.com/file/d/1deZ3Jm3pB9oWFWz2s2s2ZK3CEoX_Jnfh/view?usp=sharing

Sources include:
* PyGame Documentation https://www.pygame.org/docs/
* StackOverflow Forums
* Python Documentation https://docs.python.org/3.7/tutorial/index.html

Modules Used Include:
* JSON
* PyGame

Run Main.py to start the program.

*Note* The password for setting baseline drawings currently is
"holahola". It can be changed in line 186 of Main.py