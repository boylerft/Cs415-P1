import numpy as np
import math
import matplotlib.pyplot as plt
import time

euclids_timer = []
euclids_worst_case = []
euclids_worst_case_timer = []
basic_ops = 0
mod_count = 0.0
def scatter_plot(xy, name, xaxis, yaxis):
    for i in range(len(xy)):
            plt.scatter(xy[i][0], xy[i][1])
    plt.title(name)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.show()


def euclids(m, n):
    global mod_count
    if n == 0:
        return m
    else:
        mod_count += 1
        return euclids(n, m % n)
    
def euclidsMD(n):
    global mod_count
    global euclids_timer
    mod_count = 0.0
    total_mod_count = 0.0
    for i in range(1, n+1):
        mod_count = 0
        time2 = time.clock()
        euclids(n, i)
        euclids_timer.append([i, time.clock()])
        total_mod_count += mod_count
    return total_mod_count/n

def euclidsMD_Fib(n):
    global mod_count
    global euclids_worst_case
    mod_count = 0.0
    total_mod_count = 0.0
    for i in range(1, n+1):
        mod_count = 0
       # print("K + 1: ", i + 1)
       # print("K: ", i)
        m = fib_seq(i+1)
        timer = time.clock()
        euclids(m, fib_seq(i))
        euclids_worst_case_timer.append([m, time.clock()])
        euclids_worst_case.append([m, mod_count])

def consecutive_int(m, n, t):
    global mod_count
    tmp = m % t
    mod_count += 1
    if tmp != 0:
     #   mod_count += 1
        return consecutive_int(m, n, t-1)
    else:
        tmp2 = n % t
        mod_count += 1
        if tmp2 == 0:
            return t
        else:
            return consecutive_int(m, n, t-1)

def cons_intD(n):
    global mod_count
    mod_count = 0.0
    total_mod_count = 0.0
    for i in range(1, n+1):
        t = min(i, n)
        mod_count = 0
        consecutive_int(n, i, t)
    #    print(mod_count)
        total_mod_count += mod_count
    return total_mod_count/n   

def fib_seq(k):
   # print("fib k: ", k)
    f = np.empty(k+1, dtype='int64')
    f[0] = 0
    f[1] = 1
    if (k==0):
        return 0
    if (k==1):
        return 1
    for i in range(2, k+1):
        f[i] = f[i-1] + f[i - 2]
   # print("fib array: ", f)
    #return f[k]
    return f[k]

def seiveOf_E(n):
    global basic_ops
    basic_ops = 0
    tmp = []
    L = []
    tmp.append(0)
    tmp.append(0)
    for j in range(2, n+1):
        tmp.append(j)
    for i in range(2, int(math.floor(math.sqrt(n)))+1):
        if tmp[i] != 0:
            j = i * i
            #basic_ops += 2
            while(j <= n):
                tmp[j] = 0
                j = j + i
                basic_ops += 3
    for z in range(2, n):
        if tmp[z] != 0:
            L.append(tmp[z])
    return L
''' 
def comElms(a, b):
    #c = []
    # a is max
    # removes the least amount that
    # doesnt match
    if a[0] < b[0]:
        tmp = b[0]
        for i in range(len(a)-1):
            if tmp == a[i]:
                break
            else:
                a.remove(a[i])
    elif b[0] < a[0]:
        tmp = a[0]
        for i in range(len(b)-1):
            if tmp == b[i]:
                break
            else:
                b.remove(b[i])
    # removes the greatest amount that 
    # doesnt match
    if a[len(a)-1] > b[len(a)-1]:
        tmp = b[len(a)-1]
        for i in range(len(a)-1, 0, -1):
            if tmp == a[i]:
                break
            else:
                a.remove(a[i])
    elif b[len(b)-1] > a[len(a)-1]:
        tmp = a[len(a)-1]
        for i in range(len(b)-1, 0, -1):
            if tmp == b[i]:
                break
            else:
                b.remove(b[i])
    return a, b
''' 
'''
def comElms(a, b):
    c = []
    index_a = 0
    index_b = 0
    act_it = 0
    
    if (a[0] > b[len(b)-1]) or (b[0] > a[len(b)-1]):
        return False
    
    for i in range(max(len(a), len(b))):
        if ((len(a))) == index_a or (len(b)) == index_b:
            act_it += 1
            return c, act_it
        elif a[index_a] == b[index_b]:
            c.append(a[index_a])
            index_a += 1
            index_b += 1
            act_it += 1
        elif a[index_a] < b[index_b]:
            act_it += 1
            while(a[index_a] < b[index_b]):
                if (index_a == len(a)-1):
                    break
                index_a += 1
                act_it += 1
        elif b[index_b] < a[index_a]:
            act_it += 1
            while(b[index_b] < a[index_a]):
                if (index_b == len(b)-1):
                    break
                index_b += 1
                act_it += 1
        else:
            return c, act_it
    return c, act_it
def comElms(a, b):
    c = []
    index_a = 0
    index_b = 0
    act_it = 0
    
    for i in range(max(len(a), len(b))):
        if ((len(a))) == index_a or (len(b)) == index_b:
            act_it += 1
            return c, act_it
        elif a[index_a] == b[index_b]:
            c.append(a[index_a])
            index_a += 1
            index_b += 1
            act_it += 1
        else:
            while(a[index_a] < b[index_b]):
                if (index_a == len(a)-1):
                    break
                index_a += 1
                act_it += 1
            while(b[index_b] < a[index_a]):
                if (index_b == len(b)-1):
                    break
                index_b += 1
                act_it += 1
    return c, act_it
         
def comElms(a, b):
    c = []
    index_a = 0
    index_b = 0
    act_it = 0
    
    for i in range(max(len(a), len(b))):
        if ((len(a))) == index_a or (len(b)) == index_b:
            act_it += 1
            return c, act_it
        elif a[index_a] == b[index_b]:
            c.append(a[index_a])
            index_a += 1
            index_b += 1
            act_it += 1
        else:
            if (a[index_a] < b[index_b]):
                
                if (index_a == len(a)-1):
                    break
                
                index_a += 1
                act_it += 1
            elif (b[index_b] < a[index_a]):
                
                if (index_b == len(b)-1):
                    break
                
                index_b += 1
                act_it += 1
    return c, act_it
'''
def comElms(a, b):
    c = []
    index_a = 0
    index_b = 0
    act_it = 0
    
    for i in range(max(len(a), len(b))):
        if ((len(a))) == index_a or (len(b)) == index_b:
            act_it += 1
            return c, act_it
        elif a[index_a] == b[index_b]:
            c.append(a[index_a])
            index_a += 1
            index_b += 1
            act_it += 1
        else:
            if (a[index_a] < b[index_b]):
                index_a += 1
                act_it += 1
            else:
                index_b += 1
    return c, act_it  

def main():
    user_input = -1
    while(user_input != 0):
        user_input = int(input("Which task would you like to run? (Task 1 = 1, Task 2 = 2, Task 3 = 3, 0 to stop!\n"))
        # TASK 1
        if (user_input == 1):
            task1_input = -1
            while(task1_input != 0):
                task1_input = int(input("Which alorithm would you like to run? Euclids = 1, Consecutive Integer = 2, 0 to stop.\n"))
                # EUCLIDS
                if (task1_input == 1):
                    n = int(input("Please enter a value for N: "))
                    task1_E = []
                    global euclids_timer
                    #euclids_timer.clear()
                    del euclids_timer [:]
                    for i in range(1, n, 5):
                        task1_E.append([i, euclidsMD(i)])
                    print("Here is the scatter plot: \n")
                    scatter_plot(task1_E, "Euclids Average Case Effiecency", "Input N", "Average")
                    timer_case = -1
                    while(timer_case != 0):
                        timer_case = int(input("Would you like to see the time effiecency? (1 for yes, 0 for no) : "))
                        if (timer_case == 1):
                            scatter_plot(euclids_timer, "Euclids Average Time Case Effiecency", "Input N", "Time")
                
                # Consecutive Integer
                if (task1_input == 2):
                    n = int(input("Please enter a value for N: "))
                    task1_C = []
                    for i in range(1, n, 5):
                        task1_C.append([i, cons_intD(i)])
                    print("Here is the scatter plot: \n")
                    scatter_plot(task1_C, "Consecutive Integer Avgerage Case Effiecency", "Input N", "Average")
                else:
                    print("Invalid input, please try again!")
                    
        if (user_input == 2):
            task2_input = -1
            while(task2_input != 0):
                task2_input = int(input("What would you like to do? (Run Euclids worst case effiecency = 1, exit = 0) : \n"))
                if (task2_input == 1):
                    k = int(input("What value would you like to enter for K? : "))
                    timerC = []
                    global euclids_worst_case
                    global euclids_worst_case_timer
                    #euclids_worst_case.clear()
                    del euclids_worst_case [:]
                    #euclids_worst_case_timer.clear()
                    del euclids_worst_case_timer [:]
                    for i in range(1, k, 2):
                        #task2_E.append([i, euclidsMD_Fib(i)])
                        #timer = time.clock()
                        euclidsMD_Fib(i)
                        #timerC.append([i, time.clock()])
                    print("Here is the scatter plot: \n")
                    scatter_plot(euclids_worst_case, "Euclids Worst Case (Fib sequence) With value K: ", "Value of M", "Number of modulos")
                    timer_input = int(input("Would you like to see the time Effiecency of this case? (1 for yes, 0 for no) : "))
                    if (timer_input == 1):
                        scatter_plot(euclids_worst_case_timer, "Time Effiecency of K input", "K input", "Time Effiecency")
                        
        
        if (user_input == 3):
            task3_input = -1
            while(task3_input != 0):
                task3_input = int(input("Which algorithm would you like to run? (sieve of Eratosthenes = 1, find Common Elements = 2, 0 to stop: "))
                if (task3_input == 1):
                    n = int(input("Enter an input for N: "))
                    primeTime = []
                    primeOps = []
                    for i in range(10, n, 5):
                        time1 = time.clock()
                        primes = seiveOf_E(i)
                        primeTime.append([i, time.clock()])
                        primeOps.append([i, basic_ops])
                    which_case = -1
                    while(which_case != 0):
                        which_case = int(input("Which case would you like to see? (Basic Operations = 1, Time Effiecency = 2, 0 to exit) :"))
                        if (which_case == 1):
                            scatter_plot(primeOps, "Basic Operations of sieve of Eratosthenes", "Input", "Basic Operations")
                        if (which_case == 2):
                            scatter_plot(primeTime, "Time Effiecency of sieve of Eratosthenes", "Input", "Time")
                        elif(which_case != 0):
                            print("Invalid input, please try again!")
                if (task3_input == 2):
                    n = int(input("Enter an input for N: "))
                    comElmsEFF_time = []
                    comElmsEFF = []
                    for i in range(10, n, 1):
                        a = np.random.randint(1, high=i, size=i)
                        a.sort()
                        b = np.random.randint(1, high=i/2, size=i/2)
                        b.sort()
                        #print(a, b)
                        #print("after Elms")
                        time2 = time.clock()
                        ret = comElms(a, b)
                        #print(ret)
                        comElmsEFF_time.append([i, time.clock()])
                        comElmsEFF.append([i, ret[1]])
                    which_case = -1
                    while(which_case != 0):
                        which_case = int(input("Which case would you like to see? (Basic Operations = 1, Time Effiecency = 2, 0 to exit) :"))
                        if (which_case == 1):
                            scatter_plot(comElmsEFF, "Basic Operations of Common Elements", "Input", "Basic Operations")
                        if (which_case == 2):
                            scatter_plot(comElmsEFF_time, "Time Effiecency of Common Elements", "Input", "Time")
                        elif (which_case != 0):
                            print("Invalid input, please try again!")
                    
        elif(user_input != 0):
            print("Invalid input, please try again!")
    '''
    # Task 1

    task1_E = []
    task1_C = []
    for i in range(1, n):
       # task1_E.append([i, euclidsMD(i)])
        task1_C.append([i, cons_intD(i)])
        i += 5
   # scatter_plot(task1_E, "Euclids Avg")
    scatter_plot(task1_C, "Consecutive Integer Avg")

    
    # Task 2
    #k = 5
    #print(fib_seq(2))
    task2_E = []
    for i in range(1, 20):
        #task2_E.append([i, euclidsMD_Fib(i)])
        euclidsMD_Fib(i)
        i += 5
    scatter_plot(euclids_worst_case, "Euclids Worst Case (Fib sequence)")

    
    
    # Task 3

    primeTime = []
    primeOps = []
    for i in range(10, 10000):
        time1 = time.clock()
        primes = seiveOf_E(i)
        #primeOps.append([i, basic_ops])
        primeTime.append([i, time.clock() ])
        i += 5
    scatter_plot(primeTime, "Time effieceny of Seive")

    
    #a = [2, 2, 3, 5, 5, 7, 15, 20]
    #b = [2, 5, 5, 5, 15]
    n = 1000
    comElmsEFF_time = []
    comElmsEFF = []
    zero_count = 0
    nonZero_count = 0
    n = 1000
    for i in range(10, n, 1):
        a = np.random.randint(1, high=i, size=i)
        a.sort()
        b = np.random.randint(1, high=i/2, size=i/2)
        b.sort()
        time2 = time.clock()
        ret = comElms(a, b)
        if (ret[1] == 0):
            zero_count += 1
        else:
            nonZero_count += 1
        comElmsEFF_time.append([i, time.clock()])
        comElmsEFF.append([i, ret[1]])

    print(zero_count)
    print(nonZero_count)
        
    
    #print(comElms(a, b))
    #print(comElms(a, b))
    scatter_plot(comElmsEFF_time, "common Elements Time Effiecency")
    #scatter_plot(primeOps, "Basic Ops of Seive")
    #print(seiveOf_E(50))
  #  print(task1_data)
'''  
main()