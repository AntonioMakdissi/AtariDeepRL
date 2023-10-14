import stable_baselines3
import gymnasium
import numpy as np
# import gym
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_atari_env
from ocatari.core import OCAtari



# # List all the available environments to see the correct name
# all_envs = list(gym.envs.registry.keys())
# for env_name in all_envs:
#     print(env_name)


# env = gym.make("AssaultNoFrameskip-v4", render_mode="rgb_array")

env = OCAtari("AssaultNoFrameskip-v4", mode="raw", render_mode="rgb_array") # set game
# Reset the environment and obtain the initial observation
# observation, info = env.reset()
# prevRam = None
# already_figured_out = []
# for i in range(1000):

#     ram_value = 9   # set here the RAM value

#     for b in range(0, 126):     # loop through the RAM
#         obs, reward, terminated, truncated, info = env.step(np.random.randint(0, 0))
#         print(b - 1)
#         env.set_ram(b, ram_value)
#         env.render()  #Render the environment (for visualization purposes)
#         #ipdb.set_trace()
        
# # Close the OCAtari environment
# env.close()

# # %%


# # Initialize the OCAtari environment for the "Assault" game
# env = OCAtari.OCAtari("Assault", mode="raw", render_mode="rgb_array")

# Reset the environment and obtain the initial observation
observation, info = env.reset()

# Loop through the RAM addresses
for ram_address in range(128):
    # Set a random RAM value (for demonstration)
    ram_value = np.random.randint(0, 255)
    
    # Print the RAM address and value for debugging
    print(f"RAM Address: {ram_address}, RAM Value: {ram_value}")
    
    # Set the RAM value for the specified address
    env.set_ram(ram_address, ram_value)
    
    # Render the environment (for visualization purposes)
    env.render()

# Close the OCAtari environment
env.close()



