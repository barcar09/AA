import numpy
starting_list= [el for el in range(1,101)]
all_counter=0
def Schedule_returner(Input_Schedule):
    harmonic = 0.0
    for i in range(1, 101):
        harmonic += 1.0 / i
    Prob_list= [el for el in range(1,101)]
    if Input_Schedule == "Linear":
         z=numpy.random.choice(starting_list,p=[1/100 for el in range(100)])
    if Input_Schedule == "Harmonic":
         z=numpy.random.choice(starting_list,p=[1/el*harmonic for el in range(1,101)])
    if Input_Schedule == "Geometric":
        z=numpy.random.choice(starting_list,p=[1/2**el for el in range(1,100)].append(1/2**99))
    return(z)

def self_orgenised_lists(z, type_of_orgenised):
    if type_of_orgenised == "no_organisation":
        counter=1
        for el in range(100):
            if starting_list[el] == z:
                return (counter)
            else:
                counter+=1
    if type_of_orgenised == "move_to_front":
        counter=1
        for el in range(100):
            if starting_list[el] == z:
                starting_list.insert(0, starting_list.pop(starting_list.index(el+1)))
                return (counter)
            else:
                counter+=1
    if type_of_orgenised == "transpose":
        counter=1
        for el in range(100):
            if starting_list[el] == z:

                starting_list.insert(starting_list.index(el+2), starting_list.pop(starting_list.index(el+1)))
                return (counter)
            else:
                counter+=1
for el in range(100):
    s=Schedule_returner("Linear")
    all_counter+=self_orgenised_lists(s,"move_to_front")
    print(starting_list)
print(all_counter/100)
