import json
from pprint import pprint
from sys import argv
import sys
import collections
from collections import OrderedDict

q_list = []
sub_lis = []

#k1_list = []
k1_list = sys.argv[2]
k2_list = []
#kw = []
kw = k1_list.split()
#print kw
res_dict = {}
# for x in k1_list:
#     x=x.strip()
#     x=x.split()
#     while len(x) > 0:
#         k2_list.append(x.pop())
# for j in k2_list:
#     j1 = ''.join( [i for i in j if i.isalnum()] )
#     kw.append(j1)



def convertstring(ques):
    cstring=""
    ques=ques.lower()                           ##please check
    for i in ques :
        if i.isalnum() or '0'<= i <= '9':
            cstring+=i
        elif i == ' ':
            cstring +=' '
        elif i == "'":
            cstring +=''
        else:
            cstring +=' '
    return cstring

def check_ques(ques):
    cstring=convertstring(ques)
    count = 0
    for key in kw:
            key=key.lower()                          ## please check
            splitted=cstring.split()
            for j in splitted :
                if j == key:
                    count += 1
                    break
    if count == len(kw):
        return True
    else :
        # ques = ques.lower()
        # for key in kw:
        #     key = key.lower()
        #     if key in ques:
        #         print ques,key
        return False


if __name__ == "__main__":
    dict_list= []
    filename = sys.argv[1]
    with open(filename) as data_file:
        data_r = json.load(data_file)
    length=0
    for i in range(0,len(data_r["data"])) :
        for j in range(0,len(data_r["data"][i]["paragraphs"])):
            for k in range(0,len(data_r["data"][i]["paragraphs"][j]["qas"])):
                ques = data_r["data"][i]["paragraphs"][j]["qas"][k]["question"]
                rv = check_ques(ques)
                if rv == True:
                    length+=1
                    id = data_r["data"][i]["paragraphs"][j]["qas"][k]["id"]
                    ans = data_r["data"][i]["paragraphs"][j]["qas"][k]["answers"][0]["text"]
                    res_dict =OrderedDict([("id",id),("question",ques),("answer",ans)])
                    #OrderedDict(res_dict)
                    q_list.append(ques)
                    sub_lis.append(res_dict)

    with open('1b.json','w') as fp:
        json.dump(sub_lis, fp)

    print(q_list)
    #print sub_lis
    #print(length)
