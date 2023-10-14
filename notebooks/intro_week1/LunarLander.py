# %%
# Import the Gym library, which provides a wide range of environments for reinforcement learning
import gymnasium as gym
import numpy as np

# Create an environment for the LunarLander-v2 task(game), with rendering in a human-friendly mode
env = gym.make("LunarLander-v2", render_mode="human")

# Reset the environment and get the initial observation and info
observation, info = env.reset() #no particular seed

# Loop for a fixed number of time steps (1000 in this case)
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



