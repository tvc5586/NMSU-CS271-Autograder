# An autograder for CS271

## Introduction

**This repo is still under development!**

**At this point, the autograder only works with Lab 2!**

This is an autograder for NMSU CS271 course. It will automatically pull all students' repos from Github Classroom and compare the outputs of students' code with the correct one. Based on the results of the comparisons, it will automatically assign scores to each student.

## Requirements

This program requires you to have the [Github CLI Tool](https://github.com/cli/cli) installed.

After finishing installing the Github CLI Tool, you need to run `gh extension install github/gh-classroom` to install the classroom extension.

After finishing installing the extension, run `gh auth login` to authenticate your Github account.

The autograder requires `Python 3` and the following libraries to function:
- `pandas`

## How to run this program

You can run this autograder by using this command: `python3 Autograder.py --classroom-ID=<Github classroom ID> --assignment="<Assignment name>" --github-file-name="<Github classroom grades file>" --grade-file-name="<Canvas grades file>" --code-name="<Name of the program>" --compile-command="<Compile commands>" --program-arguments=<Arguments to the program>`

**All command-line arguments to this program are required for this program to run!**

## Command-line Arguments Explanation

|Command-line Argument|Explanation                                               |
|---------------------|----------------------------------------------------------|
|`--classroom-ID`     |ID provided by classroom's *Download Student Repos* option|
|`--assignment`       |Name of the assignment (e.g. Lab 1)                       |
|`--github-file-name` |Name of Github classroom's *Grades* file                  |
|`--grade-file-name`  |Name of Canvas's *Gradebook* file                         |
|`--code-name`        |Name of the program students need to complete             |
|`--compile-command`  |Necessary commands to compile students' code              |
|`--program-arguments`|Arguments used to run the compiled code                   |

## To-Do List

- Making testing students' code more comprehensive by modifying the autograder so that it can process multiple program arguments at the same time
- Convert the `reference_code` function into a separate file to facilitate modification
- Automatically deduct points from partially correct answers
- Automatically assign 0 to students who didn't submit

## Contact

If you have any questions, feel free to contact the following people

		Autograder creator: tvc5586@nmsu.edu
		Course instructor: joncook@nmsu.edu

