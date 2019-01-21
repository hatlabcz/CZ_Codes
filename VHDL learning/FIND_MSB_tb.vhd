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

entity FIND_MSB_tb is	
end FIND_MSB_tb;

architecture Behavioral of FIND_MSB_tb is
  
  constant c_clk_period   : time :=10 ns;
  
  signal r_Din        : std_logic_vector(16 downto 0);
  signal w_Dout       : std_logic_vector(4 downto 0):="01111";
  signal r_rst     : std_logic:='0';
  signal r_clk     : std_logic:='0';
  
  component FIND_MSB is
    port(
    Din : in std_logic_vector(16 downto 0);
	Dout: out std_logic_vector(4 downto 0):="01111";
    
	clk : in std_logic;
	rst : in std_logic
  
    );
  end component FIND_MSB;
  
begin
  UUT1 : FIND_MSB
    port map (
	  clk     => r_clk,
      rst     => r_rst,
      Din     => r_Din,
      Dout    => w_Dout
      );
 
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
  end process p_clk_gen;
	
	
  process
  begin
    r_Din <= "11111111111101111";
	wait for 10 ns;
	r_Din <= "11111111111000001";
	wait for 10 ns;
	r_Din <= "00000001111111111";
	wait for 10 ns;
	r_Din <= "00000000000111111";
	wait for 10 ns;
	r_Din <= "00000000000000111";
	wait for 10 ns;

	
	
  
  
  end process;
  
End Behavioral;