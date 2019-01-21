----------------------------------------------------------------------------------
-- Company: Hatlab@Pitt
-- Author : Chao Zhou
-- Reference : 
-- Create Date: 07/25/2018
-- Description : Change the incoming signal into the form that is suitable for the Divison block(1.15 bit_shift, i.e. 1 integer 15 fractional bits). 
--               1)Use XOR gate to find the sign of result then convert the input to abs value
--               2)Find MSB and shift it to the first bit
--               3)Record the difference of number of bits shiffted for final reduction.
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.numeric_std.all;

entity Div_FormConv_tb is	
end Div_FormConv_tb;

architecture Behavioral of Div_FormConv_tb is

  constant c_clk_period  : time:=10 ns;
 
  
  signal r_N_in       : std_logic_vector(15 downto 0);
  signal r_D_in       : std_logic_vector(15 downto 0);
  signal w_sign       : std_logic :='0';
  signal w_bit_shift  : std_logic_vector(3 downto 0);
  signal w_N_out      : std_logic_vector(15 downto 0);
  signal w_D_out      : std_logic_vector(15 downto 0);
  
  signal r_rst     : std_logic:='0';
  signal r_clk     : std_logic:='0';
  
  component Div_FormConv is
    port(
	N_in  : in std_logic_vector(15 downto 0);
	D_in  : in std_logic_vector(15 downto 0);   --Assume 16 bits income
	
	sign      : out std_logic := '0';
	bit_shift : out std_logic_vector (3 downto 0) := "0000";  --Also assume Denorminator is always graeator than Norminator
	
	N_out     : out std_logic_vector(15 downto 0):= (others => '1');
	D_out     : out std_logic_vector(15 downto 0):= (others => '1');
	
	clk : in std_logic;
	rst : in std_logic
    );
	
  end component Div_FormConv;
  
begin
  UUT1 : Div_FormConv
    port map (
      N_in     => r_N_in,
      D_in     => r_D_in,
	  sign       => w_sign,
	  bit_shift  => w_bit_shift,
	  N_out    => w_N_out,
	  D_out    => w_D_out,
      clk      => r_clk,
	  rst      => r_rst
      );
 
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
  end process p_clk_gen;
	
	
  process
  begin
	r_N_in <= "0111000100010000";
	r_D_in <= "0111110000000010";
	wait for 10 ns;
	r_N_in <= "0000000000000001";
	r_D_in <= "1000000000000000";
	wait for 10 ns;
	r_N_in <= "1111111111100000";
	r_D_in <= "0111110000000000";
	wait for 10 ns;
	r_rst <= '1';
	wait for 10 ns;
	r_rst <= '0';
	r_N_in <= "0111000000000000";
	r_D_in <= "0111110000000000";
	wait for 10 ns;
	r_N_in <= "1111000000000000";
	r_D_in <= "0111110000000000";
	wait for 10 ns;
	r_N_in <= "1111111111100000";
	r_D_in <= "0111110000000000";
  
  end process;
  
End Behavioral;