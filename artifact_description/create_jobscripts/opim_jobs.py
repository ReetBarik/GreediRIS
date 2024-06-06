#!/bin/bash

#SBATCH -A m3083
#SBATCH -C cpu
#SBATCH -t 01:00:00
#SBATCH -q regular
#SBATCH -N 513
#SBATCH --ntasks-per-node=1
#SBATCH -J a125_m513_opimc_streaming_friendster_IC_1000
#SBATCH -o /pscratch/sd/r/reetb/results/opimc/friendster/a125_m513_opimc_streaming_friendster_IC_1000.o
#SBATCH -e /pscratch/sd/r/reetb/results/opimc/friendster/a125_m513_opimc_streaming_friendster_IC_1000.e

# module use /global/common/software/m3169/perlmutter/modulefiles
module use /global/common/software/m3169/perlmutter/modulefiles

#OpenMP settings:
export OMP_NUM_THREADS=64
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

#module load PrgEnv-cray
# module load python/3.9-anaconda-2021.11
module load gcc/11.2.0
module load cmake/3.24.3
module load cray-mpich
module load cray-libsci
#module load openmpi
#module load cudatoolkit/11.0

cp /global/cfs/cdirs/m1641/network-data/Binaries/friendster_IC_binary.txt /pscratch/sd/r/reetb/

srun -n 513 /global/homes/r/reetb/GreeDIMM/build/release/tools/mpi-greedimm -i /pscratch/sd/r/reetb/friendster_IC_binary.txt -w -k 1000 -p -d IC -e 0.01 -o /pscratch/sd/r/reetb/results/opimc/friendster/a125_m513_opimc_streaming_friendster_IC_1000.json --reload-binary -u --opimc=1 --epsilon-2=0.0562 --alpha=0.125 --pessimistic_approximation=true

cp /pscratch/sd/r/reetb/results/opimc/friendster/a125_m513_opimc_streaming_friendster_IC_1000.* /global/homes/r/reetb/results/opimc/friendster/
