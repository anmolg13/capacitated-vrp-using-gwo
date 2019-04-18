import random
import numpy,copy
from math import *
from dataSetFiles import *
from fit import *
import matplotlib.pyplot as plt
def dist(x1,y1,x2,y2):
    return sqrt(((x2-x1)**2)+((y2-y1)**2))
for v in range(1,21):
    a='funA'+str(v)
    distArr=[]
    filename,no_of_data_points=globals()[a]()
    for z in range(10):
        no_of_customers=no_of_data_points-1
        capacity=0
        Max_iter=500
        SearchAgents=100#wolves
        file = open(filename, 'r')
        data = file.readline()
        capacity=(int)(data)
        x_list=list()
        y_list=list()
        coord=list()
        demand=list()
        data = file.readline()
        temp=data.split()
        source_x=(int)(temp[0])
        source_y=(int)(temp[1])
        #print ("source_x ::: ",source_x)
        #print ("source_y ::: ",source_y)
        for i in range(no_of_customers):
            data = file.readline()
            word = data.split()
            x=(int)(word[0])
            y=(int)(word[1])
            x_list.append(x)
            y_list.append(y)
            pair=list()
            pair.append(x)
            pair.append(y)
            coord.append(pair)
            #print (pair)
        data = file.readline()
        data = file.readline()
        for i in range(no_of_customers):
            data = file.readline()
            demand.append((int)(data))
        print (demand)
        file.close()

        x_min=min(x_list)
        x_max=max(x_list)
        y_min=min(y_list)
        y_max=max(y_list)

        #print("sum demand ::: ",sum(demand))
        k=int((sum(demand)/capacity)+0.99)
        #print ('k value ::: ',k)

        population=list()
        for i in range(SearchAgents):
            chromosome=list()
            for i in range(k):
                #x_rand_coord=random.uniform(x_min,x_max)
                #y_rand_coord=random.uniform(y_min,y_max)
                x_rand_coord=(random.uniform(0,1)*(x_max-x_min))+x_min
                y_rand_coord=(random.uniform(0,1)*(y_max-y_min))+y_min
                pair=list()
                pair.append(x_rand_coord)
                pair.append(y_rand_coord)
                chromosome.append(pair)
            #print (chromosome)
            population.append(chromosome)

        Alpha_pos=numpy.zeros(k)
        Alpha_score=float("inf")
            
        Beta_pos=numpy.zeros(k)
        Beta_score=float("inf")
            
        Delta_pos=numpy.zeros(k)
        Delta_score=float("inf")
            
        Convergence_curve=numpy.zeros(Max_iter)
            
        for l in range(Max_iter):
            for i in range(SearchAgents):
                clusters,fitness=fitness5(population[i],k,coord,no_of_customers,demand,capacity)
                #print(fitness)
                
                if (fitness<Alpha_score) :
                    Alpha_score=fitness; # Update alpha
                    Alpha_pos=population[i]
                    final_cluster=clusters
                    
                    
                if (fitness>Alpha_score and fitness<Beta_score ):
                    Beta_score=fitness  # Update beta
                    Beta_pos=population[i]
                    
                    
                if (fitness>Alpha_score and fitness>Beta_score and fitness<Delta_score): 
                    Delta_score=fitness # Update delta
                    Delta_pos=population[i]
                    
                
            a=2-l*((2)/Max_iter);
            
            for i in range(0,SearchAgents):
                for j in range (0,k):
                    r1=random.random() # r1 is a random number in [0,1]
                    r2=random.random() # r2 is a random number in [0,1]
                    
                    A1=2*a*r1-a; # Equation (3.3)
                    C1=2*r2; # Equation (3.4)
                    
                    D_alpha_x=abs(C1*Alpha_pos[j][0]-population[i][j][0]); # Equation (3.5)-part 1
                    X1=Alpha_pos[j][0]-A1*D_alpha_x; 
                    D_alpha_y=abs(C1*Alpha_pos[j][1]-population[i][j][1]); # Equation (3.5)-part 1
                    Y1=Alpha_pos[j][1]-A1*D_alpha_y;# Equation (3.6)-part 1
                               
                    r1=random.random()
                    r2=random.random()
                    
                    A2=2*a*r1-a; # Equation (3.3)
                    C2=2*r2; # Equation (3.4)

                    D_beta_x=abs(C2*Beta_pos[j][0]-population[i][j][0]); # Equation (3.5)-part 1
                    X2=Beta_pos[j][0]-A2*D_beta_x; 
                    D_beta_y=abs(C2*Beta_pos[j][1]-population[i][j][1]); # Equation (3.5)-part 1
                    Y2=Beta_pos[j][1]-A2*D_beta_y; # Equation (3.6)-part 2       
                    
                    r1=random.random()
                    r2=random.random() 
                    
                    A3=2*a*r1-a; # Equation (3.3)
                    C3=2*r2; # Equation (3.4)
                    
                    D_delta_x=abs(C3*Delta_pos[j][0]-population[i][j][0]); # Equation (3.5)-part 3
                    X3=Delta_pos[j][0]-A3*D_delta_x; # Equation (3.5)-part 3             
                    D_delta_y=abs(C3*Delta_pos[j][1]-population[i][j][1]); # Equation (3.5)-part 3
                    Y3=Delta_pos[j][1]-A3*D_delta_y; 
                    
                    population[i][j][0]=(X1+X2+X3)/3  # Equation (3.7)
                    population[i][j][1]=(Y1+Y2+Y3)/3                 
                    
                
                
            Convergence_curve[l]=Alpha_score;
            
            #print(['At iteration '+ str(l)+ ' the best fitness is '+ str(Alpha_score)+str(final_cluster)])
            #print("\n")
            
        #print ("alpha pop ::: ",Alpha_pos)

        #print(final_cluster)

        total_distance=0
        n=0
        for i in final_cluster:
            cities=[]
            tour=[]
            cities.append([source_x,source_y])
            for j in i:
                cities.append(coord[j])
            len_of_cluster=len(i)+1
            for j in range(len_of_cluster):
                tour.append(j)
            #print (tour)
            for temperature in numpy.logspace(0,5,num=5000)[::-1]:
                [i,j] = sorted(random.sample(range(len_of_cluster),2))
                newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1]+tour[j+1:]
                if exp( ( sum([ sqrt(sum([(cities[tour[(k+1) % len_of_cluster]][d] - cities[tour[k % len_of_cluster]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]]) - sum([ sqrt(sum([(cities[newTour[(k+1) % len_of_cluster]][d] - cities[newTour[k % len_of_cluster]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]])) / temperature) > random.random():
                    tour = copy.copy(newTour);
            #print (tour)
            zero_index=tour.index(0)
            new_tour=tour[zero_index:]+tour[0:zero_index]
            #print (new_tour)
            x=[]
            y=[]
            distance=0
            x.append(source_x)
            y.append(source_y)
            for j in range(0,(len(tour)-1)):
                x.append(cities[new_tour[j]][0])
                y.append(cities[new_tour[j]][1])
                distance=distance+dist(cities[new_tour[j]][0],cities[new_tour[j]][1],cities[new_tour[j+1]][0],cities[new_tour[j+1]][1])
            x.append(cities[new_tour[len(new_tour)-1]][0])
            y.append(cities[new_tour[len(new_tour)-1]][1])
            distance=distance+dist(cities[new_tour[len(tour)-1]][0],cities[new_tour[len(tour)-1]][1],source_x,source_y)
            x.append(source_x)
            y.append(source_y)
            n=n+1
            #plt.plot(x,y,label=n)
            total_distance=total_distance+distance
        #print (total_distance)
        distArr.append(total_distance)
        #plt.legend()
        #plt.show()
    print('##################################################################################################')
    print("fun ::: "+str(v))
    print(distArr)
    print(min(distArr))
