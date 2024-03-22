read_netlist /home/010/s/sx/sxc210186/synopsys/WORK/hw3/gtech_lib.v -library
read_netlist /home/010/s/sx/sxc210186/synopsys/WORK/hw3/fig_8-13.v 
set_build -merge nomux_from_gates
run_build_model circuit8r
run_drc
set_faults -model path_delay -report collapsed -fault_coverage -summary verbose
add_delay_paths /home/010/s/sx/sxc210186/synopsys/WORK/hw3/nr.txt
remove_faults -all
add_faults -all
run_atpg -ndetects 1
report_delay_paths -all
report_delay_paths path2f -display -pindata
report_patterns -all -internal
report_patterns -all -internal -path_delay