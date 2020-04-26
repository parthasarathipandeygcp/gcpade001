#!/bin/bash

gsutil cp gs://sd_freeway_data/SD_5min.csv raw.csv
python to_messages.py
gsutil cp messages.csv.gz gs://psp-class-stream/sandiego/sensor_obs.csv.gz
