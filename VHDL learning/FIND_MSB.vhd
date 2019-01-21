----------------------------------------------------------------------------------
-- Company: Hatlab@Pitt
-- Author : Chao Zhou
-- 
-- Create Date:    07/18/2018

----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.numeric_std.all;

entity FIND_MSB is
  port(
    Din : in std_logic_vector(16 downto 0);
	Dout: out std_logic_vector(4 downto 0):="01111";  -- unsigned
    
	clk : in std_logic;
	rst : in std_logic
  
  );
end FIND_MSB;

architecture behave of FIND_MSB is
  
  Signal MSB_temp : std_logic_vector(4 downto 0)  :="01111";
  signal bar      : std_logic_vector(16 downto 0)  :=(others => '0');
  signal Din_abs  : std_logic_vector(16 downto 0) :=(others => '0');
  
begin

  Din_abs <= not Din  when Din(16)='1' else Din;
  
  process(clk, rst)
  begin
    if(rst = '1') then
			MSB_temp <= "01111";
			
	else
		if(clk'event and clk = '1') then
			if (to_integer(unsigned(Din_abs))-to_integer(unsigned(bar))>0) then
				bar <= Din_abs;
				if Din_abs(16 downto 15) = "01" then
					MSB_temp <= "11111";
				elsif Din_abs(16 downto 14) = "001" then
					MSB_temp <= "11110";
				elsif Din_abs(16 downto 13) = "0001" then
					MSB_temp <= "11101";
				elsif Din_abs(16 downto 12) = "00001" then
					MSB_temp <= "11100";
				elsif Din_abs(16 downto 11) = "000001" then
					MSB_temp <= "11011";
				elsif Din_abs(16 downto 10) = "0000001" then
					MSB_temp <= "11010";
				elsif Din_abs(16 downto  9) = "00000001" then
					MSB_temp <= "11001";
				elsif Din_abs(16 downto  8) = "000000001" then
					MSB_temp <= "11000";
				elsif Din_abs(16 downto  7) = "0000000001" then
					MSB_temp <= "10111";
				elsif Din_abs(16 downto  6) = "00000000001" then
					MSB_temp <= "10110";
				elsif Din_abs(16 downto  5) = "000000000001" then
					MSB_temp <= "10101";
				elsif Din_abs(16 downto  4) = "0000000000001" then
					MSB_temp <= "10100";
				elsif Din_abs(16 downto  3) = "00000000000001" then
					MSB_temp <= "10011";
				elsif Din_abs(16 downto  2) = "000000000000001" then
					MSB_temp <= "10010";
				elsif Din_abs(16 downto  1) = "0000000000000001" then
					MSB_temp <= "10001";
				elsif Din_abs(16 downto  0) = "00000000000000001" then
					MSB_temp <= "10000";
				else
					MSB_temp <= "01111";
				end if;
		    end if;
		end if;
	end if;
  end process;
  Dout <= MSB_temp ;
end behave;
