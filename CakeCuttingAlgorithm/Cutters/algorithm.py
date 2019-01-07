#Cake Cutting Algorithm


#dependencies
import random

def initialize_agents(n_agents):
	i=0
	unused_agent=[]
	while i<n_agents:
		unused_agent.append(i)
		i+=1
	return unused_agent


def rand_select_agent(available_agent):
	selected_agent_index=random.randint(0,available_agent.__len__()-1)
	available_agent.remove(selected_agent_index)
	return available_agent, selected_agent_index
	
	
