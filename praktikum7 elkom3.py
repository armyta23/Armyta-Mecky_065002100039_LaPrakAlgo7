# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 02:33:32 2021

@author: LENOVO
"""

def main(ss):
    if ss %5==0:
        ss**5 
        print ("hasilnya adalah",ss**5)
    else:
        cek(nomor)
def cek(ss):
    if ss %5!=0:
        print ("false")
        exit(0)
nomor=int(input("masukan bilangan: "))
main(nomor)