# Generate plots

The scripts in this directory can be used to generate the plots shown in Figures 3, 4, and 5 of the article. 
Figure 3 shows the better scaling behavior of GreediRIS and GreediRIS-trunc compared to that of Ripples for a representative input. Figure 4 shows the parallel runtime breakdown of the receiver, longest running sender, and the total runtime for GreediRIS. Figure 5 (a) and (b) shows the scaling behavior of GreediRIS and GreediRIS-trunc respectively with the seed-selection step shown as a shaded fraction of the total runtime. 

The command to generate the plots in Figures 3, 4, and 5 are: `python3 plot_master.py`

This will result in the generation of the following:
* Figure3.PDF -- corresponding to the scaling plot in Figure 3 in the article.
* Figure4_livejournal_breakdown.PDF -- corresponding to the breakdown plot in Figure 4 in the article.
* Figure5.PDF -- corresponding to the truncated plot in Figure 5 in the article.

