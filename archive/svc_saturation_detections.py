from specIO import *
import pandas as pd, matplotlib.pyplot as plt, numpy as np



specDIR = "/Users/adam/Dropbox/rs/leaftraits2016/20160527/spectra/svc/"

spec1 = openSVC(specDIR + "SOHY_T_B_SH_20160527_004.sig")

spec2 = openSVC(specDIR + "CAOV_T_A_SH_20160527_002.sig")

spec3 = openSVC(specDIR + "ACSA_T_A_SH_20160527_002.sig")