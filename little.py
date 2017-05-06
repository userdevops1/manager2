#!/usr/bin/python

from random import randint	
import os 
for i in range(5):
     j = randint(0,100)
     os.system("touch %s-%s.txt" % (i,j))	 

