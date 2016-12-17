
import math

def entropy_target(data):
    a={}
    a[0]=0.0  # number of zeros in data
    a[1]=0.0

    for record in (data):
        if record==0:
            a[0]+=1
        else:
            a[1]+=1
        
    pr_1=float(a[0]/len(data)) # probability of data sets
    pr_2=float(a[1]/len(data))
    if pr_1==0:
        e_1=0
    else:
        e_1=math.log(1/pr_1,2)
    if pr_2==0:
        e_2=0
    else:
        e_2=math.log(1/pr_2,2)

    entropy = (pr_1*e_1) +(pr_2*e_2)
    
    return entropy



    
def entropy(data, target_attr):
    a={}
    a[0]=0.0  # number of zeros in data
    a[1]=0.0
    a[2]=0.0
    b={}
    b[0]=0.0  # number of zeros in target attribute for 0 in data
    b[1]=0.0  # number of ones in target attribute for 0 in data
    c={}
    c[0]=0.0  # number of zeros in target attribute for 1 in data
    c[1]=0.0
    d={}
    d[0]=0.0  # number of zeros in target attribute for 2 in data
    d[1]=0.0
    for record in (data):
        if record==0:
            a[0]+=1
        elif record==1:
            a[1]+=1
        else:
            a[2]+=1
    
    i=0
    for record in data:
        if record == 0:
            if record == target_attr[i]:
                b[0]+=1.0
                i=i+1
            else:
                b[1]+=1.0
                i=i+1
        if record == 1:
            if target_attr[i] == 0:
                c[0]+=1.0
                i=i+1
            else:
                c[1]+=1.0
                i=i+1
        if record == 2:
            if target_attr[i] == 0:
                d[0]+=1.0
                i=i+1
            else:
                d[1]+=1.0
                i=i+1
    

    pr_1=float(a[0]/len(data)) # probability of data sets
    pr_2=float(a[1]/len(data))
    pr_3=float(a[2]/len(data))
    

    if a[0]==0:
        e_1=0
        e_2=0
    else:
        e_1=float(b[0]/a[0])
        e_2=float(b[1]/a[0])

    if a[1]==0:
        e_3=0
        e_4=0
    else:
        e_3=float(c[0]/a[1])
        e_4=float(c[1]/a[1])
    if a[2]==0:
        e_5=0
        e_6=0
    else:
        e_5=float(d[0]/a[2])
        e_6=float(d[1]/a[2])

        

    if e_1 == 0:
        lo_1 = 0
    else:
        lo_1 = math.log(1/e_1,2)

    if e_2 == 0:
        lo_2 = 0
    else:
        lo_2 = math.log(1/e_2,2)

    if e_3 == 0:
        lo_3 = 0
    else:
        lo_3 = math.log(1/e_3,2)

    if e_4 == 0:
        lo_4 = 0
    else:
        lo_4 = math.log(1/e_4,2)

    if e_5 == 0:
        lo_5 = 0
    else:
        lo_5 = math.log(1/e_5,2)

    if e_6 == 0:
        lo_6 = 0
    else:
        lo_6 = math.log(1/e_6,2)

    
    if pr_1==0:
        r_1=0
    else:
        r_1 = pr_1*(e_1*lo_1+e_2*lo_2)
    if pr_2==0:
        r_2=0
    else:
        r_2= pr_2*(e_3*lo_3+e_4*lo_4)
    if pr_3==0:
        r_3=0
    else:
        r_3= pr_3*(e_5*lo_5+e_6*lo_6)
    
   
    entropy = r_1+r_2+r_3
    
    return entropy

def gain(entropy_attribute, entropy_target_attr):
    return(entropy_target_attr-entropy_attribute)

def partition_new(fi,partition):
    
    k=[]
    for i in range(0,len(partition)):
        k.append([])
    for i in range(0,len(partition)):
        for j in range(1,len(partition[i])):
                       k[i].append(int(partition[i][j]))
        
    return k
def cal_final_f(rec,f_partition,total_ins):
    temp=[]
    i=0  
    for record in f_partition:
        temp.append(rec[record-1])
        i+=1
        
    
    rel_target=[]
    

    rel_target=zip(*temp)#inverting rows to columns 
    
    e1=entropy_target(rel_target[len(rel_target)-1])
    
    keep_entropy=[]
    for i in range(0,len(rel_target)-1):
        keep_entropy.append(entropy(rel_target[i],rel_target[len(rel_target)-1]))
    

    gain_rel=[]
    for i in range(0,len(keep_entropy)):
        gain_rel.append(gain(keep_entropy[i],e1))
    
    target_attr=total_ins #change it to pass arguements
    
    f1=float(len(f_partition))/float(target_attr)*max(gain_rel)
    return f1
def final_split(index,partition,rec_int):
    
    sub_arr=[]
    for record in partition:
        sub_arr.append(rec_int[record-1])
    
    con_sub_arr=[]
    con_sub_arr=zip(*sub_arr)
    
    e1=entropy_target(con_sub_arr[len(con_sub_arr)-1]) 
    split_entropy=[]
    for i in range(0,len(con_sub_arr)-1):
        split_entropy.append(entropy(con_sub_arr[i],con_sub_arr[len(con_sub_arr)-1]))
    gain_re=[]
    for i in range(0,len(split_entropy)):
        gain_re.append(gain(split_entropy[i],e1))
    print gain_re
    
    
    for i in range(0,len(gain_re)):
        if gain_re[i] == max(gain_re):
            feature_split_index=i
    
    z1=[]
    z2=[]
    z3=[]
    
    for i in range(0,len(con_sub_arr[feature_split_index])):
                   if(con_sub_arr[feature_split_index][i]==0):
                       z1.append(partition[i])
                   elif(con_sub_arr[feature_split_index][i]==1):
                       z2.append(partition[i])
                   else:
                       z3.append(partition[i])
    z1.insert(0,'z1')
    z2.insert(0,'z2')
    z3.insert(0,'z3')
    
    
    
                      
    return z1,z2,z3,feature_split_index+1


print "Enter names of the files dataset input-partition output-partition"
dataset= raw_input(">")
partition= raw_input(">")
output= raw_input(">")


rec=[]
file = open(dataset,"r")
a=file.readline()
b=[]
b=a.split(' ')
total_ins = int(b[0])
total_atts = int(b[1])

for line in file:
    rec.append(line.split())#rec has input file
    
file.close()


rec_2 = []

file2 = open(partition,"r")
for line_1 in file2:
    rec_2.append(line_1.split())

file2.close()


f_partition=[]
f_partition=partition_new(rec,rec_2)# rec_2 has partition file data

sum=0
for i in range(0,len(f_partition)):
    for j in range(0,len(f_partition[i])):
        sum+=f_partition[i][j]

s_ins = total_ins*(total_ins+1)/2

if (sum != s_ins):
    print "please enter correct partition"
    exit()




rec_int=[]
for i in range(0,len(rec)):
    rec_int.append([])
for i in range(0,len(rec)):
    for j in range(0,len(rec[i])):
        rec_int[i].append(int(rec[i][j])) #rec_int has input in integer format

all_f=[]
for i in range(0,len(f_partition)):
    all_f.append(cal_final_f(rec_int,f_partition[i],total_ins))#call above loop
   

for i in range(0,len(all_f)):
    if all_f[i]==max(all_f):
        index=i


z1,z2,z3,feature_split_index=final_split(index,f_partition[index],rec_int)

print "partition ",rec_2[index][0]," was replaced with partitions ",
if(len(z1)!=1):
    print "z1",
    rec_2.append(z1)
if(len(z2)!=1):
    print "z2",
    rec_2.append(z2)
if(len(z3)!=1):
    print "z3",
    rec_2.append(z3)
print "using feature",feature_split_index

rec_2.pop(index)

with open(output, 'w') as file3:
    file3.writelines(' '.join(str(j) for j in i) + '\n' for i in rec_2)
file3.close()

