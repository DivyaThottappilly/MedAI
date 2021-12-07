#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:39:43 2021

@author: aditya
"""

"""
serum_bilirubin (mg/dL)
serum creatinine (mg/dL)

"""
 
import math                 
                  
serum_creatinine = 1.2
serum_bilirubin = 1.8
inr = 1.1
sodium = 138

def meld_score(x):
    serum_creatinine =float(x[1])
    serum_bilirubin = float(x[2])
    inr = float(x[3])
    sodium = float(x[4])
    if sodium <125:
        sodium = 125
    elif sodium >137:
        sodium = 137
        
    meld_score =round( 3.78 * math.log(serum_bilirubin) + 11.2 * math.log(inr) + 9.57 * math.log(serum_creatinine) + 6.43)
    meld_na_score = round(meld_score - sodium - (0.025 * meld_score * (140-sodium)) +140)
    print(meld_score)
    
    print(meld_na_score)
    prediction='MELD Score is '+' {}'.format(meld_score)+' & MELD Na Score is'+' {}'.format(meld_na_score)