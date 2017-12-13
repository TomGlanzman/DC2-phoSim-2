## utils.py - utility functions for use in DC2 phoSim workflow scripts

import os,sys
import pickle


def dm2phosim(chipID):
    ## Convert dm to phosim style of LSST sensor ID
    ##
    ## dm format: R:n,m S:n,m (or S:n,m,A/B for corner rafts)
    ## phosim format: Rnm_Snm
    ## where n,m range from 0-4
    #print 'dm2phosim - chipID = ',chipID
    rRow = chipID.split()[0].split(':')[1].split(',')[0]
    rCol = chipID.split()[0].split(':')[1].split(',')[1]
    #print 'rRow = ',rRow,', rCol = ',rCol
    sRow = chipID.split()[1].split(':')[1].split(',')[0]
    sCol = chipID.split()[1].split(':')[1].split(',')[1]
    #print 'sRow = ',sRow,', sCol = ',sCol
    r = rRow+rCol
    s = sRow+sCol
    newID = 'R'+r+'_S'+s
    #print 'newID = ',newID
    ## Ignore corner rafts
    if r == '00' or r == '04' or r == '40' or r == '44':
        newID = None
        #print 'corner raft...ignore.'
        pass
    return newID


def getVisit(stream, visitFile):

    print 'Entering getVisit:\n   stream ',stream,'\n   visitFile ',visitFile

    # Open & read visit list
    fd = open(visitFile,'r')
    vList = fd.readlines()
    fd.close()

    print "     visit file contains ",len(vList)," visits."

    # Select visit number (obsHistID) index by stream #
    obsHistID = vList[stream].split()[0]
    print "     stream ",stream,' corresponds to visit (obsHistID) = ',obsHistID
    print "=============================\n"
    # Return obsHistID
    return obsHistID


