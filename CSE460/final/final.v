module alu(clk, reset, srcA, srcB, opCode, aluResult, zero, carryx, sign);

input clk, reset;
input [3:0] srcA, srcB;
input [2:0] opCode;

output reg [3:0] aluResult;
output reg zero, carryx, sign;

reg [1:0] state;

always @(posedge clk, posedge reset)
begin
	if (reset == 1)
		state = 2'b00;
	else
	begin
		case(opCode)
		
			3'b000:	//reset
				state = 2'b00;
			3'b001:	//xor
			begin
				case(state)
					2'b00:
					begin
						aluResult[0] = srcA[0]^srcB[0];
						state = 01;
					end
					2'b01:
					begin
						aluResult[1] = srcA[1]^srcB[1];
						state = 10;
					end
					2'b10:
					begin
						aluResult[2] = srcA[2]^srcB[2];
						state = 11;
					end
					2'b11:
					begin
						aluResult[3] = srcA[3]^srcB[3];
						state = 00;
					end
					default: state = 2'b00;
				endcase
				zero = !(|aluResult);
				carryx = 0;
				sign = aluResult[3];
			end
			
			
			3'b100:	//sub
			begin
				case(state)
					2'b00:
					begin
						carryx = 0;
						aluResult[0] = (srcA[0]^srcB[0])^carryx;
						carryx = (((~srcA[0])&srcB[0])|((~srcA[0])&carryx)|(scrB[0]&carryx));
						state = 01;
					end
					2'b01:
					begin
						aluResult[1] = (srcA[1]^srcB[1])^carryx;
						carryx = ((~srcA[1])&srcB[1])|((~srcA[1])&carryx)|(scrB[1]&carryx));
						state = 10;
					end
					2'b10:
					begin
						aluResult[2] = (srcA[2]^srcB[2])^carryx;
						carryx = (((~srcA[2])&srcB[2])|((~srcA[2])&carryx)|(scrB[2]&carryx));
						state = 11;
					end
					2'b11:
					begin
						aluResult[3] = (srcA[3]^srcB[3])^carryx;
						carryx = ((~srcA[3])&srcB[3])|((~srcA[3])&carryx)|(scrB[3]&carryx);
						state = 00;
					end
					default: state = 2'b00;
				endcase
				zero = !(|aluResult);
				carryx = 0;
				sign = aluResult[3];
			end			
			
			default: state = 2'b00;
		endcase
	end
end
endmodule