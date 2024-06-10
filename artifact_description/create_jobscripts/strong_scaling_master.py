# Script to generate job scripts for all experiments in Table 4: Strong scaling performance of GreeDIMM for different inputs,
# varying m up to 1,024 nodes. 
# python3 strong_scaling_master.py <ACCOUNT>

import sys
from greediris_job_script_gen import write_greediris_job_script
from imm_job_script_gen import write_imm_job_script

def build_scaling_master(account):
	nodes = [8, 16, 32, 64, 128, 256, 512, 1024]
	k = 100

	directed_datasets = ['Pokec', 'livejournal', 'friendster']
	undirected_datasets = ['orkut_small', 'orkuk_big', 'wikipedia']
	for d in directed_datasets + undirected_datasets:
		for n in nodes:
			directed_flag = '1' if d in undirected_datasets else '0'
			if ((d == 'wikipedia' or d == 'friendster') and (n < 65)):
				continue
			else:
				write_greediris_job_script(account, n + 1, d, directed_flag, model, k, "")
				write_greediris_job_script(account, n + 1, d, directed_flag, model, k, "0.125")
				write_imm_job_script(account, n, d, directed_flag, model)
				# still need to add DIiMM scripts

if __name__ == "__main__": 
	account = sys.argv[1]
	build_scaling_master(account)