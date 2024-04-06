`include "gtech_lib.v"
module circuit(X,Z);
input x;
output z;

wire ;

GTECH_AND2 G1(x,y1,c3);
GTECH_OR3 G2(x,y2,y3,c4);
GTECH_AND2 G3(c3,c4,c5);
GTECH_OR2 G4(c5,y2,c8);
GTECH_AND2 G5(c5,y3,c9);
GTECH_AND2 G6(c8,c9);
GTECH_NOT G7(c8,z);

endmodule