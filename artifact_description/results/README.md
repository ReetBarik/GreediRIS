# Results

This directory contains the experimental outputs generated from all the runs conducted on the NERSC Perlmutter supercomputer. Scripts to parse the logs to generate the CSVs and PDFs corresponding to the tables and plots respectively in Section 4 can be found in the directory `/artifact_description/create_figures/`.

The outputs for each experiment are split into three distinct files
- The `<experiment>.json` file contains the output of an experiment. 
- The `<experiment>.o` file contains the diagnostic information collected during the runtime of the experiment. 
- The `<experiment>.e` is populated if an error occures during the runtime of the experiment. 

The experimental results used in the article are divided into three subdirectories;
- `/imm/` and `/diimm/` contains the experimental results for the `Ripples` and `DiIMM` columns repectively in table 4. 
- `/strong_scaling/` contains the experimental results for 
  - the results for the `GreediRIS` column in table 4
  - table 5
  - figure 3 and figure 4
- `/truncated/` contains the experimental results for figure 5
