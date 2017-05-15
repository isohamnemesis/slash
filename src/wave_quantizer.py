import numpy as np
import data_utils as du
import os
from etaprogress.progress import ProgressBar as pgb
import sys

#===============================================================================
# Pre processing script for wave quantization
# Reads raw waves from ../waves/*.wav files
# Generates mu law encoded quantizations
# Stores them in ../data/*.npy
#===============================================================================

if not os.path.exists('../waves/'):
    print 'ERROR: waves directory not found!'
    sys.exit(1)
else:
    wave_files = os.listdir('../waves/')

if not os.path.exists('../data/'):
	os.makedirs('../data/')

bar = pgb(len(wave_files), max_width=50)
print 'starting processing..'

max_len = int(5e4)
for i in range(len(wave_files)):
    bar.numerator = i+1
    clip_name = wave_files[i][:-4]
    q_wave = du.load_file('../waves/'+wave_files[i])
    length = (q_wave.shape[0]/max_len)*max_len
    for j in range(length/max_len):
        np.save('../data/'+clip_name+'_'+str(j)+'.npy', q_wave[j*max_len:(j+1)*max_len])
    print '\033[Ffiles processed:', bar
print 'quantized waves stored in ../data/ '
