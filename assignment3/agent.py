import json
import sys
import argparse

# First iteration
def init():
   init_dict = {
           "iterations": 1,
           "last_opponent_moves":[],
           "next_agent_moves":["silent","silent","silent","silent","silent","silent","silent","silent","silent","silent"],
   }
   first_agent_move = "silent"

   # Save data to disk
   save_data(init_dict)

   print(first_agent_move)

def agent_move(last_opp_move):
        
        # Read data from disk
        my_dict = read_data()
                
        # Determine the agent move
        itr = my_dict['iterations']
        nam = my_dict['next_agent_moves']
        lom = my_dict['last_opponent_moves']
        silent_count = 0
        scount_opponent = 0
        ccount_opponent = 0
        nam_stack = []
        lom_queue = []
        for item in lom:
            lom_queue.append(item)
        for itema in nam:
            nam_stack.append(itema)
            if (itema == "silent"):
               silent_count = silent_count + 1               

        if (itr >= 20):
            while (len(lom_queue) != 10):
                lom_queue.pop(0)
            for move in lom_queue:
                if (move == 'silent'):
                    scount_opponent + 1
                else:
                    ccount_opponent + 1

        if (len(nam_stack) == 0): 
           for x in range(5):
             nam_stack.append("confess")
           for x in range(5):
             nam_stack.append("silent")
        elif(silent_count == 0):
           pass
        elif (last_opp_move == "confess"): 
           while(len(nam_stack) > 0):
              nam_stack.pop()
           for x in range(10): 
              nam_stack.append("confess")

        lom_queue.append(last_opp_move)
        my_dict['last_opponent_moves'] = lom_queue
        my_dict['iterations'] = itr + 1
                                        
        # Return the agent_move 
        my_move = ''
        if (itr >= 20):
           my_move = nam_stack.pop()
           if (scount_opponent > ccount_opponent and my_move == 'silent'):
               my_move = 'silent'
           else:
               my_move = 'confess'
        else:
           my_move = nam_stack.pop()

        my_dict['next_agent_moves'] = nam_stack

        # Save data to disk
        save_data(my_dict)

        print(my_move)
     
def save_data(dictionary):
    json_obj = json.dumps(dictionary, indent = 4)
    with open('prgmdata.json', 'w') as fp:
        fp.write(json_obj) 
    fp.close()

def read_data():
    with open('prgmdata.json', 'r') as f:
       json_obj = json.load(f)      
    f.close()

    #return data
    return json_obj

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()
    if(args.last_opponent_move != 'zero' and args.init == None):
       agent_move(args.last_opponent_move) 
    else:
       init()
