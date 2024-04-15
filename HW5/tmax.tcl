read_netlist ./class.v -library
read_netlist ./file_scan.v
run_build_model circuit
set_drc ./file_scan.stil
run_drc
add_faults -all
run_atpg -ndetects 1