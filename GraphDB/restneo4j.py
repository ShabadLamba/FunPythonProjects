from neo4j.v1 import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "Plmokn1234."))

def create_nodes(cypher_query,valid_states):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	for states in range(0,len(valid_states)):
        		for record in tx.run(cypher_query,rpolicemen=valid_states[states]['rpolicemen']\
        			,rprisoners=valid_states[states]['rprisoners'],lpolicemen=valid_states[states]['lpolicemen'],\
        			lprisoners=valid_states[states]['lprisoners']):
        			print(record)	

def create_relationships(cypher_query,current_state,valid_states,position_of_boat):
	print current_state
	with driver.session() as session:
		with session.begin_transaction() as tx:
			for states in range(0,len(valid_states)):
				for record in tx.run(cypher_query,position_of_boat=position_of_boat,lpolicemen2=valid_states[states]['lpolicemen']\
        			,lprisoners2=valid_states[states]['lprisoners'],lpolicemen1=current_state['lpolicemen'],\
        			lprisoners1=current_state['lprisoners']):
					print(record)	

# print_friends_of("LAMBA")
