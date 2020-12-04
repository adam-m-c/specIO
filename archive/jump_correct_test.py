from specIO import *
import matplotlib.pyplot as plt



asd =  openASD("/home/adam/Dropbox/rs/leaftraits2016/20160916/spectra/asd/POTR_T_B_SH_2016091600003.asd",jump_correct=True)

fig = plt.figure(figsize =(8,8))
ax = fig.add_subplot(111)

asd.refl.plot(ax=ax)

asd.refl.loc[:,350:asd.splice1]  =asd.refl.loc[:,350:asd.splice1+1] +  (asd.refl[asd.splice1+1] - asd.refl[asd.splice1])

asd.refl.loc[:,asd.splice2+1:2500]  =asd.refl.loc[:,asd.splice2+1:2500] +  (asd.refl[asd.splice2] - asd.refl[asd.splice2+1])

asd.refl.plot(ax=ax)
ax.set_xlim(1795,1805)
ax.set_ylim(.3,.35)
