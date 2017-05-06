#!/usr/bin/python

from random import randint	
import os 
for i in range(2):
     j = randint(0,10)
     os.system("touch %s-%s.txt" % (i,j))	 

