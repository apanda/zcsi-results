#!/bin/bash
python scripts/compute-stats.py results/size/bess-container-* > computed/size/bess-container
python scripts/compute-stats.py results/size/bess-vm-* > computed/size/bess-vm
python scripts/compute-stats.py results/size/bess-isol-container-* > computed/size/bess-isol-container
python scripts/compute-stats.py results/size/ovs-vm-* > computed/size/ovs-vm
python scripts/compute-stats.py results/size/ovs-container-* > computed/size/ovs-container
python scripts/compute-stats.py results/size/zcsi-clean > computed/size/zcsi
python scripts/combine-files.py -c "Median_rx" -c "P95_rx" -c "P99_rx" "computed/size/bess-container,Bess Container" \
"computed/size/bess-isol-container,Bess Container w/Copy" "computed/size/bess-vm,Bess VM" \
"computed/size/ovs-container,OVS Container" "computed/size/ovs-vm,OVS VM" "computed/size/zcsi,ZCSI" > \
computed/size/size-all
