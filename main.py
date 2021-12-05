import the_agent
import environment
import matplotlib.pyplot as plt
import time
from collections import deque
import numpy as np

# rom para entrenar
name = 'PongDeterministic-v4'


#enviroment para entrenar

agent = the_agent.Agent(possible_actions=[0,2,3],starting_mem_len=50000,max_mem_len=750000,starting_epsilon = 1, learn_rate = .00025)
env = environment.make_env(name,agent)

last_100_avg = [-21]
scores = deque(maxlen = 100)
max_score = -21


env.reset()

#Pre visualizaciones y resumen de cada episodio entrenado

for i in range(1000000):
    timesteps = agent.total_timesteps
    timee = time.time()
    score = environment.play_episode(name, env, agent, debug = True) #set debug to true for rendering
    scores.append(score)
    if score > max_score:
        max_score = score

    print('\nEpisode: ' + str(i))
    print('Steps: ' + str(agent.total_timesteps - timesteps))
    print('Duration: ' + str(time.time() - timee))
    print('Epsilon: ' + str(agent.epsilon))

