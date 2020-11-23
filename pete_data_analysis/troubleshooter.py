import cable_inspection as cip 
import os,re,sys
import accubid_class as acc

def troubleshooter1(job_number,conduit_size):  
    
    output=[]
    job_name_dict=cip.job_name_dict
    
    L,FOC,TE=cip.main() 
    total=L+FOC+TE  
    
    total_accubid=acc.main()
    
    print('\n')
    print ('FOR DATASET OF REAZ BELOW:')
    for i in range (len(total)): 
        if (total[i].job_name==job_name_dict[job_number]) and (conduit_size in total[i].conduit_dict): 
            reaz=total[i].drawing.strip(' ')   
            print (reaz)
            output.append(reaz)
    
    print('\n')
    print ('FOR DATASET OF ACCUBID BELOW:')
    for i in range (len(total_accubid)): 
        if (total_accubid[i].job_name==job_name_dict[job_number]) and (conduit_size in total_accubid[i].conduit_dict): 
            accubid=total_accubid[i].drawing.strip(' ') 
            print (accubid)
            if accubid not in output: 
                output.append(accubid)
    print (output)    
    return output

if __name__=="__main__":
    job_number=int(input('Enter job number: '))
    conduit_size=input('Enter conduit size: ') 
    troubleshooter1(job_number, conduit_size)