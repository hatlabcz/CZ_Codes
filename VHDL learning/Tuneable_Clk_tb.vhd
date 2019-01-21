library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all;

entity tuneable_clk_tb is
end tuneable_clk_tb;


architecture behaviral of tuneable_clk_tb is

  constant c_clk_period  : time:=10 ns; 
  
  signal r_clk     : std_logic :='1';
  signal w_clk_out : std_logic;

  component tuneable_clk is
    generic(
      frqeuency : integer := 50  --in MHz
    );
  
    port(
      clk_100 : in std_logic;
      clk_out : out std_logic
    );
  
end component tuneable_clk;
  
begin

  UUT : tuneable_clk
    port map (
	  clk_100  => r_clk,
	  clk_out  => w_clk_out
      );
 
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
  end process p_clk_gen;
	
	
  process
  begin
    wait for 1000 ns;
    
  end process;
 
end behaviral; 