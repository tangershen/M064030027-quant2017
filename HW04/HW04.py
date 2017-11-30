
# coding: utf-8

# In[1]:


def multiplication_table(m,n):
    i=1
    while i<=9:
        for j in range (m,n+1):
            print(str(j)+"x"+str(i)+"="+str(j*i).rjust(2),end='    ')                       
            j+=1 
        i+=1
        print('')
    print('-------------------我是分隔線------------------')


# In[2]:


def pyramid(k):
   
    L=0
    while L<=k:
        print( (k-L)*" "+(2*L-1)*("*" ))
        
        L+=1

