#!/bin/bash
declare -a arr

for value in {0..3}
do
	arr[$value]=$(cat /sys/devices/system/cpu/cpu$value/cpufreq/scaling_governor)
done 
for value in {0..3}
do
	echo ${arr[$value]}
done
for value in {0..3}
do
	cpufreq-set -c $value -g performance
done
python3 gameplay.py
for value in {0..3}
do
	cpufreq-set -c $value -g ${arr[$value]}
done


