#!/usr/local/bin/python2.7
from subprocess import call

for x in range(1000):
	call(["sbatch","src/slurmParallel.sh"])