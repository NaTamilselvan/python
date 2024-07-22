
def kthelement(arr,size,k) :

   arr.sort()

   return arr[k-1] 




#Driver code

#if__name__=='__main__' :

#if__name__ == '__main__':

if __name__ == '__main__':

  arr=[10,2,3,4,6,7];
 
  k=3

  size=len(arr)

  print("The k th maximum element is ",kthelement(arr,size,k))







