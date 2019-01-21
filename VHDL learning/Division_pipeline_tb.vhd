----------------------------------------------------------------------------------
-- Company: Hatlab@Pitt
-- Author : Chao Zhou
-- Reference : Meyer-Baese, Uwe. Digital signal processing with field programmable gate arrays. Springer Science & Business Media, 2007. P101
-- Create Date: 07/25/2018

----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.numeric_std.all;

entity Division_pl_tb is
end Division_pl_tb;

architecture behave of Division_pl_tb is
  
  constant c_clk_period  : time:=10 ns;
  constant wid :integer :=16;
  
  signal r_N_in  : std_logic_vector(wid-1 downto 0) := (wid-1 => '1',wid-2 => '1',others =>'0');
  signal r_D_in  : std_logic_vector(wid-1 downto 0) := (wid-1 => '1',wid-2 => '1',wid-3 =>'1',others =>'0');
  signal r_sign  : std_logic := '0';
  signal r_bit_shift : std_logic_vector (3 downto 0) := "0000";
  signal w_Q_out : std_logic_vector(wid-1 downto 0) :=( others => '0');
  signal r_clk   : std_logic := '0';
  signal r_rst   : std_logic := '0';
  
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
  UUT : Division_pl
    port map (
      rst     => r_rst,
	  clk     => r_clk,
	  N_in    => r_N_in,
	  D_in    => r_D_in,
	  sign    => r_sign,
	  bit_shift => r_bit_shift,
	  Q_out   => w_Q_out
      );
 
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
  end process p_clk_gen;
	
	
  process
  begin
    r_sign <='0';
	r_bit_shift <="0000";
	r_N_in <= "1100000000000000";
	r_D_in <= "1110000000000000";
	wait for 10 ns;
	r_sign <='1';
	r_bit_shift <="0000";
	r_N_in <= "1010000000010000";
	r_D_in <= "1111111101011000";
	wait for 10 ns;
	r_sign <='1';
	r_bit_shift <="0000";
	r_N_in <= "1100000000000000";
	r_D_in <= "1110000000000000";
	wait for 10 ns;
	r_sign <='0';
	r_bit_shift <="0000";
	r_N_in <= "1100000000000000";
	r_D_in <= "1110000000000000";
	wait for 10 ns;
	
  end process;
  
End behave;
  
	
	
