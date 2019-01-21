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
use std.textio.all;


entity Div_Comb_Norm_2_tb is	
end Div_Comb_Norm_2_tb;

architecture Behavioral of Div_Comb_Norm_2_tb is

  constant c_clk_period  : time:=10 ns;
 
  
  signal r_N_in       : std_logic_vector(15 downto 0);
  signal r_D_in       : std_logic_vector(15 downto 0);
  signal w_sign       : std_logic :='0';
  signal w_bit_shift  : std_logic_vector(3 downto 0);
  signal w_N_out      : std_logic_vector(15 downto 0);
  signal w_D_out      : std_logic_vector(15 downto 0);
  signal w_Q_out      : std_logic_vector(15 downto 0);
  
  signal r_rst     : std_logic:='0';
  signal r_clk     : std_logic:='0';
  
  component Div_FormConv_Norm is
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
	
  end component Div_FormConv_Norm;
  
  component Division_pl is
	  generic(
		WN : integer := 16;   --1 integer plus 15 fractional bits
		WD : integer := 16;
		max_shift : integer := 3;  --log2(max(WD,WN))-1  or Width(binary(max(WN,WD))-1
		TWO : integer := 65536;     --2**WN
		PO2WN : integer := 32768;  --2**(WN-1)
		PO2WN2 : integer := 131071  --2**(WN+1)-1
	  );



	  port(
		N_in  : in std_logic_vector(WN-1 downto 0);
		D_in  : in std_logic_vector(WD-1 downto 0);
		sign  : in std_logic;
		bit_shift : in std_logic_vector (max_shift downto 0);
		
		Q_out : out std_logic_vector(WD-1 downto 0):= (others => '0');
		clk : in std_logic;
		rst : in std_logic
	  );
  end component Division_pl; 
  
  
  
begin
  
  UUT1 : Div_FormConv_Norm
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
   
   UUT2 : Division_pl
    port map (
      rst     => r_rst,
	  clk     => r_clk,
	  N_in    => w_N_out,
	  D_in    => w_D_out,
	  sign    => w_sign,
	  bit_shift => w_bit_shift,
	  Q_out   => w_Q_out
      );
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
  end process p_clk_gen;
	
	
  
	
  process
  begin
    r_N_in <= "0101000000001000";
    r_D_in <= "0111111110101100";
	wait for 10 ns;

  end process;
  
End Behavioral;