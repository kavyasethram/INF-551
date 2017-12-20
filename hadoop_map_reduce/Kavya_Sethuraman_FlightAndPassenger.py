from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":

    sc=SparkContext(appName='FlightAndPassenger')

    res=sc.textFile(sys.argv[1]).map(lambda s: s.encode("ascii", "ignore").split(','))\
            .map(lambda s: (s[1].split(' ')[0].split('/')[0]+'/'+s[1].split(' ')[0].split('/')[2]+', '+s[3]+', '+s[4],int(s[5])))

    lines1=res.reduceByKey(add)


    output = lines1.collect()

    res2 = sc.textFile(sys.argv[2]).map(lambda s: s.encode("ascii", "ignore").split(',')) \
        .map(lambda s: (s[1].split(' ')[0].split('/')[0] + '/' + s[1].split(' ')[0].split('/')[2] + ', ' + s[3] + ', ' + s[4], int(s[5])))

    lines2= res2.reduceByKey(add)

    output = lines2.collect()
    lines=lines1.join(lines2).sortByKey()
    output = lines.collect()
    for (key,val) in output:
        print("%s, %i, %i" % (key,val[0],val[1]))