# Script to generate job scripts for all experiments in Table 6: GreeDIMM-trunc: Runtime of the seed selection step (in sec)
# as a function of 𝛼—the fraction of seeds sent from each sender for Orkut with m = 128.
# python3 truncated_master.py <ACCOUNT>

import sys
from greediris_job_script_gen import write_greediris_job_script

def build_truncated_master(account):
	nodes = 512
	dataset = 'friendster'
	alpha = [100, 50, 25, 0.125]
	k = 1000

	for a in alpha:
		write_greediris_job_script(account, nodes + 1, dataset, "0", "IC", k, a)

if __name__ == "__main__": 
	account = sys.argv[1]
	build_truncated_master(account)