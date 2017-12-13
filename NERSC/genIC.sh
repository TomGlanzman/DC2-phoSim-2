#!/bin/bash
## genIC.sh - setup and run the DC2 instanceCatalog generator for the DC2-phoSim-2 task

echo "Entering genIC.sh - setup and run DC2 instanceCatalog generator"
date

## Handle incoming instCat generator command options
options=$@

## Remove command line parameters so as to not confuse the stack setup script :(
shift $#

## Setup
echo "$ "source /global/common/software/lsst/cori-haswell-gcc/stack/setup_w_2017_46_py3_gcc6.sh
source /global/common/software/lsst/cori-haswell-gcc/stack/setup_w_2017_46_py3_gcc6.sh

echo "$ "setup lsst_sims
setup lsst_sims

echo "$ "eups declare gcr_catalogs -r ${PHOSIM_IC_GCR_CATALOGS}  -c
eups declare gcr_catalogs -r ${PHOSIM_IC_GCR_CATALOGS}  -c

echo "$ "setup gcr_catalogs
setup gcr_catalogs

echo "$ "eups list -v gcr_catalogs
eups list -v gcr_catalogs

## Display the IC generator options (incl. default values)
echo "$ "/usr/bin/time python ${PHOSIM_IC_GENERATOR} -h
/usr/bin/time python ${PHOSIM_IC_GENERATOR} -h

## Run the IC generator
echo "$ "/usr/bin/time python ${PHOSIM_IC_GENERATOR} $options
/usr/bin/time python ${PHOSIM_IC_GENERATOR} $options
rc=$?

echo "InstanceCatalog generation complete"
date

exit $rc

