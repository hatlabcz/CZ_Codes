----------------------------------------------------------------------------------
-- Company: Hatlab@Pitt
-- Author : Chao Zhou
-- Reference : Meyer-Baese, Uwe. Digital signal processing with field programmable gate arrays. Springer Science & Business Media, 2007. P101
-- Create Date: 07/25/2018

----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_arith.all;



entity Devision is
  generic(
    WN : integer := 16;   --1 integer plus 15 fractional bits
	WD : integer := 16;
	max_shift : integer := 4;  --log2(max(WD,WN))  or Width(binary(max(WN,WD))-1
	steps : integer := 3;
	TWO : integer := 65536;     --2**WN
	PO2WN : integer := 32768;  --2**(WN-1)
	PO2WN2 : integer := 131071  --2**(WN+1)-1
  );


  port(
    N_in  : in std_logic_vector(WN-1 downto 0);
	D_in  : in std_logic_vector(WD-1 downto 0);
	sign  : in std_logic;
	bit_shift : in std_logic_vector (max_shift downto 0);
	
	Q_out : out std_logic_vector(WD-1 downto 0):= "0000000000000000";
	clk : in std_logic;
	rst : in std_logic
  );
end Devision; 
  
architecture fpga of Devision is
  
  subtype word is integer range 0 to PO2WN2;
  
  type state_type is (s0, s1, s2);
  signal state : state_type;
  
begin

  states : process(rst, clk)
	  variable x,t,f : word :=0;
	  variable count : integer range 0 to steps;
  
	  begin
		if rst = '1' then
			state <= s0;
			q_out <=(others => '0');--------------------------------------
		else
			if(clk'event and clk = '1') then
				case state is
				  when s0 =>
					state <= s1;
					count := 0;
					t := conv_integer(D_in);
					x := conv_integer(N_in);
				  when s1 => 
					f := TWO-t;
					x := x * f / PO2WN;
					t := t * f / PO2WN;
					count := count+1;
					if count = steps then
						state <= s2;
					else
						state <= s1;
					end if;
				  when s2=>
					q_out <= conv_std_logic_vector(x,WN);
					state <= s0;
				end case;
			end if;
		end if;
	  end process states;

end fpga;
	
			
			  

  
  