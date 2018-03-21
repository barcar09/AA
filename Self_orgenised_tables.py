import numpy
import collections
import matplotlib.pyplot as plt
import pylab as P
starting_list = [el for el in range(1,101)]         #  List for sorting
dict_counter = collections.OrderedDict(list(zip(starting_list,[1 for el in range(100)])))   #  Dict for counter method

def Schedule_returner(Input_Schedule): # This function return schedule choose by name parameter.
    harmonic = 0.0
    for i in range(1, 101): # Count 100 harmonic number
        harmonic += 1.0 / i
    Prob_list= [el for el in range(1,101)]
    if Input_Schedule == "Linear":
         z=numpy.random.choice(starting_list,p = [1 / 100 for el in range(100)])
    if Input_Schedule == "Harmonic":
         z=numpy.random.choice(starting_list,p = [1 / (el*harmonic) for el in range(1, 101)])
    if Input_Schedule == "Geometric":
        alfa=[(1/2) ** el for el in range(1,100)]
        alfa.append(1/2 ** 99)
        z=numpy.random.choice(starting_list, pv = alfa)
        
    return(z)

def self_orgenised_lists(z, type_of_orgenised):     # This function return type of orgenising list.
    counter = 1
    global dict_counter
    if type_of_orgenised == "no_organisation":

        for el in range(100):
            if starting_list[el] == z:
                return (counter)
            else:
                counter+=1
    if type_of_orgenised == "move_to_front":
        for els in range(100):
            if starting_list[els] == z:
                starting_list.insert(0, starting_list.pop(starting_list.index(starting_list[els])))
                return (counter)
            else:
                counter+=1
    if type_of_orgenised == "transpose":
        for els in range(100):
            if starting_list[els] == z:

                if starting_list.index(starting_list[els]) == 99:
                    starting_list.insert(0, starting_list.pop(starting_list.index(starting_list[els])))
                else:
                    starting_list.insert(starting_list.index(starting_list[els+1]),
                                         starting_list.pop(starting_list.index(starting_list[els]))
                                         )
                return (counter)
            else:
                counter+=1
    if type_of_orgenised == "count":
        for els in dict_counter.keys():
            if els == z:
                dict_counter[els] += 1
                dict_counter = collections.OrderedDict(sorted(dict_counter.items(), key=lambda d: d[1], reverse = True))
                return (counter)
            else:
                counter+=1
def ret_tab_function(typ_of_scheduling, type_of_orgenised):     # This function return iteration by n with choosing schedule and orgenising
    global starting_list
    global dict_counter
    linear_data_tab=[]
    all_counter=0
    n=[100,500,1000,5000,10000,50000,100000]
    for els in n:
        starting_list= [el for el in range(1,101)]
        dict_counter = collections.OrderedDict(list(zip(starting_list, [1 for el in range(100)])))
        for el in range(els):
            s = Schedule_returner(typ_of_scheduling)
            all_counter += self_orgenised_lists(s,type_of_orgenised)
        linear_data_tab.append(all_counter / els)
        all_counter=0
    return(linear_data_tab)
Linear_data_sets_no_org=ret_tab_function("Geometric", "no_organisation")

Linear_data_sets_move_to_front= ret_tab_function("Geometric", "move_to_front")      # Returning each schedule with geometric schedule
Linear_data_sets_transpose = ret_tab_function("Geometric", "transpose")
Linear_data_sets_count = ret_tab_function("Geometric", "count")
N = 7
# Ploting histogram with chosen schedule
ind = numpy.arange(N)  # the x locations for the groups
width = 0.10
fig,ax = plt.subplots()
rects1 = ax.bar(ind,Linear_data_sets_no_org, width, color='r')
rects2 = ax.bar(ind + 0.10,Linear_data_sets_move_to_front, width, color='y')
rects3 = ax.bar(ind + 0.20,Linear_data_sets_transpose, width, color='b')
rects4 = ax.bar(ind + 0.30,Linear_data_sets_count, width, color='g')
# add some text for labels, title and axes ticks
ax.set_ylabel('Średni koszt')
ax.set_xlabel('Ilość operacji')
ax.set_title('Średnie dla rozkładu harmonicznego')
ax.set_xticks(ind + 0.3 / 2)
axes = plt.gca()
ax.set_xticklabels(('100', '500', '1000', '5000', '10000','50000','100000'))

ax.legend((rects1[0], rects2[0],rects3[0],rects4[0]) ,('no org', 'mtf','trans','count'))
plt.show()
print("ukończono")

