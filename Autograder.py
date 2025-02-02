import argparse
import subprocess
import pandas as pd

def handle_inputs():
	parser = argparse.ArgumentParser(description = "Process necessary arguments")
	
	parser.add_argument("--classroom-ID", type = int,
						dest = "classroomID",
						help = "Github Classroom ID indicated by the download option", 
						required=True)
	parser.add_argument("--assignment", type = str,
						dest = "assignment",
						help = "Assignment name indicated on Canvas", 
						required=True)
	parser.add_argument("--github-file-name", type = str,
						dest = "githubFile",
						help = "Github classroom grades file", 
						required=True)
	parser.add_argument("--grade-file-name", type = str,
						dest = "gradeFile",
						help = "Canvas gradebook file", 
						required=True)
	parser.add_argument("--code-name", type = str,
						dest = "codeName",
						help = "Name of the program", 
						required=True)
	parser.add_argument("--compile-command", type = str,
						dest = "compileCommand",
						help = "Compilation commands", 
						required=True)
	# TODO: Convert this into list so multiple params can be tested
	parser.add_argument("--program-arguments", type = int, #nargs = "+", 
						dest = "programParameters",
						help = "Arguments for the program", 
						required=True)
	parser.add_argument("--show-grades", action = "store_true",
						dest = "showGrades",
						help = "Show students' grades")
	parser.add_argument("--store-grades", action = "store_true",
						dest = "storeGrades",
						help = "Store students' grades to Canvas gradebook")
						
	args = parser.parse_args()
	
	return args

# TODO: convert this into a separate file
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
	
def auto_grade(args):
	
	classroomID = args.classroomID
	assignment = args.assignment
	githubFile = args.githubFile
	gradeFile = args.gradeFile
	codeName = args.codeName
	compileCommand = args.compileCommand
	# TODO: Convert this into list so multiple params can be tested
	programParameters = args.programParameters
	showGrades = args.showGrades
	storeGrades = args.storeGrades
	
	# Put all reference outputs to a list
	correctAnswers = reference_code(programParameters)
	
	# Download students' repos
	classroomLink = ["gh", "classroom", "clone", "student-repos", "-a" f"{classroomID}"]
	_ = subprocess.run(classroomLink)
	
	# Separator
	print("\n\n " +' Run Tests '.center(70, '*') + "\n\n")
	
	# Read student's github information
	githubInfo = pd.read_csv(githubFile)
	assignmentName = githubInfo['assignment_name'][0]

	# Read grading sheet
	gradeSheet = pd.read_csv(gradeFile)

	# Get appropriate assignment column
	for column in gradeSheet.columns:
		if assignment in column:
			assignmentColumn = column

	# Set scores of the assignment
	fullScore = gradeSheet[f"{assignmentColumn}"][0]
	tempScore = 0
	
	# Loop through students' files and assign grades
	# or report students whose code is not correct
	for githubLink, studentID in zip(
		githubInfo['student_repository_name'], 
		githubInfo['roster_identifier']
	):
		for name, nmsuID in zip(
			gradeSheet['Student'], 
			gradeSheet['SIS Login ID']
		):
			if studentID == nmsuID:
				# TODO: modify to work with multiple params
				script = f"""{compileCommand} {assignmentName}-submissions/{githubLink}/{codeName} &&
							 ./test {programParameters}"""
				
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
				
					else:
						print(f"{name} Failed\nFolder name: {githubLink}\n")
				
				# Assign scores
				gradeSheet.loc[
					gradeSheet['Student'] == name,
					f"{assignmentColumn}"
				] = tempScore
				
				# Reset temp score
				tempScore = 0
	
	# Students who don't have a repo gets no points
	gradeSheet[f'{assignmentColumn}'] = gradeSheet[f'{assignmentColumn}'].fillna(0)
	
	# Show grades if requested
	if showGrades:		
		# Separator
		print("\n\n " +' Grades '.center(70, '*') + "\n\n")
		
		for i, j in zip(gradeSheet['Student'][1:], gradeSheet[f'{assignmentColumn}'][1:]):
			print(f"{i}'s score is {j}")
	
	# Store grades if requested
	if storeGrades:
		gradeSheet.to_csv(f"{gradeFile}", header = True, index = False)
		
		# Separator
		print("\n\n " +' Gradebook updated '.center(70, '*') + "\n\n")


if __name__ == "__main__":
	args = handle_inputs()
	auto_grade(args)
			
