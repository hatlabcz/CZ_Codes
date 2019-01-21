----------------------------------------------------------------------------------
-- Company: Signadyne
-- Engineer: Marcel Gozalbo
-- 
-- Create Date:    11:02:21 07/26/2012 
-- Design Name: 
-- Module Name:    Integrator_datax5 - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.numeric_std.all;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity Integrator_stream_datax5_fbtr is	
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
		Din_sdi_dataStreamFCx5_S_valid : in std_logic;
		
		
		Dout       : out std_logic_vector(output_width-1 downto 0);
		Dout_31_15 : out std_logic_vector(16 downto 0) := (others =>'0');
		
		clk : in std_logic;
		rst : in std_logic;
		clr : in std_logic;
		
		truncate_start: in std_logic_vector(4 downto 0)
	);
	
end Integrator_stream_datax5_fbtr;

architecture Behavioral of Integrator_stream_datax5_fbtr is

signal Din_0_int : std_logic_vector(input_width-1 downto 0);
signal Din_1_int : std_logic_vector(input_width-1 downto 0);
signal Din_2_int : std_logic_vector(input_width-1 downto 0);
signal Din_3_int : std_logic_vector(input_width-1 downto 0);
signal Din_4_int : std_logic_vector(input_width-1 downto 0);
signal Din_valid_int : std_logic;

signal Dout_int :	std_logic_vector(31 downto 0);

signal truncate_start_int : integer := 31;

begin
	
latch_in:	if(input_latch = TRUE) generate

				process(clk)
				begin	
					if(clk'event and clk = '1') then
						Din_valid_int <= Din_sdi_dataStreamFCx5_S_valid;
						Din_0_int <= Din_sdi_dataStreamFCx5_S_data_0;
						Din_1_int <= Din_sdi_dataStreamFCx5_S_data_1;
						Din_2_int <= Din_sdi_dataStreamFCx5_S_data_2;
						Din_3_int <= Din_sdi_dataStreamFCx5_S_data_3;
						Din_4_int <= Din_sdi_dataStreamFCx5_S_data_4;
					end if;
				end process;
				
			end generate latch_in;
			
no_latch_in:	if(input_latch = FALSE) generate
				
					Din_valid_int <= Din_sdi_dataStreamFCx5_S_valid;
					Din_0_int <= Din_sdi_dataStreamFCx5_S_data_0;
					Din_1_int <= Din_sdi_dataStreamFCx5_S_data_1;
					Din_2_int <= Din_sdi_dataStreamFCx5_S_data_2;
					Din_3_int <= Din_sdi_dataStreamFCx5_S_data_3;
					Din_4_int <= Din_sdi_dataStreamFCx5_S_data_4;
					
				end generate no_latch_in;
	

signed_in:	if(input_signed = TRUE) generate

				process(clk)
				begin	
					if(clk'event and clk = '1') then
						if(rst = '1' or clr = '1') then
							Dout_int <= (others => '0');
						else
							if(Din_valid_int = '1') then
								Dout_int <= ((31 downto input_width => Din_0_int(input_width-1))&Din_0_int) + 
											((31 downto input_width => Din_1_int(input_width-1))&Din_1_int) + 
											((31 downto input_width => Din_2_int(input_width-1))&Din_2_int) + 
											((31 downto input_width => Din_3_int(input_width-1))&Din_3_int) + 
											((31 downto input_width => Din_4_int(input_width-1))&Din_4_int);
							end if;
						end if;
					end if;
				end process;
				
			end generate signed_in;
			
no_signed_in:	if(input_signed = FALSE) generate
	
					process(clk)
					begin	
						if(clk'event and clk = '1') then
							if(rst = '1' or clr = '1') then
								Dout_int <= (others => '0');
							else
								if(Din_valid_int = '1') then
									Dout_int <= ((31 downto input_width => '0')&Din_0_int) +
												((31 downto input_width => '0')&Din_1_int) + 
												((31 downto input_width => '0')&Din_2_int) + 
												((31 downto input_width => '0')&Din_3_int) +
												((31 downto input_width => '0')&Din_4_int);
								end if;
							end if;
						end if;
					end process;
					
				end generate no_signed_in;

truncate_start_int <= to_integer(unsigned(truncate_start));			
Dout <= Dout_int(truncate_start_int downto truncate_start_int-15);
Dout_31_15 <= Dout_int(31 downto 15);

end Behavioral;
