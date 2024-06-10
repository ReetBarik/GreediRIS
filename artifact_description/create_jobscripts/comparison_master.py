# Script to generate job scripts for all experiments in Table 5: Comparison of GreeDIMM with Ripples and IMM-mt. 
# python3 comparison_master.py <ACCOUNT>

import sys
import subprocess
from greediris_job_script_gen import write_greediris_job_script
from imm_job_script_gen import write_imm_job_script

def build_comparision_jobs(account):
	nodes = 512
	models = ['LT', 'IC']
	directed_datasets = ['HepPh', 'Pokec', 'livejournal', 'friendster']
	undirected_datasets = ['github', 'DBLP', 'orkut_small', 'orkuk_big', 'wikipedia']

	for d in directed_datasets + undirected_datasets:
		for model in models:
			directed_flag = '1' if d in undirected_datasets else '0'
			write_greediris_job_script(account, nodes + 1, d, directed_flag, model, "")
			write_greediris_job_script(account, nodes + 1, d, directed_flag, model, "0.125")
			write_imm_job_script(account, nodes, d, directed_flag, model, "")
			# still need to add DIiMM scripts

if __name__ == "__main__": 
	account = sys.argv[1]
	build_comparision_jobs(account)