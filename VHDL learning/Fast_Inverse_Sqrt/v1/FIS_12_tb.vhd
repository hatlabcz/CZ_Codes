library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;

entity fis12_tb is
end fis12_tb;

architecture behave of fis12_tb is

  constant c_clk_period  : time:=10 ns;
  signal r_input     : std_logic_vector(31 downto 0);
  signal w_output_flt    : std_logic_vector(31 downto 0);
  signal w_sign_out  : std_logic :='0';
  signal w_exp_out   : std_logic_vector(7 downto 0)  :=(others =>'0');
  signal w_mants_out : std_logic_vector(22 downto 0) :=(others =>'0');
  signal w_I_flt     : std_logic_vector(31 downto 0) :=(others =>'0');
 
  signal w_output    : std_logic_vector(15 downto 0);
  signal w_output2    : std_logic_vector(15 downto 0);
  
  
  signal r_rst       : std_logic:='0';
  signal r_clk       : std_logic:='0';
   
component fix_to_flo_32 is
    Port (
		D_in   : in std_logic_vector(31 downto 0);        
		D_out_flt  : out std_logic_vector(31 downto 0):= (others =>'0');
		D_out      : out std_logic_vector(15 downto 0):= (others =>'0');
		rst : in std_logic;
		clk : in std_logic;
		
		sign_out : out std_logic :='0';
		exp_out  : out std_logic_vector(7 downto 0)  :=(others =>'0');
		mants_out: out std_logic_vector(22 downto 0) :=(others =>'0')
	);
end component fix_to_flo_32;

component Inv_Sqrt_I is
  port(
    D_in_flt   : in std_logic_vector(31 downto 0);
	I_flt  : out std_logic_vector(31 downto 0) := (others =>'0');
	
	D_in  : in std_logic_vector(15 downto 0) := (others =>'0');
	D_out : out std_logic_vector(15 downto 0):= (others =>'0');
	
	rst : in std_logic;
	clk : in std_logic
  );
end component Inv_Sqrt_I;

begin
  UUT1 : fix_to_flo_32
    port map (
      rst     => r_rst,
      D_in    => r_input,
      D_out_flt   => w_output_flt,
	  D_out   => w_output,
	  sign_out => w_sign_out,
	  exp_out  => w_exp_out,
	  mants_out => w_mants_out,
	  clk     => r_clk
      );
  UUT2 : Inv_Sqrt_I
    port map (
      rst     => r_rst,
      D_in_flt    => w_output_flt,
	  D_in   => w_output,
	  D_out   => w_output2,
	  I_flt      => w_I_flt,
	  clk     => r_clk
      );  
	 
 
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
	end process p_clk_gen;
	
	
  process
  begin
  
  r_input <= "00000101111101011110000100000000";
  wait for 10 ns;
  r_input <= "01111111111111111111111111111111";
  wait for 10 ns;
  r_input <= "00000000000000000000000000000001";
  wait for 10 ns;
  r_input <= "00011111111111110001111111111111";
  wait for 10 ns;
  r_input <= "00000000000011110000000000001111";
  wait for 10 ns;
  r_rst <='1';
  wait for 10 ns;
  r_rst <= '0';
  r_input <= "10000000000000000000000000000000";
  wait for 10 ns;
  r_input <= "11111111111111111111111111111111";
  wait for 10 ns;
  r_input <= "01111111111111110111111111111111";
  wait for 10 ns;
  r_input <= "00011111111111110001111111111111";
  wait for 10 ns;
  r_input <= "00000000000011110000000000001111";
  
  end process;
 
end behave;
  