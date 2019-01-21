library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all;

entity counter_tb is
end counter_tb;


architecture behaviral of counter_tb is

  constant c_clk_period  : time:=10 ns; 
  
  signal r_clk    : std_logic :='0';
  signal r_rst    : std_logic :='0';
  signal w_count : std_logic_vector(15 downto 0);
  
  

  component counter is
    generic(
      start : integer := 1; -- can be negative, start < stop 
	  stop  : integer := 5  --maxmium: 32767 ,minimum:-32768
    );
  
    port(
      clk : in std_logic;
	  rst : in std_logic;
	  count : out std_logic_vector(15 downto 0)
    );
  end component counter;
  
begin

  UUT : counter
    port map (
      rst    => r_rst,
	  clk    => r_clk,
	  count  => w_count
      );
 
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
  end process p_clk_gen;
	
	
  process
  begin
    wait for 100 ns;
    
  end process;
 
end behaviral; 