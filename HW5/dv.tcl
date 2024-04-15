gui_start
analyze -library WORK -format verilog {/home/010/s/sx/sxc210186/synopsys/WORK/hw5/scan.v}
elaborate circuit -architecture verilog -library WORK
write -hierarchy -format ddc
read_file -format ddc {/home/010/s/sx/sxc210186/synopsys/WORK/hw5/circuit.ddc}
compile -exact_map -only_design_rule
set_scan_configuration -style multiplexed_flip_flop
set_scan_configuration -chain_count 1
set_dft_signal -view existing_dft -type ScanClock -port clk -timing {1 10}
create_test_protocol -capture_procedure single_clock
insert_dft
current_design
dft_drc -verbose
check_design -multiple_designs
write_test_protocol -o file_scan.stil
write -hierarchy -format verilog -output file_scan.