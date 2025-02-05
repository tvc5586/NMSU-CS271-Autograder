# An autograder for CS271

## Introduction

**This repo is still under development!**

**Update `Reference.py` and `Execution.py` according to the assignment requirements before using!**

This is an autograder for NMSU CS271 course. It will automatically pull all students' repos from Github Classroom and compare the outputs of students' code with the correct one. Based on the results of the comparisons, it will automatically assign a score to each student and update the *Gradebook* file accordingly.

## Requirements

~~This program requires the [Github CLI Tool](https://github.com/cli/cli).~~

~~After finishing installing the Github CLI Tool, run `gh extension install github/gh-classroom` to install the classroom extension.~~

~~After finishing installing the extension, run `gh auth login` to authenticate your Github account.~~

Github's CLI Tool has a bug that forbids it to update students' commits. Therefore, the current version uses `git` and `ssh clone` instead.

The autograder requires `Python 3` and the following libraries to function:
- `pandas`

## How to run this program

`Reference.py` contains the function used to produce the correct answer(s). `Execution.py` contains the function used to run students' code. **Before running the autograder, the user must update these two files to reflect the assignment's requirements!**

The user can run this autograder by using this command: `python3 Autograder.py --assignment="<Assignment name>" --github-file-name="<Github classroom grades file>" --grade-file-name="<Canvas grades file>" --code-name="<Name of the program>" --compile-command="<Compile commands>" --program-arguments=<Arguments to the program>`

## Command-line Arguments Explanation

Anything that is not optional is required to run the autograder.

|Command-line Argument|Explanation                                               |
|---------------------|----------------------------------------------------------|
|`--assignment`       |Name of the assignment (e.g. Lab 1)                       |
|`--github-file-name` |Name of Github classroom's *Grades* file                  |
|`--grade-file-name`  |Name of Canvas's *Gradebook* file                         |
|`--code-name`        |Name of the program students need to complete             |
|`--compile-command`  |Necessary commands to compile students' code              |
|`--program-arguments`|Arguments used to run the compiled code                   |
|`--show-grades`      |(Optional) Display grades on terminal                     |
|`--store-grades`     |(Optional) Saving grades to Canvas's *Gradebook* file     |

## To-Do List

- Making testing students' code more comprehensive by modifying the autograder so that it can process multiple program arguments at the same time

## Contact

If there are any questions, feel free to contact the following people

	Autograder creator: tvc5586@nmsu.edu
	Course instructor: joncook@nmsu.edu

