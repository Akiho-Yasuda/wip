# from pass_gen import pass_gen
# from sprg import
#
# inputVal_1 = pass_gen() #PASS
# print("inputVal_1:{0}".format(inputVal_1 == inputVal_2))
#
# inputVal_2 = "1"  #ユーザ音声入力
# print("inputVal_2:{0}".format(inputVal_2 == inputVal_1))

import glob
import os
# import pass_gen

list_of_files = glob.glob('/Users/akiho/wip/*.txt') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

f=open(latest_file, "r")
if f.mode == 'r':
    contents =f.read()
    # print(contents)

d=open('pas.txt', "r")
if d.mode == 'r':
    pas = d.read()
    # print(contents)

# inputVal_1 = pas
inputVal_1 = pas
inputVal_2 = contents
print("inputVal_1:{0}".format(inputVal_1 in inputVal_2))
print("inputVal_2:{0}".format(inputVal_2 in inputVal_1))
