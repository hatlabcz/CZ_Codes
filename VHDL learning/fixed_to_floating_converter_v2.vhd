library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;

entity fix_to_flo is
  Generic (
		input_width : integer := 16;
		exp_bits_num : integer := 6 -- the whole file need to be re-writed if this value is changed
	);
  Port (
		input  : in std_logic_vector(input_width-1 downto 0);
		output : out std_logic_vector(input_width-1 downto 0); --assume that input_width=output_width
		rst : in std_logic
	);
end fix_to_flo;

architecture behavioral of fix_to_flo is

  signal sign       : std_logic := '0';
  signal complement : std_logic_vector(input_width-1 downto 0) := (others => '0');
  signal exponent   : std_logic_vector(exp_bits_num-1 downto 0) := (others => '0');
  signal mantissa   : std_logic_vector(input_width-exp_bits_num-2 downto 0) := (others => '0');
 
begin

  sign <= '1' when(input(input_width-1)='1') else '0';
  complement <= (not(input)+1) when(input(input_width-1)='1') else input;
  
  exponent <= "001111" when complement(input_width-1)='1' else
			  "001110" when complement(input_width-1 downto input_width-2)= "01" else
			  "001101" when complement(input_width-1 downto input_width-3)= "001" else
			  "001100" when complement(input_width-1 downto input_width-4)= "0001" else
			  "001011" when complement(input_width-1 downto input_width-5)= "00001" else
			  "001010" when complement(input_width-1 downto input_width-6)= "000001" else
			  "001001" when complement(input_width-1 downto input_width-7)= "0000001" else
			  "001000" when complement(input_width-1 downto input_width-8)= "00000001" else
			  "000111" when complement(input_width-1 downto input_width-9)= "000000001" else
			  "000110" when complement(input_width-1 downto input_width-10)= "0000000001" else
			  "000101" when complement(input_width-1 downto input_width-11)= "00000000001" else
			  "000100" when complement(input_width-1 downto input_width-12)= "000000000001" else
			  "000011" when complement(input_width-1 downto input_width-13)= "0000000000001" else
			  "000010" when complement(input_width-1 downto input_width-14)= "00000000000001" else
			  "000001" when complement(input_width-1 downto input_width-15)= "000000000000001" else
			  "000000";
			  
  mantissa <= complement(input_width-2 downto exp_bits_num) when complement(input_width-1)='1' else
			  complement(input_width-3 downto exp_bits_num-1) when complement(input_width-1 downto input_width-2)= "01" else
			  complement(input_width-4 downto exp_bits_num-2) when complement(input_width-1 downto input_width-3)= "001" else
			  complement(input_width-5 downto exp_bits_num-3) when complement(input_width-1 downto input_width-4)= "0001" else
			  complement(input_width-6 downto exp_bits_num-4) when complement(input_width-1 downto input_width-5)= "00001" else
			  complement(input_width-7 downto exp_bits_num-5) when complement(input_width-1 downto input_width-6)= "000001" else
			  complement(input_width-8 downto exp_bits_num-6) when complement(input_width-1 downto input_width-7)= "0000001" else
			  "0" & complement(input_width-9 downto 0) when complement(input_width-1 downto input_width-8)= "00000001" else
			  "00" & complement(input_width-10 downto 0) when complement(input_width-1 downto input_width-9)= "000000001" else
			  "000" & complement(input_width-11 downto 0) when complement(input_width-1 downto input_width-10)= "0000000001" else
			  "0000" & complement(input_width-12 downto 0) when complement(input_width-1 downto input_width-11)= "00000000001" else
			  "00000" & complement(input_width-13 downto 0) when complement(input_width-1 downto input_width-12)= "000000000001" else
			  "000000" & complement(input_width-14 downto 0) when complement(input_width-1 downto input_width-13)= "0000000000001" else
			  "0000000" & complement(input_width-15 downto 0) when complement(input_width-1 downto input_width-14)= "00000000000001" else
			  "00000000" & complement(input_width-16 downto 0) when complement(input_width-1 downto input_width-15)= "000000000000001" else
			  "000000000";
	
	output <= (others=>'0') when rst='1' else sign&exponent&mantissa;

end behavioral;
 