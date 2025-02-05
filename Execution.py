
# ===========================================
# Edit this file according to the assignments
# ===========================================


import subprocess


def CLI_execution(compileCommand, githubLink, codeName, programParameters):
	# TODO: modify to work with multiple params
	script = f"""{compileCommand} {githubLink}/{codeName} &&
					         ./test {programParameters}"""

	# Get output
	result = subprocess.run(
		script, shell = True,
		capture_output = True,
		text = True)

	return str(result.stdout)
