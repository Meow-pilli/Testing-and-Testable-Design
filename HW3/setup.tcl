read_netlist /home/010/s/sx/sxc210186/synopsys/WORK/hw3/gtech_lib.v
read_netlist /home/010/s/sx/sxc210186/synopsys/WORK/hw3/fig_8-13.v -library
run_build_model circuit8r
run_drc
set_faults -model path_delay -report collapsed -fault_coverage -summary verbose
add_delay_paths /home/010/s/sx/sxc210186/synopsys/WORK/hw3/non-robust.txt
add_faults -all
run_atpg -ndetects 1
report_patterns -all -internal -path_delay
report_patterns -all -internal
write_patterns /home/010/s/sx/sxc210186/synopsys/WORK/hw3/output_patterns -internal -format stil99 -cycle_count -nopatinfo -parallel 0 -cellnames parallel
