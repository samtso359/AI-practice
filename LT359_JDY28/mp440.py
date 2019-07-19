import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue 
'''
global queue

def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    global queue
    if initialize == True:
        queue = []
    queue.append((node_id, parent_node_id))
    return queue

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    global queue
    if len(queue)>0:
        return False
    else:
        return True

'''
BFS pop from queue
'''
def pop_front_BFS():
    global queue
    (node_id, parent_node_id) = (0, 0)
    temp = queue[0]
    del queue[0]
    return temp

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    global queue
    if initialize == True:
        queue = []
    queue.append((node_id, parent_node_id))
    return queue


'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    global queue
    if len(queue) > 0:
        return False
    else:
        return True

'''
DFS pop from queue
'''
def pop_front_DFS():
    global queue
    (node_id, parent_node_id) = (0, 0)
    temp = queue[len(queue)-1]
    del queue[len(queue)-1]
    return temp

'''
UC add to queue 
'''

global id_cost

def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    global queue
    global id_cost

    if initialize == True:
        queue = []
        id_cost ={}
    if len(queue) ==0:
        queue.append((node_id, parent_node_id))
        id_cost[node_id] = cost

    else:
        for i in range(len(queue)):
            #print(id_cost)

            if id_cost.get(queue[i][0])>= cost:
                queue.insert(i, (node_id, parent_node_id))
                id_cost[node_id] = cost

            else:
                queue.insert(i + 1, (node_id, parent_node_id))
                id_cost[node_id] = cost


    return queue


'''
UC add to queue 
'''
def is_queue_empty_UC():
    global queue
    if len(queue) > 0:
        return False
    else:
        return True

'''
UC pop from queue
'''
def pop_front_UC():
    global queue
    (node_id, parent_node_id) = (0, 0)
    temp = queue[0]
    del queue[0]
    return temp

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    global queue
    global id_cost

    if initialize == True:
        queue = []
        id_cost = {}
    if len(queue) == 0:
        queue.append((node_id, parent_node_id))
        id_cost[node_id] = cost

    else:
        for i in range(len(queue)):
            #print(id_cost)

            if id_cost.get(queue[i][0]) >= cost:
                queue.insert(i, (node_id, parent_node_id))
                id_cost[node_id] = cost

            else:
                queue.insert(i + 1, (node_id, parent_node_id))
                id_cost[node_id] = cost

    return queue

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    global queue
    if len(queue) > 0:
        return False
    else:
        return True

'''
A* pop from queue
'''
def pop_front_ASTAR():
    global queue
    (node_id, parent_node_id) = (0, 0)
    temp = queue[0]
    del queue[0]
    return temp

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    for x in range(n):
        state.append(random.randint(1, n))

    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    for x in range(0, len(state)):
        for y in range(x+1, len(state)):
            if(state[x]==state[y]):
                #print (str(x) + "," + str(y))
                number_attacking_pairs = number_attacking_pairs + 1
            if(state[x]==state[y]+y-x):
              #  print (str(x) + "," + str(y))
                number_attacking_pairs = number_attacking_pairs + 1
            if (state[x] == state[y]-y+x):
             #   print (str(x) + "," + str(y))
                number_attacking_pairs = number_attacking_pairs + 1



    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
    final_state = []
    temp = comp_att_pairs(state);
    final_state = state
    if (temp == 0):
        return final_state
    for x in range(0, len(state)):
        for y in range(1, len(state)+1):
            if(state[x] != y):
                #print (str(x) + "," + str(y))
                tempstate = list(state)
                tempstate[x] = y
                #print ("tempstate  " + str(tempstate))
                i = comp_att_pairs(tempstate)
                if(i < temp):
                    temp = i
                    final_state = tempstate
                    #print ("final_state" + str(final_state))
    # Your code here
    return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = []
    state = get_rand_st(n)
    #print state
    final_state = list(state)
    while (comp_att_pairs(final_state) != 0):
        #print comp_att_pairs(final_state)
        new_state = hill_descending(final_state, comp_att_pairs)
        #print ("new_state: " + str(new_state))
        if (final_state == new_state):
            #print ("getting new state")
            final_state = get_rand_st(n)
        else:
            #print ("updating fs")
            final_state = list(new_state)
            #print ("new fs: " + str(final_state))
    # Your code here
    #print comp_att_pairs(final_state)
    return final_state






