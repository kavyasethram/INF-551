from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":

    sc=SparkContext(appName='BusyMonth')

    lines=sc.textFile(sys.argv[1]).map(lambda s: s.encode("ascii", "ignore").split(','))\
            .map(lambda s: (s[1],s[2],int(s[5])))\
            .filter(lambda (x,y,z): y =='Terminal 1' or y =='Terminal 2' or y =='Terminal 3' or y =='Terminal 4' or y =='Terminal 5'\
                                or y =='Terminal 6' or y == 'Terminal 7' or y == 'Terminal 8'\
                                or y =='Tom Bradley International Terminal')\
            .map(lambda (x,y,z): (x,z))\
            .map(lambda (x,y): (x.split(' ')[0].split('/')[0]+'/'+x.split(' ')[0].split('/')[2],y))

    lines1 = lines.reduceByKey(add).filter(lambda (x,y): y>5000000)

    result = lines.collect()
    for (key,value) in result:
        print("%s %i" % (key,value))