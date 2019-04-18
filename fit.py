from math import *
def dist(x1,y1,x2,y2):
    return sqrt(((x2-x1)**2)+((y2-y1)**2))
def fitness1(wolf,no_of_wolf,coord,no_of_datap,demand,capacity):
    clusters=list()
    cap_viol=[0]*no_of_wolf
    for i in range(no_of_wolf):
        a=list()
        clusters.append(a)
    for i in range(no_of_datap):
        min_dist=float("inf")
        min_dist_index=float("inf")
        for j in range(no_of_wolf):
            d=dist(coord[i][0],coord[i][1],wolf[j][0],wolf[j][1])
            #print("dp ",i,"c ",j)
            #print("dist ",d)
            if(min_dist>d):
                min_dist=d
                min_dist_index=j
        clusters[min_dist_index].append(i)
        cap_viol[min_dist_index]=cap_viol[min_dist_index]+demand[i]
        
    print(clusters)
    print(cap_viol)
    fitness_d=0
    fitness_cp=0
    for i in range(no_of_wolf):
        for j in clusters[i]:
           fitness_d=fitness_d+dist(coord[j][0],coord[j][1],wolf[i][0],wolf[i][1])
        fitness_cp=fitness_cp+max(0,cap_viol[i]-capacity)
    #print(fitness_d)
    return (clusters,fitness_d+fitness_cp)

def fitness2(wolf,no_of_wolf,coord,no_of_datap,demand,capacity):
    #print("capacity ::: ",capacity)
    #print ("function starting")
    clusters=list()
    cap_viol=[0]*no_of_wolf
    unvisited=list()
    for i in range(no_of_wolf):#6
        a=list()
        clusters.append(a)
    overall_dist_array=list()#[index of data point,dist_array of that dp(dist with 6 centroids)]
    for i in range(no_of_datap):#33
        dist_array=list()#2d array (index,distance)
        min_dist_index=0
        for j in range(no_of_wolf):
            pair=list()
            d=dist(coord[i][0],coord[i][1],wolf[j][0],wolf[j][1])
            dist_array.append([j,d])
        overall_dist_array.append(dist_array)
        dist_array.sort(key=lambda elem:elem[1])
        min_dist_index=dist_array[0][0]
        if((cap_viol[min_dist_index]+demand[i])<=capacity):
            clusters[min_dist_index].append(i)
            cap_viol[min_dist_index]=cap_viol[min_dist_index]+demand[i]
        else :
            unvisited.append(i)

    '''print(clusters)
    print(cap_viol)
    print(unvisited)
    print(" ")
    print("After adding")'''
    for i in unvisited:
        #print("data point ",i," with demand ::: ",demand[i])
        dist_array=overall_dist_array[i]
        #print("dist array ",dist_array)
        for j in range(1,no_of_wolf):
            #print(j)
            if((cap_viol[dist_array[j][0]]+demand[i])<=capacity):
                clusters[dist_array[j][0]].append(i)
                cap_viol[dist_array[j][0]]=cap_viol[dist_array[j][0]]+demand[i]
                #print("entering in ::: ",dist_array[j][0])
                #print("cap_viol ",cap_viol)
                break
            else :
                #print("not able to enter in ",dist_array[j][0])
                continue
    '''print(clusters)
    print(cap_viol)'''
    '''print(" ")
    for i in range(33):
        print(i,overall_dist_array[i])
    total_dist=0
    for i in range(no_of_wolf):
        for j in clusters[i]:
            total_dist=total_dist+overall_dist_array[j][i][1]
    print ("total ",total_dist)'''
    fitness_d=0
    for i in range(no_of_wolf):
        for j in clusters[i]:
           fitness_d=fitness_d+dist(coord[j][0],coord[j][1],wolf[i][0],wolf[i][1])
    return (clusters,fitness_d)

#ratio=distance/demand
def fitness3(wolf,no_of_wolf,coord,no_of_datap,demand,capacity):
    #print ("function starting")
    clusters=list()
    cap_viol=[0]*no_of_wolf
    unvisited=list()
    for i in range(no_of_wolf):#6
        a=list()
        clusters.append(a)
    overall_ratio_array=list()#[index of data point,dist_array of that dp(dist with 6 centroids)]
    for i in range(no_of_datap):#33
        ratio_array=list()#2d array (index,distance/demand)
        min_dist_index=0
        for j in range(no_of_wolf):
            pair=list()
            d=dist(coord[i][0],coord[i][1],wolf[j][0],wolf[j][1])
            D=d/demand[i]
            ratio_array.append([j,D])
        overall_ratio_array.append(ratio_array)
        ratio_array.sort(key=lambda elem:elem[1])
        min_ratio_index=ratio_array[0][0]
        if((cap_viol[min_dist_index]+demand[i])<=capacity):
            clusters[min_dist_index].append(i)
            cap_viol[min_dist_index]=cap_viol[min_dist_index]+demand[i]
        else :
            unvisited.append(i)

    #print(clusters)
    #print(cap_viol)
    #print(unvisited)
    #print(" ")
    #print("After adding")
    for i in unvisited:
        #print("data point ",i," with demand ::: ",demand[i])
        ratio_array=overall_ratio_array[i]
        #print("ratio array ",ratio_array)
        for j in range(1,no_of_wolf):
            #print(j)
            if((cap_viol[ratio_array[j][0]]+demand[i])<=capacity):
                clusters[ratio_array[j][0]].append(i)
                cap_viol[ratio_array[j][0]]=cap_viol[ratio_array[j][0]]+demand[i]
                #print("entering in ::: ",ratio_array[j][0])
                #print("cap_viol ",cap_viol)
                break
            else :
                #print("not able to enter in ",ratio_array[j][0])
                continue
    #print(clusters)
    #print(cap_viol)
    fitness_d=0
    for i in range(no_of_wolf):
        for j in clusters[i]:
           fitness_d=fitness_d+dist(coord[j][0],coord[j][1],wolf[i][0],wolf[i][1])
    return (clusters,fitness_d)

def fitness4(wolf,no_of_wolf,coord,no_of_datap,demand,capacity):
     
     clusters=list()
     cap=[0]*no_of_wolf
     cap_viol=[0]*no_of_wolf
   
     for i in range(no_of_wolf):
         a=list()
         clusters.append(a)
     for i in range(no_of_datap):
         dis=list()
         for j in range(no_of_wolf):
             dis.append(dist(coord[i][0],coord[i][1],wolf[j][0],wolf[j][1]))
         min_dist_index=dis.index(min(dis))
         if cap[min_dist_index]+demand[i]<=capacity:       
             clusters[min_dist_index].append(i)
             cap[min_dist_index]=cap[min_dist_index]+demand[i]
         else:
             d=list()
             for k in range(no_of_wolf):
                 d.append([k,dis[k]])
             d.sort(key=lambda elem:elem[1])
             min_viol=float("inf")
             for k in d:
                 cap_viol[k[0]]=max(0,(cap[k[0]]+demand[i])-capacity)
                 if min_viol>cap_viol[k[0]]:
                     min_viol=cap_viol[k[0]]
                     min_viol_index=k[0]
                     
             clusters[min_viol_index].append(i)        
             cap[min_viol_index]=cap[min_viol_index]+demand[i]
            
     #print(clusters)
     #print(cap)
     fitness_d=0
    #fitness_cp=0
     for i in range(no_of_wolf):
         for j in clusters[i]:
            fitness_d=fitness_d+dist(coord[j][0],coord[j][1],wolf[i][0],wolf[i][1])
        #fitness_cp=fitness_cp+max(0,cap[i]-capacity)
    #print(fitness_d)
     return (clusters,fitness_d)


def fitness5(wolf,no_of_wolf,coord,no_of_datap,demand,capacity):
     
     clusters=list()
     cap=[0]*no_of_wolf
     cap_viol=[0]*no_of_wolf
   
     for i in range(no_of_wolf):
         a=list()
         clusters.append(a)
     for i in range(no_of_datap):
         dis=list()
         for j in range(no_of_wolf):
             dis.append(dist(coord[i][0],coord[i][1],wolf[j][0],wolf[j][1])/demand[i])
         min_dist_index=dis.index(min(dis))
         if cap[min_dist_index]+demand[i]<=capacity:       
             clusters[min_dist_index].append(i)
             cap[min_dist_index]=cap[min_dist_index]+demand[i]
         else:
             d=list()
             for k in range(no_of_wolf):
                 d.append([k,dis[k]])
             d.sort(key=lambda elem:elem[1])
             min_viol=float("inf")
             for k in d:
                 cap_viol[k[0]]=max(0,(cap[k[0]]+demand[i])-capacity)
                 if min_viol>cap_viol[k[0]]:
                     min_viol=cap_viol[k[0]]
                     min_viol_index=k[0]
                     
             clusters[min_viol_index].append(i)        
             cap[min_viol_index]=cap[min_viol_index]+demand[i]
            
     #print(clusters)
     #print(cap)
     fitness_d=0
    #fitness_cp=0
     for i in range(no_of_wolf):
         for j in clusters[i]:
            fitness_d=fitness_d+dist(coord[j][0],coord[j][1],wolf[i][0],wolf[i][1])
        #fitness_cp=fitness_cp+max(0,cap[i]-capacity)
    #print(fitness_d)
     return (clusters,fitness_d)    

