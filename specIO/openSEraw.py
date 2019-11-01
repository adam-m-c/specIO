import pandas as pd, numpy as np
import os, datetime as dt,struct

######################################################################################################################################################                                                 
"""   ___      ___    ___     ___              ___   __   __   ___   
     / __|    | _ \  | __|   / __|     o O O  | __|  \ \ / /  / _ \  
     \__ \    |  _/  | _|   | (__     o       | _|    \ V /  | (_) | 
     |___/   _|_|_   |___|   \___|   TS__[O]  |___|   _\_/_   \___/  
"""
######################################################################################################################################################                                                                                                 
                                                                                                                                                   
"""The following functions and classes are used to parse out SPRECTRAL EVOLUTION spectral data
from .sed files, not all attributes are enabled."""

class SE(object):
    """Spec Evo spectral data object"""

    def __init__(self):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        
        self.filename = np.nan            
        self.channels= np.nan    
        self.refr =  np.nan
        self.targ =  np.nan

        def changeColumnNames(self,byColumn):
            for key, value in self.__dict__.items():
                print(key)


def populateSEClass(meta,refr,targ):
    
    classObject = SE()
    
    classObject.filename = meta.filename
    classObject.channels= meta.channels
    classObject.refr =  refr
    classObject.targ =  targ
    
    return classObject


def SEspectraSeries(fullpathname):
    #this function take as input a single spectra and returns a pandas series 
    
    #intitiate list to hold spectral metadata    
    metadata = [[],[]]    

    #read spectral text file
    text = open(fullpathname,'r')
       
    #get filename     
    metadata[0].append("filename")
    metadata[1].append(os.path.basename(fullpathname))
    
    #open the .raw file as a binary file
    with open(savFile, 'rb') as f:
        #read the file
        sav = f.read()
        
    #get number of wavelength values         
    channels1 = struct.unpack("I", sav[:4])[0]  
    
    
    #combine reference date and time into a datetime object    
    metadata[0].append("channels")
    metadata[1].append(channels1)       

    #list to hold wavelengths    
    wavelengths= []
    
    #cycle through data to get wavelengths
    for x in range(channels1):
        #get wavelength
        wavelength = struct.unpack("h", sav[4+(x*2): 4+(x*2)+2])[0] 
        #append wavelngth to wavelength list
        wavelengths.append(wavelength/10.)
        
    #calcualte the start of the second channel length
    ch2_start =    4+ channels1*2 
    
    #get number of reference values         
    channels2 = struct.unpack("I", sav[ch2_start:ch2_start+4])[0] 
    
    #list to hold reference DNs
    referenceDNs = []
    
    #cycle through data to get reference DNS
    for x in range(channels2):
        #get reference DN
        reference = struct.unpack("h", sav[ch2_start+(x*2): ch2_start+(x*2)+2])[0] 
        #append reference DN to list
        referenceDNs.append(reference)
    
    #calcualte the start of the third channel length
    ch3_start =    ch2_start+ channels2*2 
    
    #get number of target values         
    channels3  = struct.unpack("I", sav[ch2_start:ch2_start+4])[0] 
    
    #list to hold target DNs    
    targetDNs= []
    
    #cycle through data to get target DNs
    for x in range(channels3):
        #get target DN
        target = struct.unpack("h", sav[ch3_start+(x*2): ch3_start+(x*2)+2])[0] 
        #append target DN to list
        targetDNs.append(target)

    #load  metadata, reference, target data into pandas series
    metaSeries = pd.Series(metadata[1],index = metadata[0])
    refrSeries = pd.Series(referenceDNs,index = wavelengths)
    targSeries = pd.Series(targetDNs,index = wavelengths)

    
    #return data series;
    return metaSeries,refrSeries,targSeries
        


def openSEraw(foldORfile):
    #this function is used to open spectral datafiles Ocean Optics spectrometers. 
    #It can take an input a folder or a single file. If a single file is input it will return
    # a pandas series, if a folder is input it will return a pandas dataframe containing all the spectra
    # This function assumes that all of the txt files containg in the folder are OO spectra.


    #if the input path is a file
    if os.path.isfile(foldORfile) and foldORfile.endswith(".raw"):

        #read spectral data
        meta,refr,targ=  SEspectraSeries(foldORfile)
        
        #get a populated SE object
        SE =  populateSEClass(meta,refr,targ)
        
        return SE

    #if the patgh is a folder    
    elif os.path.isdir(foldORfile):

        #create empty dataframe to hold metadata
        metaDF = pd.DataFrame()
        
        #create empty dataframe to hold refrerence data
        refrDF = pd.DataFrame()
        
        #create empty dataframe to hold target data
        targDF = pd.DataFrame()

        #get list of txt files in the folder
        files = [txt for txt in os.listdir(foldORfile) if txt.endswith(".raw")]
        
        #cycle through each of the spectra
        for i,filename in enumerate(files): 

            series = SEspectraSeries(foldORfile +filename)
        
            #load spectral data into a pandas series
            metaDF[i] = series[0]
            refrDF[i] = series[1]
            targDF[i] = series[2]
                        
        #get a populated ASD object
        SE =   populateSEClass(metaDF.T,refrDF,targDF)
        
        print("Loaded %s Spectral Evolution spectral files" % SE.refr.shape[1])
        return SE
        
        
    else:
        
        print("Pathname is neither a file nor a folder!!!!!")
        return
        
        
        
import struct 


savFile = "/Users/adam/Dropbox/temp/D09_0037_CA_00001.raw"

#open the .sav file as a binary file
with open(savFile, 'rb') as f:
    #read the file
    sav = f.read()
    
#get number of wavelength values         
channels1 = struct.unpack("I", sav[:4])[0]  

wavelengths= []

#cycle through data to get wavelengths
for x in range(channels1):
    #get wavelength
    wavelength = struct.unpack("h", sav[4+(x*2): 4+(x*2)+2])[0] 
    wavelengths.append(wavelength/10.)
    

ch2_start =    4+ channels1*2 
#get number of reference values         
channels2 = struct.unpack("I", sav[ch2_start:ch2_start+4])[0] 

referenceDNs = []

#cycle through data to get wavelengths
for x in range(channels2):
    #get wavelength
    reference = struct.unpack("h", sav[ch2_start+(x*2): ch2_start+(x*2)+2])[0] 
    referenceDNs.append(reference)


ch3_start =    ch2_start+ channels2*2 

#get number of reference values         
channels3  = struct.unpack("I", sav[ch2_start:ch2_start+4])[0] 

targetDNs= []

#cycle through data to get wavelengths
for x in range(channels2):
    #get wavelength
    target = struct.unpack("h", sav[ch3_start+(x*2): ch3_start+(x*2)+2])[0] 
    targetDNs.append(target)
    
targetDNs = np.array(targetDNs)
referenceDNs = np.array(referenceDNs)