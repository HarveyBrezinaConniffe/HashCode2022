from collections import namedtuple
import random

numContributors, numProjects = map(int, input("").split(" "))

Skill = namedtuple("Skill", ["name", "level"])
Person = namedtuple("Person", ["name", "skills"])
Project = namedtuple("Project", ["name", "days", "score", "bestBefore", "roles"])
Assignment = namedtuple("Assignment", ["name", "assignedRoles"])

people = []
projects = []

for i in range(numContributors):
	personName, numSkills = input("").split()
	skills = []
	for j in range(int(numSkills)):
		skillName, level = input("").split()
		skills.append(Skill(skillName, int(level)))
	people.append(Person(personName, skills))

for i in range(numProjects):
	projectName, days, score, bestBefore, numRoles = input().split(" ")
	days = int(days)
	score = int(score)
	bestBefore = int(bestBefore)
	numRoles = int(numRoles)
	roles = []
	for j in range(numRoles):
		skillName, level = input("").split()
		roles.append(Skill(skillName, int(level)))
	projects.append(Project(projectName, days, score, bestBefore, roles))

# Function that takes in the skills needed for a project and available people.
# Finds any subset of people that satisfy the skills requirement.
def findWorkableAssignment(roles, availablePeople):
	# Find all people that have skills at minimum level
	rolesToPeople = {}	
	for role in roles:
		if role not in rolesToPeople:
			rolesToPeople[role] = []
		minLevel = role.level
		for person in availablePeople:
			suitable = False
			for skill in person.skills:
				if skill.name == role.name and skill.level >= role.level:
					suitable = True
					break
			if suitable:
				rolesToPeople[role].append(person.name)
	# Check if any roles have no suitable people, If so we cannot have a valid list right now
	for role in rolesToPeople:
		if len(rolesToPeople[role]) == 0:
			return -1
	return rolesToPeople	

def isUnique(currentList):
	seenPeople = {}
	for person in currentList:
		if person in seenPeople:
			return False
		seenPeople[person] = 1
	return True

def genList(rolesToPeople):
	output = []
	counter = 0
	while True:
		if counter == 10:
			return -1
		for role in rolesToPeople:
			possiblePeople = rolesToPeople[role]
			person = random.choice(possiblePeople)
			output.append(person)
		counter += 1
		if isUnique(output):
			return output
	return -1

Assignment = namedtuple("Assignment", ["projectName", "roleNames"])
assignments = []

for project in projects:
	rolesToPeople = findWorkableAssignment(project.roles, people)
	if rolesToPeople == -1:
		continue
	assignmentList = genList(findWorkableAssignment(project.roles, people))
	if assignmentList == -1:
		continue
	assignments.append(Assignment(project.name, assignmentList))

print(len(assignments))
for assignment in assignments:
	print(assignment.projectName)
	print(" ".join(assignment.roleNames))
