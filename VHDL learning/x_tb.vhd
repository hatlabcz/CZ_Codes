library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity x_tb is	

end x_tb;

architecture Behavioral_x of x_tb is
  
  constant r_input_width : integer:=16;
  constant r_output_width : integer:=16;
  constant c_clk_period  : time:=10 ns;
 
  
  signal r_A       : std_logic_vector(r_input_width-1 downto 0);
  signal r_B       : std_logic_vector(r_input_width-1 downto 0);
  signal W_Dout    : std_logic_vector(r_output_width-1 downto 0);
  
  signal r_rst     : std_logic:='0';
  signal r_clk     : std_logic:='0';
  
  component x is
  	
	
  end component x;
  
begin
  UUT1 : x
    port map (
      rst     => r_rst,
      A       => r_A,
	  B       => r_B,
      Dout    => w_Dout,
	  clk     => r_clk
      );
 
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
  end process p_clk_gen;
	
	
  process
  begin
  
  
  end process;
  
End Behavioral;