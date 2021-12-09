import random

def initialize_lifts():

    floors = random.sample([i for i in range(0, 20)], 5) 
    #getting a sample of 5 ensures randomization and unique values = 5 picked from 0 to 20
    #since two lifts can never be on the same floor
    directions = ['U', 'D', ''] 
    #either the lifts are going up, down or are stationary

    lifts = []
    for i in range(5):
        floor = floors[i]
        if floor==0: #if its on the ground floor it cant go down, only up or stationary
            currState = str(floor)+random.choice(['U', ''])
        elif floor==20: #if its on the top floor the only direction it can go is down
            currState = str(floor)+'D' 
        else:
            currState = str(floor)+random.choice(directions)
        lifts.append(currState)
    
    return lifts


def call_lift():
    # we can process the input but first we need to do some validation checking
    while True:
        try:
            user = input("Enter a request? ")
            dir = user[-1]
            pos = int(user.rstrip(dir))
            if (pos >=0 and pos <=20) and (dir=='U' or dir=='D' or dir==''):
                break
            else:
                print("Please re-enter. Floor number has to be from 0 to 20 and direction can only be U or D")
        except ValueError:
            print("Please correct your input format. Should be <floor> <direction>")
            continue

    print("User is on {}th floor going {}".format(pos, dir))
    return user

def get_lift(user, lifts):
    user_dir = user[-1]
    user_pos = int(user.rstrip(user_dir))
    distance=0
    diff_list = [] #putting the various distances in a list
    for index, lift in enumerate(lifts):
        if lift[-1].isdigit(): 
            lift_pos = int(lift)
            lift_dir=''
            distance = abs(lift_pos - user_pos) #if the lift is stationary, the absolute distance is all it'd take
            #print(distance)
        else:
            lift_dir=lift[-1]
            lift_pos = int(lift.rstrip(lift_dir))
            #the position and the direction are gotten in case the lift is moving
            if (lift_dir == user_dir): #if its moving in the same direction as the user
                if lift_dir=='U':
                    distance = (user_pos - lift_pos) if (user_pos > lift_pos) else (20-lift_pos + 20 - user_pos)
                else:
                    distance = user_pos + lift_pos
            else:
                if lift_dir=='U':
                    distance = (user_pos - lift_pos) if (user_pos > lift_pos) else (20-lift_pos + 20 - user_pos)
                else:
                    distance = user_pos + lift_pos
            #print(distance)
        diff_list.append(distance)
    return diff_list
        
if __name__=="__main__":
    lifts = initialize_lifts()
    print("RANDOMIZED LIFTS ARE AT: \n {}".format(lifts))
    curr = call_lift()
    list_distances = (get_lift(curr, lifts))
    print("The distances => {}".format(list_distances))
    min_index = list_distances.index(min(list_distances))+1 #since the indices start from 0
    print("Lift no. {} is coming to get you!".format(min_index))