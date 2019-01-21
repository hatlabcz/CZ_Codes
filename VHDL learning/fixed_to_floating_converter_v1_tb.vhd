library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;

entity fix_to_flo_tb is
end fix_to_flo_tb;

architecture behavioral of fix_to_flo_tb is

  constant c_clk_period  : time := 10 ns;
  constant r_input_width : integer:=16;
  
  signal r_input  : std_logic_vector(r_input_width-1 downto 0):=(others => '0');
  signal r_output : std_logic_vector(r_input_width-1 downto 0):=(others => '0');
  signal r_clk  : std_logic := '0';
  signal r_rst    : std_logic := '0';

  component fix_to_flo is
    Generic (
		input_width : integer := 16; -- the whole file need to be re-writed if this value is changed
		exp_bits_num : integer := 6 -- the whole file need to be re-writed if this value is changed
	);
    Port (
		input  : in std_logic_vector(input_width-1 downto 0);
		output : out std_logic_vector(input_width-1 downto 0); --assume that input_width=output_width
		clk : in std_logic;
		rst : in std_logic
	);
  end component fix_to_flo;

begin

  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
	end process p_clk_gen;
	
   uut : fix_to_flo
   port map(
     input => r_input,
	 output => r_output,
	 clk => r_clk,
	 rst => r_rst
   );
   
   process
   begin
	 r_input <= "1011111111111111";
	 wait for 10 ns;
	 r_input <= "1001111111111111";
	 wait for 10 ns;
	 r_input <= "0001111111111111";
	 wait for 10 ns;
   end process;

end behavioral;