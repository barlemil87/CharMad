with open('TEXT1.txt', 'w+') as f:
    
    t=0
    t_f=0    
    #pops=init_pop
        
    while t<=total_rxn_time:
             
        a0=0
        aj=[]
        sum_a=0
    
        for j in range(0, no_of_rxns):
        
            aj=aj+[(reaction_constants[j]*pops[reactant_index_new[j]])]
            a0=a0+aj[j]
            
            if a0==0:
                with open('test2.txt', 'w+') as f:
                    print(t_f, ip, sep=' ', end='\n', file=f)
                    break 
        
        import random 
        r1=random.uniform(0,1)
        r2=random.uniform(0,1)
    
        tau=(1/a0)*math.log(1/r1)
        alpha=a0*r2
            
            if r1==0:
                #r1=0.0000001
    
        sum_a=0
        
        for i in range(0, no_of_rxns):
            
            sum_a=sum_a+aj[i]
        
            if sum_a>=alpha:
                    
                Rj=i
                pops[reactant_index_new[Rj]]=pops[reactant_index_new[Rj]]-1
                pops[product_index_new[Rj]]=pops[product_index_new[Rj]]+1
                break
            
        while t_f<=t:
            ip = ' '.join(str(i) for i in pops)
            print(t_f, ip, sep=' ', end='\n', file=f)
            t_f=t_f+time_interval
        
        t=t+tau
        
import itertools

for _ in itertools.repeat(None, 10):
    do_something()
