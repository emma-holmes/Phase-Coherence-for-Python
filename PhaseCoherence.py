# -*- coding: utf-8 -*-
"""
This function calculates phase coherence at a frequency of interest 
across different measurements, i.e. cosistency of phase at a given 
frequency. The output phase coherence value lies between 0 and 1: 
1 indicates perfect phase coherence and 0 indicates no phase coherence.

Created on Wed Aug  2 17:58:06 2017
@author: emmah
"""

import numpy as np

def PhaseCoherence(freq, timeSeries, FS):

    # Get parameters of input data
    nMeasures	 = np.shape(timeSeries)[0]
    nSamples 	= np.shape(timeSeries)[1]
    nSecs = nSamples / FS
    print('Number of measurements =', nMeasures)
    print('Number of time samples =', nSamples, '=', nSecs, 'seconds')
    
    # Calculate FFT for each measurement (spect is freq x measurements)
    spect = np.fft.fft(timeSeries, axis=1)
    
    # Normalise by amplitude
    spect = spect / abs(spect)
    
    # Find spectrum values for frequency bin of interest
    freqRes = 1 / nSecs;
    foibin = round(freq / freqRes + 1) - 1
    spectFoi = spect[:,foibin]
    
    # Find individual phase angles per measurement at frequency of interest
    anglesFoi = np.arctan2(spectFoi.imag, spectFoi.real)
    
    # PC is root mean square of the sums of the cosines and sines of the angles
    PC = np.sqrt((np.sum(np.cos(anglesFoi)))**2 + (np.sum(np.sin(anglesFoi)))**2) / np.shape(anglesFoi)[0]
    
    # Print the value
    print('----------------------------------');
    print('Phase coherence value = ' + str("{0:.3f}".format(PC)));
        
    return PC