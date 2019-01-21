library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.numeric_std.all;

entity Integrator_stream_datax5_fbtr_tb is	
end Integrator_stream_datax5_fbtr_tb;

architecture Behavioral of Integrator_stream_datax5_fbtr_tb is
  
  constant c_clk_period   : time :=10 ns;
  
  signal r_Din_FMSB        : std_logic_vector(16 downto 0);
  signal r_truncate_start       : std_logic_vector(4 downto 0):="01111";
  signal r_rst     : std_logic:='0';
  signal r_clk     : std_logic:='0';
  signal r_clr     : std_logic :='0';
  
  constant r_input_width  : integer :=16;
  constant r_output_width : integer :=16;


  signal r_Din_sdi_dataStreamFCx5_S_data_0 : std_logic_vector(r_input_width-1 downto 0):= (others => '0');
  signal r_Din_sdi_dataStreamFCx5_S_data_1 : std_logic_vector(r_input_width-1 downto 0):= (others => '0');
  signal r_Din_sdi_dataStreamFCx5_S_data_2 : std_logic_vector(r_input_width-1 downto 0):= (others => '0');
  signal r_Din_sdi_dataStreamFCx5_S_data_3 : std_logic_vector(r_input_width-1 downto 0):= (others => '0');
  signal r_Din_sdi_dataStreamFCx5_S_data_4 : std_logic_vector(r_input_width-1 downto 0):= (others => '0');
  signal r_Din_sdi_dataStreamFCx5_S_valid  : std_logic := '1';
  signal w_Dout                            : std_logic_vector(r_output_width-1 downto 0):= (others => '0');
  
  
  component FIND_MSB is
    port(
    Din : in std_logic_vector(16 downto 0);
	Dout: out std_logic_vector(4 downto 0):="01111";
    
	clk : in std_logic;
	rst : in std_logic
  
    );
  end component FIND_MSB;
  
  component Integrator_stream_datax5_fbtr is	
	Generic (
		input_width : integer := 16;
		output_width : integer := 16;
		input_signed : boolean := TRUE;
		input_latch	: boolean := FALSE
	);
	
	Port (
	
		Din_sdi_dataStreamFCx5_S_data_0 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_1 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_2 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_3 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_4 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_valid  : in std_logic;
		
		
		Dout       : out std_logic_vector(output_width-1 downto 0);
		Dout_31_15 : out std_logic_vector(16 downto 0) := (others =>'0');
		
		clk : in std_logic;
		rst : in std_logic;
		clr : in std_logic;
		
		truncate_start: in std_logic_vector(4 downto 0)
	);	
  end component Integrator_stream_datax5_fbtr;
  
begin

  UUT_integrator : Integrator_stream_datax5_fbtr
    port map (
	  Din_sdi_dataStreamFCx5_S_data_0  => r_Din_sdi_dataStreamFCx5_S_data_0,
	  Din_sdi_dataStreamFCx5_S_data_1  => r_Din_sdi_dataStreamFCx5_S_data_1,
	  Din_sdi_dataStreamFCx5_S_data_2  => r_Din_sdi_dataStreamFCx5_S_data_2,
	  Din_sdi_dataStreamFCx5_S_data_3  => r_Din_sdi_dataStreamFCx5_S_data_3,
	  Din_sdi_dataStreamFCx5_S_data_4  => r_Din_sdi_dataStreamFCx5_S_data_4,
	  Din_sdi_dataStreamFCx5_S_valid   => r_Din_sdi_dataStreamFCx5_S_valid, 
	  
	  Dout => w_Dout,
	  Dout_31_15 => r_Din_FMSB,
	  
	  clk => r_clk,
	  rst => r_rst,
	  clr => r_clr,

	  truncate_start=>r_truncate_start
      );
  UUT1 : FIND_MSB
    port map (
	  clk     => r_clk,
      rst     => r_rst,
      Din     => r_Din_FMSB,
      Dout    => r_truncate_start
      );


 
  p_clk_gen : process is
    begin 
	  wait for c_clk_period/2;
	  r_clk <= not(r_clk);
  end process p_clk_gen;
	
	
  process
  begin
    r_rst <= '1';
	wait for 30 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000010000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000001000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0001000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0001000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0000000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0000000100000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0000000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0010000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0000000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0100000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0100000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0100000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0100000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0100000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0100000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0100000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0100000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0100000010000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0100000000000000";
    wait for 10 ns;
	r_rst <= '0';
    r_Din_sdi_dataStreamFCx5_S_data_0 <="0001000000000010";
	r_Din_sdi_dataStreamFCx5_S_data_1 <="0010000000000001";
	r_Din_sdi_dataStreamFCx5_S_data_2 <="0100000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_3 <="0001000000000000";
	r_Din_sdi_dataStreamFCx5_S_data_4 <="0100000000000000";
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

	
	
  
  
  end process;
  
End Behavioral;