
import sys
import subprocess

datasets = ['livejournal']

for d in datasets:
	command1 = 'python3 greedi_plots.py --data ' + d + '_data.csv --output Figure4_' + d + '_breakdown.PDF'  
	subprocess.call(command1.split())


command2 = 'python3 truncated.py'
subprocess.call(command2.split())

command3 = 'python3 scaling.py'
subprocess.call(command3.split())
