#!/usr/local/bin/python2.7
for x in range(1000):
	call("sbatch","Rscript","src/analysis_parallelTests.R")