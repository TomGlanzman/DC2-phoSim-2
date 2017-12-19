#!/usr/bin/env python
## runRaytrace.py - phoSim catalog trim step
##

import os,sys,shutil,gzip

print '\n\nWelcome to runRaytrace.py\n========================\n'
rc = 0

## Setup logging, python style
import logging as log
log.basicConfig(stream=sys.stdout, format='%(asctime)s %(levelname)s in %(filename)s line %(lineno)s: %(message)s', level=log.INFO)
log.info("Start")

## Insert task config area for python modules (insert as 2nd element in sys.path)
sys.path.insert(1,os.getenv('DC2_CONFIGDIR'))
#from config import *
import runPhosimStep

## Initialize lists of output data products
outputFiles = []  # filenames of phosim data products
outList = []         # full final path/filename of data products

## Loop over exposures (snaps) for this visit
nsnaps = os.getenv('DC2_NSNAP')
log.info('Number of exposures for this visit: '+nsnaps)
for snap in range(0,int(nsnaps)):
    log.info('Start raytrace for exposure '+str(snap))

    ## phoSim raytrace
    rc = 0
    rc = runPhosimStep.runPhosimStep('raytrace',snap)
    if rc != 0: sys.exit(1)

    ## phoSim e2adc [optional]
    if os.getenv('PHOSIM_E2ADC') == '1':
        rc = runPhosimStep.runPhosimStep('e2adc',snap)
        if rc != 0: sys.exit(1)
    else:
        log.info('Skipping e2adc step')
        pass

    ## Collect phoSim output data product file names
    exposure = "%03d" % snap
    core1 = os.getenv('DC2_OBSHISTID')+'_f'+os.getenv('DC2_FILTER_NUM')+'_'+os.getenv('DC2_SENSORID')
    core2 = '_E'+exposure
    print 'filename common core1 = ',core1
    print 'filename common core2 = ',core2

    ## Electron file
    fElectron = 'lsst_e_'+core1+core2+'.fits.gz'
    print 'fElectron = ',fElectron
    outputFiles.append(fElectron)

    ## Centroid file
    if os.getenv('DC2_CENTROIDFILE') == '1':
        fCentroid = 'centroid_lsst_e_'+core1+core2+'.txt'
        print 'fCentroid = ',fCentroid
        outputFiles.append(fCentroid)
        pass
       
    ## Amplifier (e2adc) files
    if os.getenv('PHOSIM_E2ADC') == '1':
        #log.warning('Harvesting e2adc files not yet supported')
        for a in range(0,18):
            if a == 8 or a == 9: continue
            amp = "_C%0.2i" % a
            fAmplifier = 'lsst_a_'+core1+amp+core2+'.fits.gz'
            print 'fAmplifier = ',fAmplifier
            outputFiles.append(fAmplifier)
            pass
        pass
   

    ## Copy data products from $SCRATCH to project area
    log.info('Copy data products from $SCRATCH to project area')
    sixdigits = "%06d" % int(os.getenv('DC2_TOPLEVEL6'))
    workDir = os.path.join(os.getenv('PHOSIM_SCR_ROOT'),sixdigits,'work')
    print 'workDir = ',workDir
    outDir = os.getenv('DC2_PHOSIMOUT')
    print 'outDir = ',outDir
    for filename in outputFiles:
        ifile = os.path.join(workDir,filename)
        ofile = os.path.join(outDir,filename)
        if not os.access(ifile,os.R_OK):
            log.error('Cannot access phosim data product: '+ifile)
            rc = 1
            pass
        shutil.copy2(ifile,ofile)
        outList.append(ofile)
        pass

    pass ## end of loop over exposures


## Send list of output files to workflow engine for subsequent registration
log.info('Prepare list of files to be registered')
outlist = ','.join(outputFiles)
print 'length of outlist = ',len(outlist)

cmd = 'pipelineSet DC2_OUTPUTDIR '+outDir
print cmd
rc = os.system(cmd)
if rc <> 0 :
    log.error("Unable to set pipeline variable \n $%s",cmd)
    sys.exit(99)
    pass
cmd = 'pipelineSet DC2_OUTPUTLIST '+outlist
print cmd
rc = os.system(cmd)
if rc <> 0 :
    log.error("Unable to set pipeline variable \n $%s",cmd)
    sys.exit(99)
    pass
    
log.info("All done")
sys.exit(rc)
