#implementation of discrete and bounded envy-less cake-cutting algorithm by Sin Yong, Teng


#import data
import pandas as pd
import os
path=os.getcwd()
data = pd.read_csv(path+"\Data\Cake.csv")

print(data)


#algorithm dependencies
import random
import numpy as np
import pandas as pd


#format dataframe
n_cakecol, n_criteriacol=1,1
offset=n_cakecol + n_criteriacol
n_criteria=data.shape[0]
n_agents=data.shape[1]-offset

print n_criteria,n_agents


def initialize_agents(n_agents):
	i=0
	unused_agent=[]
	while i<n_agents:
		unused_agent.append(i)
		i+=1
	return unused_agent

print(initialize_agents(n_agents))








		



def choose_cutter():
	''''''
	