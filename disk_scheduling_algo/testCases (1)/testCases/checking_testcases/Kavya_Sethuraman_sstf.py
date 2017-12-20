import os
import random
import sys
import copy

num_req=10

def split_list(list):
    return list[:num_req], list[num_req:]

def sstf(list,head):
    tlist = copy.copy( list )
    tlist.sort()
    order1 = []
    order2 = []
    diff_list = []
    j = 0
    added = 1

    while j < len( tlist ):
        if head > tlist[j]:
            order2.append( tlist[j] )  # lesser than head
        else:
            order1.append( tlist[j] )  # greater than head
        j = j + 1

    if len( order2 ) > 0 and len( order1 ) > 0:
        order2.reverse()
        if abs( order1[0] - head ) == abs( order2[0] - head ):
            order = order2 + order1
        else:
            order = order1 + order2
    elif len( order1 ) > 0:
        order = order1
    else:
        order2.reverse()
        order = order2

    seektime = 0
    j = 0
    while j < len( order ):
        diff = abs( head - order[j] )
        diff_list.append( diff )
        seektime = seektime + diff
        head = order[j]
        j = j + 1
#       print( "     The Diff List      : {}".format( diff_list ) )
    return seektime, order


def Main():
    input_file= open( sys.argv[-1], 'r' )
    print(input_file.name)
    read_file = input_file.readline()   # read head
    head=int(read_file)
    read_file = input_file.readline()   # read the list and split
    list=read_file.split(',')
    list=[int(i) for i in list]
    input_file.close()

    #print("Input --> Head = {} , List = {}".format(head,list))
    #print("SSTF Algorithm")
    seektime, order = sstf(list,head)
    print( order )
    print(seektime)
    print(order[-1],seektime)

Main()