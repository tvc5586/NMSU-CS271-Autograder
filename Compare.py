
# ===========================================
# Edit this file according to the assignments
# ===========================================


import subprocess


def compare_answers(
	compileCommand, githubLink, codeName, programParameters,
	correctAnswers, fullScore
):
	tempScore = 0

	# TODO: modify to work with multiple params
    #
    # At this point, the below string is designed
    # to work with Makefile
    #
    # Modifify if necessary
	script = f"""cd {githubLink} &&
               {compileCommand}"""

	# Get output
	result = subprocess.run(
		script, shell = True,
		capture_output = True,
		text = True)

	output = str(result.stdout)
	
	# Compare answers
	for answer in correctAnswers:
		if answer in output:
			tempScore += fullScore / len(correctAnswers)

	return round(tempScore, 5)
