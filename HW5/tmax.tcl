read_netlist /home/010/s/sx/sxc210186/synopsys/WORK/hw5/class.v -library
read_netlist /home/010/s/sx/sxc210186/synopsys/WORK/hw5/file_scan.v
run_build_model circuit
set_drc /home/010/s/sx/sxc210186/synopsys/WORK/hw5/file_scan.stil
run_drc
add_faults -all
run_atpg -ndetects 1