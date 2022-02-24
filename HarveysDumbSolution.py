from collections import namedtuple

numContributors, numProjects = map(int, input("").split(" "))

Skill = namedtuple("Skill", ["name", "level"])
Person = namedtuple("Person", ["name", "skills"])
Project = namedtuple("Project", ["name", "days", "score", "bestBefore", "roles"])

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

print(people)
print()
print(projects)
