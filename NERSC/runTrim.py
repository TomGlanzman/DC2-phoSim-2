#!/usr/bin/env python
## runTrim.py - phoSim catalog trim step
##

import os,sys,shutil,gzip

print '\n\nWelcome to runTrim.py\n========================\n'
rc = 0

## Setup logging, python style
import logging as log
log.basicConfig(stream=sys.stdout, format='%(asctime)s %(levelname)s in %(filename)s line %(lineno)s: %(message)s', level=log.INFO)

## Insert task config area for python modules (insert as 2nd element in sys.path)
sys.path.insert(1,os.getenv('DC2_CONFIGDIR'))
#from config import *
import runPhosimStep


## Run Trim
log.info('Run Trim')
print '\n\n======================== Begin phoSim/Trim ========================\n'
rc = runPhosimStep.runPhosimStep('trim',0)
if rc != 0:
    log.error('Failure in trim step, aborting...')
    sys.exit(1)
print '\n======================== End phoSim/Trim ========================\n\n'



## Extract Sensor coordinates and pass back to workflow engine
log.info('Extract sensorIDs from .par file')
parFileName = 'trim_'+os.getenv('DC2_OBSHISTID')+'_'+os.getenv('PIPELINE_STREAM')+'.pars'
print 'parFileName = ',parFileName

sixdigits = "%06d" % int(os.getenv('DC2_TOPLEVEL6'))
workDir = os.path.join(os.getenv('PHOSIM_SCR_ROOT'),sixdigits,'work')
print 'workDir = ',workDir

pf = os.path.join(workDir,parFileName)
print 'parFile = ',pf
sensors = []   # all sensors in this raft
with open(pf,'r') as pfp:
    for line in pfp:
        if line.startswith('chipid'):sensors.append(line.split()[2].strip())
        pass
    pass
print 'sensors = ',sensors

## Generate list of sensors to simulate based on content of trimmed catalog and 'minsource'
sensors2 = []   # all sensors to be simulated
minsource = int(os.getenv('DC2_MINSOURCE'))
print 'Selecting sensors to be simulated (minsource=',minsource,')'
for sensor in sensors:
    trimcatFileName = 'trimcatalog_'+os.getenv('DC2_OBSHISTID')+'_'+sensor+'.pars'
    trincatFileName = os.path.join(workDir,trimcatFileName)
    print 'trimcatFileName = ',trimcatFileName
    numSources = sum(1 for line in open(trimcatFileName))-2
    print 'Number of sources found in this trimmed catalog = ',numSources
    if numSources >= minsource: sensors2.append(sensor)
    pass

numSensors = len(sensors2)
print 'sensors2 (',numSensors,') = ',sensors2
sList = ','.join(sensors2)
print 'sList = ',sList

cmd = 'pipelineSet DC2_SENSORLIST '+sList
rc = os.system(cmd)
if rc <> 0 :
    log.error("Unable to set pipeline variable")
    sys.exit(1)
    pass
cmd = 'pipelineSet DC2_SENSORLIST_LEN '+str(numSensors)
rc = os.system(cmd)
if rc <> 0 :
    log.error("Unable to set pipeline variable")
    sys.exit(1)
    pass



log.info("All done")
sys.exit(0)
