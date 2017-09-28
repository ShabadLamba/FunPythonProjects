__author__ = 'shabadlamba'
from random import shuffle

player_database = []
my_file= open("fifadata.rtf","r")
for line in my_file:
	player = line.split(" ")
	player[2] = player[2][0:2]
	player_database.append(player)
my_file.close()

def forwards_dist(forwards,teams):
	shuffle(teams)
	counter=1
	for i in range(len(forwards),len(forwards)+len(forwards)/3):
		if counter<3:
			for i,team in enumerate(teams):
				teams[i].append(forwards[len(forwards)-1])
				forwards.pop()
				counter+=1
		elif counter>3:
			for i,team in enumerate(teams):
				teams[i].append(forwards[len(forwards)-1])
				forwards.pop()
				counter-=1
	return teams

def midfielders_dist(midfielders,teams):
	shuffle(teams)
	counter=1
	for i in range(len(midfielders),len(midfielders)+len(midfielders)/3):
		if counter<3:
			for i,team in enumerate(teams):
				teams[i].append(midfielders[len(midfielders)-1])
				midfielders.pop()
				counter+=1
		elif counter>3:
			for i,team in enumerate(teams):
				teams[i].append(midfielders[len(midfielders)-1])
				midfielders.pop()
				counter-=1
	return teams

def defenders_dist(defenders,teams):
	shuffle(teams)
	counter=1
	for i in range(len(defenders),len(defenders)+len(defenders)/3):
		if counter<3:
			for i,team in enumerate(teams):
				teams[i].append(defenders[len(defenders)-1])
				defenders.pop()
				counter+=1
		elif counter>3:
			for i,team in enumerate(teams):
				teams[i].append(defenders[len(defenders)-1])
				defenders.pop()
				counter-=1
	return teams

def goalies_dist(goalies,teams):
	shuffle(teams)
	counter=1
	for i in range(len(goalies),len(goalies)+len(goalies)/3):
		if counter<3:
			for i,team in enumerate(teams):
				teams[i].append(goalies[len(goalies)-1])
				goalies.pop()
				counter+=1
		elif counter>3:
			for i,team in enumerate(teams):
				teams[i].append(goalies[len(goalies)-1])
				goalies.pop()
				counter-=1
	return teams

def distribute_team(lst):
	lst.sort(key=lambda x: x[2])
	count_forward = 0
	count_midfield = 0
	count_defence = 0
	count_goalie=0
	total=0
	average = 0
	forwards=[]
	defenders=[]
	midfielders=[]
	goalies=[]
	for i in lst:
		if i[1]=='f':
			count_forward += 1
			forwards.append(i)
		elif i[1]=='m':
			count_midfield+=1
			midfielders.append(i)
		elif i[1]=='d':
			count_defence+=1
			defenders.append(i)
		elif i[1]=='g':
			count_goalie+=1
			goalies.append(i)
	teams=[["1"],["2"],["3"]]
	teams=forwards_dist(forwards,teams)
	teams=midfielders_dist(midfielders,teams)
	teams=defenders_dist(defenders,teams)
	teams=goalies_dist(goalies,teams)
	fp=open("output.txt","w")
	for i in teams:
		for j in i:
			for k in j:
				fp.write(k)
				fp.write(" ")
			fp.write("\n")
	fp.close()		
distribute_team(player_database)

		


