import random
import os
import time
import math

def to_binary_string(arr: bool) -> str:
    if(len(arr) == 1):
        return str(int(arr[0]))
    else:
        return str(int(arr[0])) + to_binary_string(arr[1:])
        
def to_num(arr):
    return str(int(to_binary_string(arr),2))

def seed(arr):
    if(len(arr) == 1):
        return to_binary_string(arr[0])
    else:
        return to_binary_string(arr[0]) + seed(arr[1:])

def valid_ind(arr,y,x):
    if (x >= 0 and x < len(arr[0])) and (y >= 0 and y < len(arr)):
        return True
    else:
        return False
        
def pprint(arr):
    for i in range(len(arr)):
        print("\n")
        for j in range(len(arr[0])):
            print(str(arr[i][j]) + " ",end = "")
    print("\n")

def random_bool():
    return False if random.randrange(0,25) > 1 else True

def get_alive(arr,y,x):
    # y = 1
    # x = 0
    num_alive = 0
    
    # check top row
    for i in range(x - 1,x + 2):
        if valid_ind(arr,y - 1,i) and arr[y - 1][i]:

            num_alive = num_alive + 1
        
    # check either side
    if valid_ind(arr,y ,x - 1) and arr[y][x - 1]:

        num_alive = num_alive + 1
    if valid_ind(arr,y ,x + 1) and arr[y][x + 1]:
        
        num_alive = num_alive + 1
        
    # check bottom row
    for i in range(x - 1,x + 2):
        if valid_ind(arr,y + 1,i) and arr[y + 1][i]:
            num_alive = num_alive + 1
        
    return num_alive

def generate_frame(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # temp optimization (I think?) just want to skip the value if it
            # and all of its neighbors are dead. Then we know nothing will happen!
            #if(arr[i][j] == False and get_alive(arr,i,j) == 0):
                #continue
            if(arr[i][j] == True and get_alive(arr,i,j) <= 1):
                arr[i][j] = False
            elif(arr[i][j] == True and get_alive(arr,i,j) in (2,3)):
                arr[i][j] == True
            elif(arr[i][j] == False and get_alive(arr,i,j) == 3):
                arr[i][j] = True
            elif(arr[i][j] == True and get_alive(arr,i,j) >= 4):
                arr[i][j] = False
            
    return arr
                



def mask_val(val):
    if val:
        return "*"
    # solid ascii block instead of asterisk
        #return "\u2588"
    else:
        return "\u2800"
        #return "\u246C1"

    
def mask_arr(arr):
    local_arr = []
    for x in arr:
        local_arr.append(list(map(mask_val,x)))
    return local_arr

def to_arr_known(seed: str,width: int, height: int):
    if len(seed) != width*height:
        return "this seed does not match the number of elements in your array!"
    
    my_arr = []
    temp_list = []

    for i in range(height):

        temp_list = []

        # need these values on first iteration, can't cut them
        if i != 0:
            seed = seed[width:]
        my_arr.append(temp_list)

        
        for j in range(width):
            temp_list.append(True if seed[j:j+1] == '1' else False)
           

            
    return my_arr


def to_arr_known_uncompress(seed: str,width: int, height: int):
    if len(seed) != width*height:
        return "this seed does not match the number of elements in your array!"
    
    my_arr = []
    for i in range(height):

        temp_list = []

        # need these values on first iteration, can't cut them
        if i != 0:
            seed = seed[width:]
        

        
        for j in range(width):
            my_arr.append([True if seed[j:j+1] == '1' else False for x in range(width)])
           
    return my_arr


def to_arr_bin(seed: str):
    dimension = math.ceil(math.sqrt(len(seed)))
    target_len = dimension * dimension

    for i in range(target_len - len(seed)):
        seed = seed + "0"
        # maybe??
        #  seed = seed + str(int(random_bool()))

    return to_arr_known(seed,dimension,dimension)

def to_arr_bin_uncompress(seed: str):
    dimension = math.ceil(math.sqrt(len(seed)))
    target_len = dimension * dimension

    for i in range(target_len - len(seed)):
        seed = seed + "0"
        # maybe??
        #  seed = seed + str(int(random_bool()))

    return to_arr_known_uncompress(seed,dimension,dimension)


def to_arr(seed: int):
    
    num = str(bin(seed))[3:]

    return to_arr_bin(num)

def to_arr_uncompress(seed: int):
    num = str(bin(seed))[3:]

    return to_arr_bin_uncompress(num)

arr = to_arr_uncompress(random.randrange(10000000000,99999999999))


while True:
    pprint(mask_arr(arr))
    arr = generate_frame(arr)

    time.sleep(0.1)
    os.system("clear")










