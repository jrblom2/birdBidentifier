#!/bin/bash
while :
do
	arecord -D hw:1,0 -f S32_LE -c 2 -d 10 input.mp3
	python3 testRun.py
done