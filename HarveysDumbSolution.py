from collections import namedtuple

numContributors, numProjects = map(int, input("").split(" "))

Skill = namedtuple("Skill", ["name", "level"])
Person = namedtuple("Person", ["name", "skills"])

people = []

for i in range(numContributors):
	personName, numSkills = input("").split()
	skills = []
	for j in range(int(numSkills)):
		skillName, level = input("").split()
		skills.append(Skill(skillName, int(level)))
	people.append(Person(personName, skills))

print(people)
