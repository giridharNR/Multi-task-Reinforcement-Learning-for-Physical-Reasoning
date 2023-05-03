import math
import random
import json
import sys
from create_game import register_json_folder, register_json_str
import gym

MARKER_BALL = (0.6,0.75)
MEDIUM_FLOOR_0 = (0.1,-0.25)
MEDIUM_FLOOR_1 = (-0.7,-0.75)
GOAL_STAR = (-0.7, -0.75)
TARGET = (0.1, -0.25)
RADIUS = 0.3

def get_placement(centre, radius):
    # random angle
    alpha = 2 * math.pi * random.random()
    # random radius
    r = radius * math.sqrt(random.random())
    # calculating coordinates
    x = round(r * math.cos(alpha) + centre[0],2)
    y = round(r * math.sin(alpha) + centre[1],2)
    if x<-1 or x>1:
        if abs(-1-x)>abs(1-x):
            x = 0.9
        else:
            x = -0.9

    if y<-1 or y>1:
        if abs(-1-y)>abs(1-y):
            y = 0.9
        else:
            y = -0.9

    new_pos = (x, y)
    return new_pos

def read_custom_json(filename):
    custom_json_obj = json.load(open(filename))
    return custom_json_obj

def rewrite_json(custom_json_obj, new_name):
    new_marker_ball = get_placement(MARKER_BALL, RADIUS)
    new_medium_floor_0 = get_placement(MEDIUM_FLOOR_0, RADIUS)
    new_medium_floor_1 = get_placement(MEDIUM_FLOOR_1, RADIUS)
    new_target = get_placement(TARGET, RADIUS)
    new_goal = get_placement(GOAL_STAR, RADIUS)

    custom_json_obj["target"] = "["+str(new_target[0]) + ", " + str(new_target[1])+" + OFFSET]"
    custom_json_obj["goal"] = "["+str(new_goal[0]) + ", " + str(new_goal[1])+" +  OFFSET]"

    
    custom_json_obj["env"][0]["pos"] = [new_marker_ball[0], new_marker_ball[1]]
    custom_json_obj["env"][1]["pos"] = "["+str(new_target[0]) + ", " + str(new_target[1])+"]"
    custom_json_obj["env"][2]["pos"] = "["+str(new_goal[0]) + ", " + str(new_goal[1])+"]"

    custom_json_obj["name"] = new_name

    return custom_json_obj

def create_random_env(env_prefix, n):
    ans = read_custom_json("./examples/custom_json_2/level_custom.json")
    # register_json_folder('./random_envs')
    env_list = []

    for i in range(n):
        new_name = env_prefix+"CustomPush"+str(i)

        new_custom_json = rewrite_json(ans, new_name)

        # Serializing json
        json_object = json.dumps(new_custom_json, indent=4)
        
        # Writing to random envs
        # filename = "./random_envs/"+new_name+".json"
        # with open(filename, "w") as outfile:
        #     outfile.write(json_object)

        # create env
        register_json_str(json_object)
        env = gym.make('CreateLevel'+new_name+'-v0')
        env_list.append(env)

    return env_list

if __name__=='__main__':
    env = create_random_env(env_prefix="Two", n=5)