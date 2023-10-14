import stable_baselines3
import gymnasium as gym
# import gym
import numpy as np
from stable_baselines3 import DQN
from stable_baselines3.dqn import CnnPolicy
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3 import DQN
import gym_wrappers
from ocatari.core import OCAtari
#########################################
hyperparams = {
    "buffer_size": 1000,  # old buffer_size=100000 had memory problems
    "learning_rate": 1e-4,
    "batch_size": 32,
    "learning_starts": 100000,
    "target_update_interval": 1000,
    "train_freq": 4,
    "gradient_steps": 1,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.01,
    "optimize_memory_usage": False
}
##########################################
#initialize env 
#env = OCAtari("AssaultNoFrameskip-v4", n_envs=4, mode="raw", render_mode="rgb_array")
# mode="raw": Provides raw pixel data, which is useful for methods like convolutional neural networks (CNNs) for image processing.

# mode="ram": Provides access to the game's memory (RAM) content. You can read and write values to specific RAM addresses, which can be useful for debugging and memory manipulation.

# mode="ram_raw": Combines both raw pixel data and RAM access, allowing you to interact with both the game screen and its memory.
env = OCAtari("AssaultNoFrameskip-v4", mode="raw", render_mode="human")  # set game
# Get observation space information
# height, width, channels = env.observation_space.shape
actions = env.action_space.n
print(f"available actions: {actions}")  # nbr of actions

# Stack 4 frames
# env = VecFrameStack(env, n_stack=4)


env = OCAtari("Assault-v4", mode="raw", render_mode="rgb_array")

env = GymAtariWrapper(env)

observation, info = env.reset()

model = DQN(CnnPolicy, env, verbose=0)

# # Train the model
# model.learn(total_timesteps=10_000)

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



# ##############################################RANDOM
for _ in range(1000):
    # Choose a random action from the action space as an agent's policy
    action = env.action_space.sample()

    # Take a step in the environment using the selected action
    observation, reward, terminated, truncated, info = env.step(action)

    # Check if the episode is terminated (done) or truncated (timed out)
    if terminated or truncated:
        # If the episode is over, reset the environment for a new episode
        observation, info = env.reset()

# Close the environment when the loop is done
env.close()