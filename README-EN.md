## A Life of Logic Solver/Helper

### Game Introduction

A Life of Logic is a sudoku-like blocks filling puzzle game, which is provided on the [App Store](https://apps.apple.com/us/app/a-life-of-logic/id1329455663) around the world. The rule is pretty simple, player has to fill out all the blocks, meanwhile following three basic rules:

* No 3 connected same numbers (like 0 - 0 - 0).
* There must be same amount of 0s and 1s in a row or a column.
* There shouldn't be any same rows or columns.



![Sample](sample.jpg)



After getting puzzled by a level in Milestone 14, I decided to write a python script to help me infer these numbers, later on this script became even capable of solving some puzzles out.

The script however is not very calculate-effective. It uses many repeating codes just to enumerate every rows and columns. However since it doesn't require too many calculations I'm too lazy to optimize it :D.

### Usage

Edit the variable `block` to your puzzle, use "X"  to represent blanks. Like the example provided in the script, load your puzzle into a paragraph, then run the script.

```python
block = '''X1XXXX1XX1
XXXX1XX0XX
XX1XXXXXXX
XXXXXXXXXX
XX11XX0X1X
0XXXXXXXX0
X1XXXX0XXX
X1XXXXXXXX
XXXX11XXX1
0X1XX1X0XX''' #A sample of 10x10 puzzle
```

### Basic Principle

#### Step 1: Simple Filling

The script will first satisfy rule 1 and rule 2. Everytime Function `huajian()` runs, which is the Chinese of the word simplify, it fills the numbers according to the following rules:

* If X is between two same numbers, then fill X to its opposite number. (Function `jia()`)
* If X is next to two same numbers, then fill X to its opposite number. (Function `lin()`)
* If there is only 1 or 0 left to fill, then fill the entire row or column with the number. (Function `hlc()`)
* Sometimes, there are three blanks left, and if you don't follow a specific rule to fill those numbers, you ended up violating rule 1, so the script will fill one number in the right way, and left one 1 and one 0 to fill. (Function `bu()`)

Repeat these oprerations, until the result doesn't change, or it already filled the entire map (for some easy puzzles).

#### Step 2: Enumerating

Some puzzles can't be fully solved only by step 1, so next step we will have to enumerate. Of course, you could add an input() or some other code before the while True in around Line 180 to stop it beforehand. Then this script will just fill some easy blanks for you.

In enumerating process, the script will fill every blank with 0, then it will run a function to detect if it violates the rule (Function `chacuo()`), like these violations:

* Three same numbers connected (checked by four ifs)
* After filling according to the rules, the amount of 0s and 1s are not the same. (checked by two ifs)
* After filling according to the rules, there are some same rows or columns. (checked by a for loop with two ifs)

If these happens, chacuo() will return 1, the script will rollback its guess, and output 'Impossible'. Since not 0 then 1, it will fill 1 to this blank. Then, loop until the result doesn't change.

#### Step 3:

There's no step 3, 2 steps already solve many puzzles. Example provided in the script has 78 'X's, but the script is still capable of solving it. If somehow it didn't, it's because everytime it enumerate one blank to 0, without changing others. You could do some manual guessing at that time, and use this script to help you infer the rest, hopefully you will get the final answer.



Suggestions and edits are warmly welcome.