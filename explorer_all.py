import sys
import os
import time

## importa classes
from environment import Env
from explorer_1 import Explorer_1
from explorer_3 import Explorer_3
from explorer_4 import Explorer_4
from explorer_2 import Explorer_2
from rescuer import Rescuer

def main(data_folder_name):
   
    # Set the path to config files and data files for the environment
    current_folder = os.path.abspath(os.getcwd())
    data_folder = os.path.abspath(os.path.join(current_folder, data_folder_name))

    
    # Instantiate the environment
    env = Env(data_folder)
    
    # config files for the agents
    rescuer_file = os.path.join(data_folder, "rescuer_config.txt")
    explorer_file = os.path.join(data_folder, "explorer_config.txt")
    
    # Instantiate agents rescuer and explorer
    resc = Rescuer(env, rescuer_file)

    # Explorer needs to know rescuer to send the map
    # that's why rescuer is instatiated before
    exp = Explorer_1(env, explorer_file, resc)
    exp2 = Explorer_2(env, explorer_file, resc)
    exp3 = Explorer_3(env, explorer_file, resc)
    exp4 = Explorer_4(env, explorer_file,resc)