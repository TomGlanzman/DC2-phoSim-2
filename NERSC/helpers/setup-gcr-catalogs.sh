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

export PHOSIM_IC_GCR_CATALOGS=/global/projecta/projectdirs/lsst/production/DC2/gcr-catalogs

echo "$ "eups declare gcr_catalogs -r ${PHOSIM_IC_GCR_CATALOGS}  -c
eups declare gcr_catalogs -r ${PHOSIM_IC_GCR_CATALOGS}  -c

echo "$ "setup gcr_catalogs
setup gcr_catalogs

echo "$ "eups list -v gcr_catalogs
eups list -v gcr_catalogs



echo "$ "cd ${PHOSIM_IC_GCR_CATALOGS}/GCRCatSimInterface/data
cd ${PHOSIM_IC_GCR_CATALOGS}/GCRCatSimInterface/data
echo "$ "python get_sed_mags.py
python get_sed_mags.py



#export PYTHONPATH=${PHOSIM_IC_GCR_CATALOGS}
#python "import GCRCatSimInterface; print(GCRCatSimInterface.__version__)"




date



