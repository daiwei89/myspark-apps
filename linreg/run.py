#!/usr/bin/env python

import os
from os.path import dirname
from os.path import join
import time

master_ip = "10.54.1.36"
data_path = "/nfs/nas-0-16/wdai/datasets/class/binary/a1a/a1a.train.0"
driver_memory = "32g"

num_iterations = 10
step_size = 1e-7
reg_type = "NONE" # Options: L1, L2, NONE
reg_lambda = 0
data_format = "LibSVM"
minibatch_fraction = 1
num_legs = 1
num_dups = 1
num_parallelism = 16

script_dir = dirname(os.path.realpath(__file__))

cmd = "time spark-submit"
cmd += " --class LogisticRegression"
cmd += " --master spark://%s:7077" % master_ip
cmd += " --driver-memory " + driver_memory
cmd += " %s/target/linreg-1.0.jar" % script_dir
cmd += " --numIterations " + str(num_iterations)
cmd += " --stepSize " + str(step_size)
cmd += " --regType " + reg_type
cmd += " --regParam " + str(reg_lambda)
cmd += " --minibatchFraction " + str(minibatch_fraction)
cmd += " --dataFormat " + data_format
cmd += " --numLegs " + str(num_legs)
cmd += " --numDups " + str(num_dups)
cmd += " --numParallelism " + str(num_parallelism)
cmd += " " + data_path

print cmd
os.system(cmd)
