# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:47:31 2017

@author: Michael
"""
import numpy as np
from dateutil.parser import parse

def __is_date(k):
    try:
        parse(k)
        return True
    except ValueError:
        return False
    except OverflowError:
        return False

def ifdate(a):
    # accept input argument as numpy array of n rows and 3 columns
    output=np.zeros(shape=(np.shape(a)[0],3))
    this_element=a[:,2]
    for i in range(np.shape(a)[0]):
        output[i,1]=int(__is_date(str(this_element[i])))

    output[:,0]=np.append(output[:,1][1:],0)
    output[:,2]=np.insert(output[:,1][:-1],0,0)
    return output