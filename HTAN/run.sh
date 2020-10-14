#!/bin/bash
for json in `cat jsons.rerun.txt`
do
    caper submit /opt/atac-seq-pipeline/atac.wdl -i $json --port 8000
done
