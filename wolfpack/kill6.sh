#! /bin/bash

PIDS=$(ps -A | grep "python" | grep -v grep | awk '{print $1}')
for pid in $PIDS
do
	kill "$pid"
done
