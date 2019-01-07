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
from Cutters import algorithm as cutter


#format dataframe
n_cakecol, n_criteriacol=1,1
offset = n_cakecol + n_criteriacol
n_criteria = data.shape[0]
n_agents=data.shape[1]-offset


#split dataframe
Agent_evaluation = data.drop(['Criteria'],axis=1)
Total_value = Agent_evaluation.iloc[:,0]
Agent_evaluation = Agent_evaluation.drop(['Cake'],axis=1)


#setting up algorithm
available_agent = cutter.initialize_agents(n_agents)
available_agent, selected_agent=cutter.rand_select_agent(available_agent)


#Evaluating Selected Agent Score
Selected_evaluation=Agent_evaluation.iloc[:,selected_agent]
Selected_Sum_Index=np.matmul(Total_value,Selected_evaluation)

#Dividing Sum Index by number of Agents
Splitted_Sum_Index=Selected_Sum_Index/n_agents
print Splitted_Sum_Index


