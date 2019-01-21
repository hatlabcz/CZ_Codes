----------------------------------------------------------------------------------
-- Company: Hatlab@Pitt
-- Author : Chao Zhou
-- Reference : Meyer-Baese, Uwe. Digital signal processing with field programmable gate arrays. Springer Science & Business Media, 2007. P101
-- Create Date: 07/25/2018
-- Description : Following the method in reference, we change it to a pipeline form. The input should be connected to the output of Div_FormConv, 
--               which gives this block an suitable logic_vector that can make the iteration converge faster. Finally the result will be reducted
--               to the real quotient base on the sign and bit_shift input.
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.numeric_std.all;--



entity Division_pl is
  generic(
    WN : integer := 16;   --1 integer plus 15 fractional bits
	WD : integer := 16;
	max_shift : integer := 3;  --log2(max(WD,WN))-1  or Width(binary(max(WN,WD))-1
	TWO : integer := 65536;     --2**WN
	PO2WN : integer := 32768;  --2**(WN-1)
	PO2WN2 : integer := 131071  --2**(WN+1)-1
  );


  port(
    N_in  : in std_logic_vector(WN-1 downto 0);
	D_in  : in std_logic_vector(WD-1 downto 0);
	sign  : in std_logic;
	bit_shift : in std_logic_vector (max_shift downto 0);
	
	Q_out : out std_logic_vector(WD-1 downto 0):= (others => '0');
	clk : in std_logic;
	rst : in std_logic
  );
end Division_pl; 
  
architecture fpga of Division_pl is
  
  subtype word is integer range 0 to PO2WN2;
  signal x0,x1,x2,x3,x4,x5,x6,x7 : word :=0;
  signal t0,t1,t2,t3,t4,t5,t6,t7 : word :=0;
  signal b0,b1,b2,b3,b4,b5,b6,b7 : integer range 0 to 32 :=0;
  signal s0,s1,s2,s3,s4,s5,s6,s7 : std_logic :='0';
  signal D0,D1,D2,D3,D4,D5,D6,D7 : std_logic_vector(WD-1 downto 0):=(others => '0');
  signal N0,N1,N2,N3,N4,N5,N6,N7 : std_logic_vector(WD-1 downto 0):=(others => '0');
  
  --signal Q_temp : unsigned(WD-1 downto 0):= (others => '0');
 -- signal f0,f1,f2,f3,f4,f5 : word :=0;
  
  
begin

  divide: process(rst, clk)
	  --variable x0,x1,x2,x3,x4,x5 : word :=0;
	  --variable t0,t1,t2,t3,t4,t5 : word :=0;
	  variable f0,f1,f2,f3,f4,f5,f6,f7 : word :=0;
	  variable Q_temp : unsigned(WD-1 downto 0):= (others => '0');
	  begin
		if rst = '1' then
			Q_out <=(others => '0');
			x0 <= 0; x1 <= 0; x2 <= 0; x3 <= 0; x4 <= 0; x5 <= 0; x6 <= 0;x7 <= 0;
			t0 <= 0; t1 <= 0; t2 <= 0; t3 <= 0; t4 <= 0; t5 <= 0; t6 <= 0;t7 <= 0;
			b0 <= 0; b1 <= 0; b2 <= 0; b3 <= 0; b4 <= 0; b5 <= 0; b6 <= 0; b7 <= 0;
			s0 <= '0'; s1 <= '0'; s2 <= '0'; s3 <= '0'; s4 <= '0'; s5 <= '0'; s6 <= '0'; s7 <= '0';
			f0 := 0; f1 := 0; f2 := 0; f3 := 0; f4 := 0; f5 := 0; f6 := 0;f7 := 0;
			D0 <=(others => '0');D1 <=(others => '0');D2 <=(others => '0');D3 <=(others => '0');D4 <=(others => '0');D5 <=(others => '0');D6 <=(others => '0');D7 <=(others => '0');
			N0 <=(others => '0');N1 <=(others => '0');N2 <=(others => '0');N3 <=(others => '0');N4 <=(others => '0');N5 <=(others => '0');N6 <=(others => '0');N7 <=(others => '0');
			Q_temp := (others => '0');
			
		else
			if(clk'event and clk = '1') then	
				t0 <= to_integer(unsigned(D_in));
				x0 <= to_integer(unsigned(N_in));
				b0 <= to_integer(unsigned(bit_shift));
				s0 <= sign;
				D0 <= D_in;
				N0 <= N_in;
				
				f0 := TWO - t0;
				x1 <= x0 * f0 / PO2WN;
				t1 <= t0 * f0 / PO2WN;
				b1 <= b0;
				s1<=s0;
				D1 <= D0;
				N1 <= N0;
				f1 := TWO - t1;
				x2 <= x1 * f1 / PO2WN;
				t2 <= t1 * f1 / PO2WN;
				b2 <= b1;
				s2<=s1;
				D2 <= D1;
				N2 <= N1;
				f2 := TWO - t2;
				x3 <= x2 * f2 / PO2WN;
				t3 <= t2 * f2 / PO2WN;
				b3 <= b2;
				s3<=s2;
				D3 <= D2;
				N3 <= N2;
				f3 := TWO - t3;
				x4 <= x3 * f3 / PO2WN;
				t4 <= t3 * f3 / PO2WN;
				b4 <= b3;
				s4<=s3;
				D4 <= D3;
				N4 <= N3;
				f4 := TWO - t4;
				x5 <= x4 * f4 / PO2WN;
				t5 <= t4 * f4 / PO2WN;
				b5 <= b4;
				s5 <= s4;
				D5 <= D4;
				N5 <= N4;
				f5 := TWO - t5;
				x6 <= x5 * f5 / PO2WN;
				t6 <= t5 * f5 / PO2WN;
				b6 <= b5;
				s6 <= s5;
				D6 <= D5;
				N6 <= N5;
				f6 := TWO - t6;
				x7 <= x6 * f6 / PO2WN;
				t7 <= t6 * f6 / PO2WN;
				b7 <= b6;
				s7 <= s6;
				D7 <= D6;
				N7 <= N6;
				f7 := TWO - t7;
				
				
				if (D7(WD-1 downto WD-7) = "1111111" or D7(WD-1 downto WD-9) = "111111011" ) then	--D_in/PO2WN > 1.98, converge very slow ,just assume D_in = TWO
					Q_temp := unsigned(N7);
					if s7 ='0' then
						Q_out <= std_logic_vector(shift_right(Q_temp, b7+1));   --   b7+1 : "+1" means using bit shift to represent "devide by TWO"
					else 
						--Auusume Denorminator is always graeator than Norminator. So the first bit after shift will always be 0
						Q_out <= not(std_logic_vector(shift_right(Q_temp, b7+1)))+1;                     
					end if;
				else 
					Q_temp := to_unsigned(x7 * f7 / PO2WN,WN);
					if s7 ='0' then
						Q_out <= std_logic_vector(shift_right(Q_temp, b7));    
					else 
						--Auusume Denorminator is always graeator than Norminator. So the first bit after shift will always be 0
						Q_out <= not(std_logic_vector(shift_right(Q_temp, b7)))+1;   
					end if;
				end if;
			end if;
		end if;
	  end process divide;
 
end fpga;
	
