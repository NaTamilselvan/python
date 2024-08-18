#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:19:57 2024

@author: natamilme
"""

def minMax1(lst):
    
    lst2=sorted(lst)
    
    print("The min value ",lst2[0])
    print("The max value ",lst[-1])
    
    
    
    
def minMax2(lst):
    
    min=lst[0]
    max=lst[0]
    n=len(lst)
    #to get min value 
    
    for i in range(1,n):
        
        if(min>lst[i]):
            
            min=lst[i]
        
    for j in range(1,n):
        
        if(max<lst[j]):
            
            max=lst[j]
        
    print("The min value ",min)
    print("The max value ",max)
    
    
    
    
lst=[90,20,30,40,50,-1,-2]
minMax2(lst)
