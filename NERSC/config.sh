# config.sh - general set up for phoSim task

## Prepare for phoSim

## Git repository containing visit lists and instanceCatalog generator
export DC2_ROOT='/global/projecta/projectdirs/lsst/production/DC2'
export DC2_REPO=${DC2_ROOT}'/DC2_Repo/scripts/protoDC2'

## Select which to use for this task (u,g,r,i,z,y)
export DC2_REPO_FILTER_LIST="u g r i z y"
export DC2_REPO_FILTER=u

## Visit lists
export DC2_VISIT_DB=${DC2_REPO}/"protoDC2_visits_${DC2_REPO_FILTER}-band.txt"


echo 'DC2_VISIT_DB = '$DC2_VISIT_DB

##
### Instance Catalog
##
export PHOSIM_IC_GEN='DYNAMIC'
export PHOSIM_IC_GENERATOR=${DC2_REPO}'/generateDc2InstCat.py'
export PHOSIM_IC_GCR_CATALOGS=${DC2_ROOT}'/gcr-catalogs'

## Dynamic Instance Catalogs...
### OpSim DB for generating instanceCatalog
export DC2_OPSSIM_DB='/global/projecta/projectdirs/lsst/groups/SSim/DC1/minion_1016_sqlite_new_dithers.db'

## minimum magnitude (max brightness) for objects in sky catalog
export DC2_MINMAG=10.0


## Static Instance Catalogs...
## 3/27/2017 - Mustafa's private scratch area for collecting instanceCatalogs
#export PHOSIM_CATALOGS="/global/cscratch1/sd/mustafa/DC2-phoSim-3"
## 11/13/2017 - Test DC2 area for instanceCatalogs
export PHOSIM_CATALOGS="/global/cscratch1/sd/descpho/Pipeline-tasks/DC2-phoSim-1/catalogs"


DC2base=`dirname ${DC2_ROOT}`
#export PHOSIM_SEDS=${DC2base}/SEDs
#export PHOSIM_SEDS='/global/common/cori/contrib/lsst/lsstDM/w.2016.20/lsstsw/stack/Linux64/sims_sed_library/12.0'
#export PHOSIM_SEDS='/global/projecta/projectdirs/lsst/production/DC2/phoSim-data/SEDs'
export PHOSIM_COMMANDS=${DC2_CONFIGDIR}/commands.txt

###SEDLIB = '/nfs/farm/g/lsst/u1/software/redhat6-x86_64-64bit-gcc44/DMstack/v12_0/opt/lsst/sims_sed_library'

## Global and persistent scratch space to where phoSim 'work' directory will be staged
export PHOSIM_SCR_ROOT=/global/cscratch1/sd/descpho/Pipeline-tasks/${TASKNAME}
#export PHOSIM_SCR_ROOT=${SCRATCH}/Pipeline-tasks/${TASKNAME}
## Flag for cleaning up $SCRATCH after visit is complete (0=disable, 1=enable)
export PHOSIM_SCR_CLEANUP=0

## Enable or disable the E2ADC step (0=disable, 1=enable)
export PHOSIM_E2ADC=0

## For setting up phoSim and DMTCP outputs
export filePermissions="02775"     #   rwxrwxr-x



