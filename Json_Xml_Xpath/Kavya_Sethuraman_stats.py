import sys
import json
from pprint import pprint
q_list = []

h_count = 0
hmany_count = 0
hmuch_count = 0
w_count = 0
wh_count = 0
where_count = 0
which_count = 0
whom_cnt = 0
who_cnt = 0

filename = sys.argv[1]
with open(filename) as data_file:

    data_r = json.load(data_file)

for i in range(0,len(data_r["data"])) :
    for j in range(0,len(data_r["data"][i]["paragraphs"])):
        for k in range(0,len(data_r["data"][i]["paragraphs"][j]["qas"])):
            ques = data_r["data"][i]["paragraphs"][j]["qas"][k]["question"].lower()
            ques = ques.replace(',', '')
            ques = ques.split()[:2]
            q_list.append(ques)

for i in range(0,len(q_list)):
    if (q_list[i][0] == "how")  and q_list[i][1] == "many":
        hmany_count+=1
    elif (q_list[i][0] == "how") and q_list[i][1] == "much":
        hmuch_count+=1 
    elif q_list[i][0] == "how":
        h_count+=1
    elif q_list[i][0] == "what":
        w_count+=1
    elif q_list[i][0] ==  "when":
        wh_count+=1
    elif q_list[i][0] ==  "where":
        where_count+=1
    elif q_list[i][0] ==  "which":
        which_count+=1
    elif q_list[i][0] ==  "who":
         who_cnt+=1
    elif q_list[i][0] ==  "whom":
         whom_cnt+=1

h_count = h_count + hmany_count + hmuch_count
d = {"How":h_count,"How many":hmany_count,"How much":hmuch_count,"What":w_count,"When":wh_count,"Where":where_count,"Which":which_count,"Who":who_cnt,"Whom":whom_cnt}
with open('1a.json', 'w') as outfile:
    json.dump(d, outfile)