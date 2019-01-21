----------------------------------------------------------------------------------
-- Company: Hatlab@Pitt
-- Author : Chao Zhou
-- Reference : 
-- Create Date: 07/26/2018
-- Description : Change the incoming signal into the form that is suitable for the Divison block(1.15 bit_shift, i.e. 1 integer 15 fractional bits). 
--               1)Use XOR gate to find the sign of result 
--               2)Convert the input to abs value,Find MSB and shift it to the first bit
--               3)Record the difference of number of bits shiffted for final reduction.
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.numeric_std.all;


entity Div_FormConv is
  port(
	N_in  : in std_logic_vector(15 downto 0);
	D_in  : in std_logic_vector(15 downto 0);   --Assume 16 bits income
	
	sign      : out std_logic := '0';
	bit_shift : out std_logic_vector (3 downto 0) := "0000";  --Also assume Denorminator is always graeator than Norminator
	
	N_out     : out std_logic_vector(15 downto 0):= (others => '1');
	D_out     : out std_logic_vector(15 downto 0):= (others => '1');
	
	clk : in std_logic;
	rst : in std_logic
  );
end Div_FormConv;

architecture fpga of Div_FormConv is
  
  signal MSB_N : integer :=0;
  signal MSB_D : integer :=0;
  

begin


STEP1_sign: process(clk, rst)
			begin
				if(rst = '1') then
					sign <= '0';
				else
					if(clk'event and clk = '1') then	
						sign <= N_in(15) xor D_in(15);	
					end if;
				end if;
			  end process;
  
  
STEP2_N:    process(clk, rst)
			  variable N_in_abs  : std_logic_vector(15 downto 0) :=(others => '0');
			  variable N_out_temp : std_logic_vector(15 downto 0) :=(others => '0');
			begin
				if(rst = '1') then
					N_out <= (others => '0');
					MSB_N <= 0;
					N_in_abs := (others => '0');
					N_out_temp := (others => '0');
				
				else
					if(clk'event and clk = '1') then	
					
						if N_in(15)='1' then
							N_in_abs := not N_in +1;
						else
							N_in_abs := N_in; 
						end if;
					
						if N_in_abs(15) = '1' then
							N_out_temp := N_in_abs(15 downto 0);
							MSB_N <= 15;
						elsif N_in_abs(14) = '1' then
							N_out_temp := N_in_abs(14 downto 0) & '0';
							MSB_N <= 14;
						elsif N_in_abs(13) = '1' then
							N_out_temp := N_in_abs(13 downto 0) & "00";
							MSB_N <= 13;
						elsif N_in_abs(12) = '1' then
							N_out_temp := N_in_abs(12 downto 0) & "000";
							MSB_N <= 12;
						elsif N_in_abs(11) = '1' then
							N_out_temp := N_in_abs(11 downto 0) & "0000";
							MSB_N <= 11;
						elsif N_in_abs(10) = '1' then
							N_out_temp := N_in_abs(10 downto 0) & "00000";
							MSB_N <= 10;
						elsif N_in_abs(9) = '1' then
							N_out_temp := N_in_abs(9 downto 0) & "000000";
							MSB_N <= 9;
						elsif N_in_abs(8) = '1' then
							N_out_temp := N_in_abs(8 downto 0) & "0000000";
							MSB_N <= 8;
						elsif N_in_abs(7) = '1' then
							N_out_temp := N_in_abs(7 downto 0) & "00000000";
							MSB_N <= 7;
						elsif N_in_abs(6) = '1' then
							N_out_temp := N_in_abs(6 downto 0) & "000000000";
							MSB_N <= 6;
						elsif N_in_abs(5) = '1' then
							N_out_temp := N_in_abs(5 downto 0) & "0000000000";
							MSB_N <= 5;
						elsif N_in_abs(4) = '1' then
							N_out_temp := N_in_abs(4 downto 0) & "00000000000";
							MSB_N <= 4;
						elsif N_in_abs(3) = '1' then
							N_out_temp := N_in_abs(3 downto 0) & "000000000000";
							MSB_N <= 3;
						elsif N_in_abs(2) = '1' then
							N_out_temp := N_in_abs(2 downto 0) & "0000000000000";
							MSB_N <= 2;
						elsif N_in_abs(1) = '1' then
							N_out_temp := N_in_abs(1 downto 0) & "00000000000000";
							MSB_N <= 1;
						else
							N_out_temp := "1000000000000000";  -- avoid 0
							MSB_N <= 0;
						end if;
					end if;
				end if;
				N_out <= N_out_temp;
			  end process;
 
STEP2_D:    process(clk, rst)
			  variable D_in_abs  : std_logic_vector(15 downto 0) :=(others => '0');
			  variable D_out_temp : std_logic_vector(15 downto 0) :=(others => '0');
			begin
				if(rst = '1') then
					D_out <= (others => '0');
					MSB_D <= 0;
					D_in_abs := (others => '0');	
					D_out_temp := (others => '0');
				else
					if(clk'event and clk = '1') then
						
						if D_in(15)='1' then
							D_in_abs := not D_in +1;
						else
							D_in_abs := D_in; 
						end if;

						if D_in_abs(15) = '1' then
							D_out_temp := D_in_abs(15 downto 0);
							MSB_D <= 15;
						elsif D_in_abs(14) = '1' then
							D_out_temp := D_in_abs(14 downto 0) & '0';
							MSB_D <= 14;
						elsif D_in_abs(13) = '1' then
							D_out_temp := D_in_abs(13 downto 0) & "00";
							MSB_D <= 13;
						elsif D_in_abs(12) = '1' then
							D_out_temp := D_in_abs(12 downto 0) & "000";
							MSB_D <= 12;
						elsif D_in_abs(11) = '1' then
							D_out_temp := D_in_abs(11 downto 0) & "0000";
							MSB_D <= 11;
						elsif D_in_abs(10) = '1' then
							D_out_temp := D_in_abs(10 downto 0) & "00000";
							MSB_D <= 10;
						elsif D_in_abs(9) = '1' then
							D_out_temp := D_in_abs(9 downto 0) & "000000";
							MSB_D <= 9;
						elsif D_in_abs(8) = '1' then
							D_out_temp := D_in_abs(8 downto 0) & "0000000";
							MSB_D <= 8;
						elsif D_in_abs(7) = '1' then
							D_out_temp := D_in_abs(7 downto 0) & "00000000";
							MSB_D <= 7;
						elsif D_in_abs(6) = '1' then
							D_out_temp := D_in_abs(6 downto 0) & "000000000";
							MSB_D <= 6;
						elsif D_in_abs(5) = '1' then
							D_out_temp := D_in_abs(5 downto 0) & "0000000000";
							MSB_D <= 5;
						elsif D_in_abs(4) = '1' then
							D_out_temp := D_in_abs(4 downto 0) & "00000000000";
							MSB_D <= 4;
						elsif D_in_abs(3) = '1' then
							D_out_temp := D_in_abs(3 downto 0) & "000000000000";
							MSB_D <= 3;
						elsif D_in_abs(2) = '1' then
							D_out_temp := D_in_abs(2 downto 0) & "0000000000000";
							MSB_D <= 2;
						elsif D_in_abs(1) = '1' then
							D_out_temp := D_in_abs(1 downto 0) & "00000000000000";
							MSB_D <= 1;
						else
							D_out_temp := "1000000000000000";
							MSB_D <= 0;
						end if;
					end if;
				end if;
				D_out <= D_out_temp;
			end process;			

  bit_shift <= std_logic_vector(to_unsigned(MSB_D - MSB_N, 4));   ---STEP3

  
   
		
end fpga;
	
  
  
  
  