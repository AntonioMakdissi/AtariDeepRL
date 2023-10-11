import stable_baselines3
import gymnasium as gym
import numpy as np

from stable_baselines3 import DQN

from ocatari.core import OCAtari

env = OCAtari("Assault", mode="raw", render_mode="rgb_array")  # set game
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

# # Reset the environment and obtain the initial observation
# observation, info = env.reset()

# # Loop through the RAM addresses
# for ram_address in range(128):
#     # Set a random RAM value (for demonstration)
#     ram_value = np.random.randint(0, 255)
    
#     # Print the RAM address and value for debugging
#     print(f"RAM Address: {ram_address}, RAM Value: {ram_value}")
    
#     # Set the RAM value for the specified address
#     env.set_ram(ram_address, ram_value)
    
#     # Render the environment (for visualization purposes)
#     env.render()

# # Close the OCAtari environment
# env.close()



