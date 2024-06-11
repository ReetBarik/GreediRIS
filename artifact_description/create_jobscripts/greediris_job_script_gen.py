# python3 strong_scaling_jobs.py <ACCOUNT> <#NODES> <DATASET> <DIRECTED> <DIFFUSION MODEL>


import sys
import os


def write_greediris_job_script(account, nodes, dataset, directed_flag, model, k, alpha):
    job_name = f"m{nodes}_{model}_{dataset}"
    if alpha != "": 
        job_name += f"_a{alpha*100}"

    output_path = os.path.abspath('../results/strong_scaling/' + dataset + f'/{job_name}')
    tool_path = os.path.abspath('../../build/release/tools/mpi-greedimm')
    dataset_path = os.path.abspath('../datasets/' + dataset + '_binary.txt')

    script = f'''#!/bin/bash

    #SBATCH -A {account}
    #SBATCH -C cpu
    #SBATCH -t 01:00:00
    #SBATCH -q regular
    #SBATCH -N {nodes}
    #SBATCH --ntasks-per-node=1
    #SBATCH -J {job_name} 
    #SBATCH -o {output_path}.o
    #SBATCH -e {output_path}.e

    module use /global/common/software/m3169/perlmutter/modulefiles

    #OpenMP settings:
    export OMP_NUM_THREADS=64
    export OMP_PLACES=threads
    export OMP_PROC_BIND=spread

    module load python/3.9-anaconda-2021.11
    module load gcc/11.2.0
    module load cmake/3.24.3
    module load cray-mpich
    module load cray-libsci

    srun -n {nodes} {tool_path} -i {dataset_path} -w -k {k} -p {directed_flag} -d {model} -e 0.13 -o {output_path}.json --run-streaming=true --epsilon-2=0.077 --reload-binary'''

    if alpha != "":
        script += f" --alpha={alpha}"

    with open(f'{job_name}.sh', 'w') as f:
        f.write(script)

if __name__ == "__main__":
    account = sys.argv[1]
    nodes = sys.argv[2]
    dataset = sys.argv[3]
    directed_flag = '-u' if sys.argv[4] == '1' else ''
    model = sys.argv[5]
    k = sys.argv[6]
    alpha = ""
    if len(sys.argv) == 8:
        alpha = sys.argv[7]

    script = write_greediris_job_script(account, nodes, dataset, directed_flag, model, k, alpha)

