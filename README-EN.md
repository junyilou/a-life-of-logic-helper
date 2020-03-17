## A Life of Logic Solver/Helper

### Game Introduction

A Life of Logic is a sudoku-like blocks filling puzzle game, which is provided on the [App Store](https://apps.apple.com/us/app/a-life-of-logic/id1329455663) around the world. The rule is pretty simple, player has to fill out all the blocks, meanwhile following three basic rules:

* No 3 connected same numbers (like 0 - 0 - 0).
* There must be same amount of 0s and 1s in a row or a column.
* There shouldn't be any same rows or columns.



![Sample](sample.jpg)



After getting puzzled by a level in Milestone 14, I decided to write a python script to help me infer these numbers, later on this script became even capable of solving some puzzles out.

The script however is not very calculate-effective. It uses many repeating codes just to enumerate every rows and columns. However given the small amount of computation I'm too lazy to optimize it :D.

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

Some puzzles can't be fully solved only by step 1, so next step we will have to enumerate. Of course, you could add an input() or some other code before the while True in around Line 180 to stop it beforehand. Then this script will help you fill in some of the more obvious blanks without performing any enumerations.

After entering the enumuration phase, each unknown blank will be filled with 0, then an error checking function will be performed to analyze whether filling the 0 causes violations,  (Function `chacuo()`), for example:

* Three same numbers connected (checked by four ifs)
* After filling according to the rules, the amount of 0s and 1s are not the same. (checked by two ifs)
* After filling according to the rules, there are some same rows or columns. (checked by a for loop with two ifs)

In the above cases, chacuo() will return 1, which will cause the function to rollback its guess and output 'Impossible'. Since now 0 can't be filled, then only can 1, so the blank will be filled to 1. So on, loop until the result doesn't change.

#### Step 3:

There's no third step. The above 2 steps already solve many puzzles before Milestone 16. If somehow it didn't, it's because each enumeration only enumerate one blank to 0, without changing others. You could do some manual guessing at that time, and use this script to help you infer the rest, hopefully you will get the final answer.

I'm planning on updating my script so it's capable of enumerating two 0s or two 1s at the sametime, after some tests it proves this could solve every puzzle in Milestone 16. (I haven't unlock harder levels yet, haha).



Algorithm improvements and any suggestions are warmly welcome.