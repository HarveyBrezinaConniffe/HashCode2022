from collections import namedtuple

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
		if role.name not in rolesToPeople:
			rolesToPeople[role.name] = []
		minLevel = role.level
		for person in availablePeople:
			suitable = False
			for skill in person.skills:
				if skill.name == role.name and skill.level >= role.level:
					suitable = True
					break
			if suitable:
				rolesToPeople[role.name].append(person.name)
	return rolesToPeople

for project in projects:
	print("Finding suitable people list for project {}.".format(project.name))
	print(findWorkableAssignment(project.roles, people))
