#!/bin/bash
python scripts/compute-stats.py results/delay/bess-container* > computed/delay/bess-container
python scripts/compute-stats.py results/delay/bess-vm* > computed/delay/bess-vm
python scripts/compute-stats.py results/delay/bess-isol-container* > computed/delay/bess-isol-container
python scripts/compute-stats.py results/delay/ovs-vm* > computed/delay/ovs-vm
python scripts/compute-stats.py results/delay/ovs-containwe* > computed/delay/ovs-container
python scripts/compute-stats.py results/delay/zcsi* > computed/delay/zcsi
python scripts/combine-files.py -c "Median_rx" -c "P95_rx" -c "P99_rx" "computed/delay/bess-container,Bess Container" \
"computed/delay/bess-isol-container,Bess Container w/Copy" "computed/delay/bess-vm,Bess VM" \
"computed/delay/ovs-container,OVS Container" "computed/delay/ovs-vm,OVS VM" "computed/delay/zcsi,ZCSI" > \
computed/delay/delay-all
