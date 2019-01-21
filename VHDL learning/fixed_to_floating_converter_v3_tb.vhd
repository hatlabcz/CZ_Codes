library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;

entity fix_to_flo_tb is
end fix_to_flo_tb;

architecture behave of fix_to_flo_tb is

  constant r_input_width : integer:=16;
  constant c_clk_period  : time:=10 ns;
  
  signal r_input     : std_logic_vector(r_input_width-1 downto 0);
  signal w_output    : std_logic_vector(r_input_width-1 downto 0);
  signal r_rst       : std_logic:='0';
  signal r_clk       : std_logic:='0';
   
  component fix_to_flo is
    Generic (
		input_width : integer := 16;
		exp_bits_num : integer := 6 -- the whole file need to be re-writed if this value is changed
	);
    Port (
		input  : in std_logic_vector(input_width-1 downto 0);
		output : out std_logic_vector(input_width-1 downto 0); --assume that input_width=output_width
		rst : in std_logic;
		clk : in std_logic
	);
end component fix_to_flo;

begin
  UUT : fix_to_flo
    port map (
      rst     => r_rst,
      input   => r_input,
      output  => w_output,
	  clk     => r_clk
      );
 
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
	end process p_clk_gen;
	
	
  process
  begin
  
  r_input <= "1000000000000000";
  wait for 10 ns;
  r_input <= "1111111111111111";
  wait for 10 ns;
  r_input <= "0111111111111111";
  wait for 10 ns;
  r_input <= "0001111111111111";
  wait for 10 ns;
  r_input <= "0000000000001111";
  wait for 10 ns;
  
  
  end process;
 
end behave;
  