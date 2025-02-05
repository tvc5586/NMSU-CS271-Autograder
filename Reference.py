
# ===========================================
# Edit this file according to the assignments
# ===========================================


def reference_code(programParameters):

	# TODO: modify to take in multiple arguments
	
	triangle, square = "", ""
	
	# Create triangle
	for i in range(programParameters):
		for j in range(i + 1):
			triangle += "*"
		
		if i != programParameters - 1:
			triangle += "\n"

	# Create square
	for i in range(programParameters + 1):
		for j in range(programParameters + 1):
			if i % programParameters == 0 or j % programParameters == 0:
				square += "*"
			else:
				square += " "
		
		if i != programParameters:
			square += "\n"
	
	return [triangle, square]
