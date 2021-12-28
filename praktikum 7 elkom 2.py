# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 02:03:42 2021

@author: LENOVO
"""

string = list(map(str, input("masukan kalimat: ").lower()))

def vokal_kon(au):
  consonan=0
  vokal=0
  for i in range(0, len(string)):
    if string[i]=='a' or string[i]=='r' or string[i]=='m' or string[i]=='y' or string[i]=='t':
      vokal+=1
    else:
      consonan+=1
  print("Jumlah huruf Vokal: ",vokal)
  print("Jumlah huruf konsonan:",consonan)
vokal_kon(string)