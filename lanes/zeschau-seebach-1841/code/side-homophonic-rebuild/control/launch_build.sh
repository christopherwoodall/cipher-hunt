#!/bin/bash
# Detached launcher for the rebuild-fleet synthetic control build.
# Survives exec-session SIGTERM: setsid detaches the process group;
# per-seed checkpoints let it resume after any kill.
D=/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild/control
cd "$D"
exec setsid nohup python3 build_rebuild_instances.py > build_rebuild_instances.log 2>&1 < /dev/null
