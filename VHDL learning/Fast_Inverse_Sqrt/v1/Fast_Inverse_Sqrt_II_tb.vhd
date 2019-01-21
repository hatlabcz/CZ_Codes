library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;

entity Inv_Sqrt_II_tb is
end Inv_Sqrt_II_tb;

architecture behave of Inv_Sqrt_II_tb is

  constant c_clk_period  : time:=10 ns;
  signal r_input     : std_logic_vector(15 downto 0);
  signal r_D_input    : std_logic_vector(15 downto 0);
  signal w_final_out    : std_logic_vector(15 downto 0):= (others =>'0');
  
  
  signal r_rst       : std_logic:='0';
  signal r_clk       : std_logic:='0';
   


component Inv_Sqrt_II is
  port(
	I_in   : in std_logic_vector(15 downto 0);
	D_in   : in std_logic_vector(15 downto 0);
	ISqrt_out  : out std_logic_vector(15 downto 0) := (others =>'0');
	
	rst : in std_logic;
	clk : in std_logic
  );
end component Inv_Sqrt_II;

begin

  UUT4 : Inv_Sqrt_II
    port map (
      I_in => r_input,
	  D_in => r_D_input,
	  ISqrt_out => w_final_out,
	
	  rst     => r_rst,
	  clk     => r_clk
      );  	  
 
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
	end process p_clk_gen;
	
	
  process
  begin
  r_D_input<= "0000010111110101";
  r_input <= "0000011010111111";
  wait for 10 ns;
  r_D_input<= "0111111111111111";
  r_input <= "0000000101101110";
  wait for 10 ns;

  
  end process;
 
end behave;
  