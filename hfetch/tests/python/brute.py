from time import time
from hfetch import *

'''''''''
This test iterates over a huge amount of data
'''''''''
connectCassandra(["127.0.0.1"], 9042)
nparts = 6000000  # Num particles in range
p = 1000  # Num partitions

t_f = 0  # Token begin range
t_t = 5764607523034234880  # Token end range

# Token blocks
tkn_size = (t_t - t_f) / (nparts / p)
tkns = [(a, a + tkn_size) for a in xrange(t_f, t_t - tkn_size, tkn_size)]

a = Hcache("test", "particle", "WHERE token(partid)>=? AND token(partid)<?;", tkns, ["partid", "time"], ["x"],
           {'cache_size': '10', 'writer_buffer': 20})


def readAll(iter):
    count = 1
    i = iter.get_next()
    while (i is not None):
        try:
            i = iter.get_next()
        except StopIteration:
            print 'End of data, items read: ', count, ' with value ', i
            break
        count += 1
        if count % 100000 == 0:
            print count
    print "iter has %d elements" % count


start = time()
readAll(a.iterkeys(100))
print "finshed into %d" % (time() - start)
a = None
