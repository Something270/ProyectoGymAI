import gym
import preprocess_frame as ppf
import numpy as np


#Iniciamos un nuevo juego, sin memoria de juegos anteriores

def initialize_new_game(name, env, agent):
    
    env.reset()
    starting_frame = ppf.resize_frame(env.step(0)[0])

    dummy_action = 0
    dummy_reward = 0
    dummy_done = False
    for i in range(3):
        agent.memory.add_experience(starting_frame, dummy_reward, dummy_action, dummy_done)

#Creamos el ambiente del emulador

def make_env(name, agent):
    env = gym.make(name,)
    return env

#Actualizacion de timesteps y pesos hasta que termine el juego.

def take_step(name, env, agent, score, debug):
    

    agent.total_timesteps += 1
    if agent.total_timesteps % 50000 == 0:
      agent.model.save_weights('recent_weights.hdf5')
      print('\nWeights saved!')


    next_frame, next_frames_reward, next_frame_terminal, info = env.step(agent.memory.actions[-1])
    

    next_frame = ppf.resize_frame(next_frame)
    new_state = [agent.memory.frames[-3], agent.memory.frames[-2], agent.memory.frames[-1], next_frame]
    new_state = np.moveaxis(new_state,0,2)/255 #We have to do this to get it into keras's goofy format of [batch_size,rows,columns,channels]
    new_state = np.expand_dims(new_state,0) #^^^
    

    next_action = agent.get_action(new_state)


    if next_frame_terminal:
        agent.memory.add_experience(next_frame, next_frames_reward, next_action, next_frame_terminal)
        return (score + next_frames_reward),True

    #Agregamos la experiencia a la memoria

    agent.memory.add_experience(next_frame, next_frames_reward, next_action, next_frame_terminal)

    if debug:
        env.render()

    if len(agent.memory.frames) > agent.starting_mem_len:
        agent.learn(debug)

    return (score + next_frames_reward),False

#Despues de game over, iniciamos nuevo juego

def play_episode(name, env, agent, debug = False):
    initialize_new_game(name, env, agent)
    done = False
    score = 0
    while True:
        score,done = take_step(name,env,agent,score, debug)
        if done:
            break
    return score
