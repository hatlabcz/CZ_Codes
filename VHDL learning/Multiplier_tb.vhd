library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
Library UNISIM;
use UNISIM.vcomponents.all;


entity Multiplier_tb is	

end Multiplier_tb;

architecture Behavioral of Multiplier_tb is
  
  constant r_input_width : integer:=16;
  constant r_output_width : integer:=16;
  constant c_clk_period  : time:=10 ns;
 
  
  signal r_A       : std_logic_vector(r_input_width-1 downto 0);
  signal r_B       : std_logic_vector(r_input_width-1 downto 0);
  signal W_Dout    : std_logic_vector(r_output_width-1 downto 0);
  signal r_rst     : std_logic:='0';
  signal r_clk     : std_logic:='0';
  
  component Multiplier is
  	Generic (
		bus_ina_width : integer := 16;
		ina_signed : boolean := TRUE; 
		bus_inb_width : integer := 16;
		inb_signed : boolean := TRUE;
		bus_output_width : integer := 16;
		latch_input : boolean := FALSE
	);
	
	Port (
		A : in std_logic_vector(bus_ina_width-1 downto 0); 
		B : in std_logic_vector(bus_inb_width-1 downto 0);
		Dout : out std_logic_vector(bus_output_width-1 downto 0);
		clk : in std_logic;
		rst : in std_logic
	);
  end component Multiplier;
  
  begin
  UUT : Multiplier
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
  r_rst <= '0';
  r_A <= "1000000010000000";
  r_B <= "0110010010000000";
  wait for 10 ns;
  r_A <= "0101111010000000";
  r_B <= "0110010010000000";
  wait for 10 ns;
  r_A <= "1001110010000000";
  r_B <= "1010010010000000";
  wait for 10 ns;
  end process;
  
End Behavioral;
  