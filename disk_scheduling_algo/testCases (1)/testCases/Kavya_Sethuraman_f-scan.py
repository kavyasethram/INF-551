import os
import random
import sys
import copy

num_req=10

def split_list(list):
    return list[:num_req], list[num_req:]

def scan(list,head):
    tlist=copy.copy(list)
    tlist.sort()
    order1=[]
    order2=[]
    diff_list=[]
    j=0
    added=1
    while j < len(tlist) :
        if head > tlist[j]:
            order2.append(tlist[j])          #lesser than head
        else:
            order1.append(tlist[j])          #greater than head
        j=j+1

    if len(order2) > 0 and len(order1) > 0:
        order2.reverse()
        if abs(order1[0]-head) == abs(order2[0]-head):
            order2.append(0)
            order=order2+order1
            added=0
        else:
            order1.append(199)
            order=order1+order2
            added=199
    elif len(order1) > 0:
        order=order1
    else:
        order2.reverse()
        order=order2

    seektime=0
    j=0
    while j < len(order) :
        diff=abs(head-order[j])
        diff_list.append(diff)
        seektime=seektime+diff
        head=order[j]
        j=j+1
#    print( "     The Diff List      : {}".format( diff_list ) )
    if added==0:
        order.remove(0)
    elif added==199:
        order.remove(199)
    return seektime,order

def f_scan(list,head):
    tlist=copy.copy(list)
    order=[]
    final_seektime=0
    while len(tlist)> 0:
        tlist1 , tlist = split_list(tlist)
        seektime, order1 = scan( tlist1, head )
        order = order + order1
        final_seektime = final_seektime + seektime
        len_order=len(order)
        head = order[len_order-1]
    return final_seektime, order


def Main():
    input_file= open( sys.argv[-1], 'r' )
    print(input_file.name)
    read_file = input_file.readline()   # read head
    head=int(read_file)
    read_file = input_file.readline()   # read the list and split
    list=read_file.split(',')
    list=[int(i) for i in list]
    input_file.close()
    seektime, order = f_scan(list, head)
    print(order)
    print(seektime)
    print(order[-1], seektime)


Main()