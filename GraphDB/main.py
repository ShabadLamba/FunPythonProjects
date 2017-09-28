from restneo4j import create_nodes,create_relationships
from moves import *

"""
Basic Rules:

1. Always equal number of poilcemen and prisons
2. Problem always starts with all of them being on the same side
3. Boat can carry 1 or 2 passengers at a time. 
4. Boat cannot go from one shore to other without any passengers
5. Prisoners cannot overnumber policemen at any time.

"""

current_state = {'rpolicemen':0,'rprisoners':0,'lpolicemen':0,'lprisoners':0}

def main(num_of_policemen,num_of_prisioners):
	current_state['lpolicemen'] = num_of_policemen
	current_state['lprisoners'] = num_of_prisioners
	position_of_boat = 'left'
	
	# while(current_state['lprisoners'] != 0 or current_state['lpolicemen'] != 0):
	
	list_of_possible_states = dumb_generator(current_state,position_of_boat)
	list_of_valid_states = dumb_tester(list_of_possible_states)
	"""cypher = "create(x: prop{ lpolicemen:{lpolicemen},lprisoners:{lprisoners},rpolicemen:{rpolicemen},rprisoners:{rprisoners}})"\
			"return x"
	create_nodes(cypher,list_of_valid_states)"""

	cypher_relationship = "match(n:prop)"\
						  "WHERE n.lprisoners = {lprisoners1} and lpolicemen={lpolicemen1}"\
							"match(m:prop)"\
							"WHERE m.lprisoners = {lprisoners2} and m.lpolicemen={lpolicemen}"\
							"create(n)-[:{boat_position}]->(m)"\
							"return n,m"

	create_relationships(cypher,current_state,list_of_valid_states,position_of_boat)
	print list_of_valid_states	
		

# def smart_generator():

def dumb_generator(cstate,boat_position):
	list_of_possible_states = []
	current_state = dict(cstate)
	if boat_position == 'left':
		try:
			list_of_possible_states.append(move_one_policemen_lr(dict(current_state)))
			
			list_of_possible_states.append(move_one_prisioner_lr(dict(current_state)))
			
			list_of_possible_states.append(move_two_policemen_lr(dict(current_state)))

			list_of_possible_states.append(move_two_prisioner_lr(dict(current_state)))

			list_of_possible_states.append(move_one_policemenandprisioner_lr(dict(current_state)))

		except:
			if current_state['lpolicemen'] == 0:
				if current_state['lprisoners'] > 1:

					list_of_possible_states.append(move_one_prisioner_lr(dict(current_state)))

					list_of_possible_states.append(move_two_prisioner_lr(dict(current_state)))

				else:

					list_of_possible_states.append(move_one_prisioner_lr(dict(current_state)))

			elif current_state['lprisoners'] == 0:
				if current_state['lpolicemen'] > 1 :

					list_of_possible_states.append(move_one_policemen_lr(dict(current_state)))

					list_of_possible_states.append(move_two_policemen_lr(dict(current_state)))

				else:

					list_of_possible_states.append(move_one_policemen_lr(dict(current_state)))

	if boat_position == 'right':
		try:
			list_of_possible_states.append(move_one_policemen_rl(dict(current_state)))
			list_of_possible_states.append(move_one_prisioner_rl(dict(current_state)))
			list_of_possible_states.append(move_two_policemen_rl(dict(current_state)))
			list_of_possible_states.append(move_two_prisioner_rl(dict(current_state)))
			list_of_possible_states.append(move_one_policemenandprisioner_rl(dict(current_state)))
		except:
			if current_state['lpolicemen'] == 0:
				if current_state['lprisoners'] > 1 :
					list_of_possible_states.append(move_one_prisioner_rl(dict(current_state)))
					list_of_possible_states.append(move_two_prisioner_rl(dict(current_state)))
				else:
					list_of_possible_states.append(move_one_prisioner_rl(dict(current_state)))
			elif current_state['lprisoners'] == 0:
				if current_state['lpolicemen'] > 1 :
					list_of_possible_states.append(move_one_policemen_rl(dict(current_state)))
					list_of_possible_states.append(move_two_policemen_rl(dict(current_state)))
				else:
					list_of_possible_states.append(move_one_policemen_rl(dict(current_state)))
	return list_of_possible_states

# def smart_tester():

def dumb_tester(list_of_states):
	for state in range(len(list_of_states)-1,-1,-1):
		if  (list_of_states[state]['rpolicemen']>0 and list_of_states[state]['rpolicemen'] < list_of_states[state]['rprisoners']) or \
		   (list_of_states[state]['lpolicemen']>0 and list_of_states[state]['lpolicemen']<list_of_states[state]['lprisoners']):
			list_of_states.remove(list_of_states[state])
	return list_of_states



main(3,3)