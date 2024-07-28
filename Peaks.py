#This program i am trying to find peak element in python 
#what is peak element in sorted or natural order or ascending  order to last element or decending oder first element or same value element every element 
#but ascending order is  before element is low and next value high and after elemnent is low 



def  findPeak(a,n):
        
         if(n==1): 
            return n-1
         if(a[0]>a[1]):
            return n-1
         if(a[n-1]>a[n-2]):
            return n-1

         for i  in range(1,len(a)-1):
              if(a[i-1]<a[i] and a[i+1]<a[i]):
                   return a[i]



arr=[5, 10, 20, 15]
#arr = [ 1, 3, 20, 4, 1, 0 ]
n = len(arr)
#print("Index of a peak point is", findPeak(arr, n))





#driver code :

 #array= [5, 10, 20, 15]

print(findPeak(arr,len(arr)))