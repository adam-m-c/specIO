from specIO import *



test = openSE("/home/adam/data/", readRaw=True)

test2 = openSE("/home/adam/data/", readRaw=False)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(test.refl.index,test.refl*100, label = 'Raw')
ax1.plot(test2.refl.index,test2.refl, label = 'SE 1nm')
ax1.legend()