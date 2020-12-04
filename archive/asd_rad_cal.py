import struct



fullpathname = "/Users/adam/Dropbox/rs/instrumentation/goddard_calibration_jan_2016/asd/Ni161225.raw"
with open(fullpathname, 'rb') as f:
    asdbinary = f.read()

    
val = []
for i in range(2151):
    val.append(struct.unpack('d', asdbinary[484+(i*8):(484+(i*8)+8)])[0])

val = np.array(val)



test2 = openASD("/Users/adam/Dropbox/rs/leaftraits/fresh_spectra/20160610/spectra/asd/")


vnir= val[:651]
swir1 = val[651:1401]
swir2= val[1401:]

pan = (test2.targ[3]/test2.refl[3]).values


panv= pan[:651]
pans1 = (pan[651:1401]*test2.gainSWIR1[3]) -test2.offsetSWIR1[3]
pans3= (pan[1401:]*test2.gainSWIR2[3]) -test2.offsetSWIR2[3]



plt.plot(test2.targ.index[:651],panv/vnir)
plt.plot(test2.targ.index[651:1401],pans1/swir1)
plt.plot(test2.targ.index[1401:],pans3/swir2)