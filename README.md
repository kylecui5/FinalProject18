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

Sources include:
* PyGame Documentation
* StackOverflow Forums
* Python Documentation

Modules Used Include:
* JSON
* PyGame

Run Main.py to start the program.

*Note* The password for setting baseline drawings currently is
"holahola". It can be changed in line 186 of Main.py