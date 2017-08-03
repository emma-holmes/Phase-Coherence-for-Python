# Phase-Coherence-for-MATLAB
Function to calculate consistency of phase at a given frequency across measurements

## About the method
### Some background
This function calculates phase coherence at a frequency of interest, across different measurements. The phase coherence value indexes how consistent the phase is across different measurements. The phase coherence value lies between 0 and 1: 1 indicates perfect phase coherence and 0 indicates no phase coherence.

This method is often used in electro-encephalography (EEG) analyses to determine the phase consistency of the neural response at a particular frequency, across trials. For example, researchers often choose to investigate phase consistency at the frequency of a presented stimulus. Note that the same method is sometimes referred to as the phase locking value (PLV)--although some implementations of the PLV use a time-series filter rather than conducting the analyses in the frequency domain, as used here.

The method is described in the following paper: 
>Picton, T. W., John, M. S., Dimitrijevic, A., & Purcell, D. (2003). Human auditory steady-state responses: Respuestas auditivas de estado estable en humanos. International journal of audiology, 42(4), 177-219.

### Extentions of the method
This method could be applied to examine patterns in time-series data other than neural data.

## Getting started
### Prerequisites
The code was written using MATLAB 2014b, although uses basic MATLAB functions that are compatible with older and newer versions of MATLAB. No additional toolboxes are required.

### Running the MATLAB script
The MATLAB code is contained within the following file: [PhaseCoherence.m](PhaseCoherence.m)

The script takes three inputs:
1) freq - this is a value indicating the frequency to be analysed, in Hertz, e.g. 50.
2) timeSeries - this is the data to be analysed; should be a 2-dimensional matrix of size: (number of trials/measurements) x (number of time points)
3) FS - this is the sampling rate of the time-series data, in Hertz, e.g. 1000.

The code can be run as follows:
```
PC = PhaseCoherence(freq, timeSeries, FS)
```
The output from the script is a floating-point value between 0 and 1.

## License

This project is licensed under the MIT License; see the [LICENSE](LICENSE) file for details
