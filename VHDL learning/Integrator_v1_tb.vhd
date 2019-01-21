library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.numeric_std.all;
use std.textio.all;
use IEEE.std_logic_textio.all;


entity Integrator_v1_tb is
end Integrator_v1_tb;

architecture behave of Integrator_v1_tb is
 
  constant c_clk_period   : time :=10 ns;
  constant r_input_width  : integer :=16;
  constant r_output_width : integer :=32;
  
  signal r_rst     : std_logic :='0';
  signal r_clr     : std_logic :='0';
  signal r_clk     : std_logic :='0';

  signal r_Din_sdi_dataStreamFCx5_S_data_0 : std_logic_vector(r_input_width-1 downto 0):= (others => '0');
  signal r_Din_sdi_dataStreamFCx5_S_data_1 : std_logic_vector(r_input_width-1 downto 0):= (others => '0');
  signal r_Din_sdi_dataStreamFCx5_S_data_2 : std_logic_vector(r_input_width-1 downto 0):= (others => '0');
  signal r_Din_sdi_dataStreamFCx5_S_data_3 : std_logic_vector(r_input_width-1 downto 0):= (others => '0');
  signal r_Din_sdi_dataStreamFCx5_S_data_4 : std_logic_vector(r_input_width-1 downto 0):= (others => '0');
  signal r_Din_sdi_dataStreamFCx5_S_valid  : std_logic := '1';
  signal w_Dout                            : std_logic_vector(r_output_width-1 downto 0):= (others => '0');
  
  --signal r_count_out : integer;
  



  
  component Integrator_v1 is	
	Generic (
		input_width : integer := 16;
		output_width : integer := 32;
		input_signed : boolean := FALSE;
		input_latch	: boolean := FALSE;
		points : integer:=2
	);
	
	Port (
		Din_sdi_dataStreamFCx5_S_data_0 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_1 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_2 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_3 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_4 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_valid  : in std_logic;
		
		
		Dout : out std_logic_vector(output_width-1 downto 0);
		--count_out : out integer;
		
		clk : in std_logic;
		rst : in std_logic;
		clr : in std_logic
	);
	
  end component Integrator_v1;
  
begin

  UUT : Integrator_v1
    port map (
	  Din_sdi_dataStreamFCx5_S_data_0  => r_Din_sdi_dataStreamFCx5_S_data_0,
	  Din_sdi_dataStreamFCx5_S_data_1  => r_Din_sdi_dataStreamFCx5_S_data_1,
	  Din_sdi_dataStreamFCx5_S_data_2  => r_Din_sdi_dataStreamFCx5_S_data_2,
	  Din_sdi_dataStreamFCx5_S_data_3  => r_Din_sdi_dataStreamFCx5_S_data_3,
	  Din_sdi_dataStreamFCx5_S_data_4  => r_Din_sdi_dataStreamFCx5_S_data_4,
	  Din_sdi_dataStreamFCx5_S_valid   => r_Din_sdi_dataStreamFCx5_S_valid, 
	  
	  Dout => w_Dout,
	  clk => r_clk,
	  rst => r_rst,
	  clr => r_clr
	  
	--  count_out => r_count_out
	  
      );
 
 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
  end process p_clk_gen;
	
	
  process
  
  --FILE file_out : TEXT IS OUT "dataout.txt";
  --VARIABLE line_out : LINE;
  --VARIABLE output_tmp : INTEGER;
  
  begin
    r_rst <= '1';
	wait for 30 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    
	--output_tmp := to_integer(signed(w_Dout));
	--WRITE (line_out, output_tmp);
   --WRITELINE(file_out, line_out);	
    
	wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";   
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000011";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";  
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000001000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";    
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000001000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;                             --10
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;                              --20
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	
    
  end process;
 
end behave;   

