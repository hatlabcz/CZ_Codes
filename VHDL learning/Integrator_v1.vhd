

--------This integrator adds a delay of 1 cycle.

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.std_logic_unsigned.all;
use ieee.numeric_std.all;

entity Integrator_v1 is	
	Generic (
		input_width : integer := 16;
		output_width : integer := 32;
		input_signed : boolean := TRUE;
		input_latch	: boolean := FALSE;
		points : integer := 10
	);
	
	Port (
		Din_sdi_dataStreamFCx5_S_data_0 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_1 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_2 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_3 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_data_4 : in std_logic_vector(input_width-1 downto 0);
		Din_sdi_dataStreamFCx5_S_valid : in std_logic;
		
		
		Dout : out std_logic_vector(output_width-1 downto 0);
		--count_out : out integer;
		
		clk : in std_logic;
		rst : in std_logic;
		clr : in std_logic
	);
	
end Integrator_v1;

architecture Behavioral of Integrator_v1 is

signal Din_0_int : std_logic_vector(input_width-1 downto 0);
signal Din_1_int : std_logic_vector(input_width-1 downto 0);
signal Din_2_int : std_logic_vector(input_width-1 downto 0);
signal Din_3_int : std_logic_vector(input_width-1 downto 0);
signal Din_4_int : std_logic_vector(input_width-1 downto 0);
signal Din_valid_int : std_logic;

signal Dout_int :	std_logic_vector(31 downto 0):=(others=>'0');
signal count    :  integer := 0; 


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
		  	    variable Dout_int :	std_logic_vector(31 downto 0):=(others=>'0');
			    begin	
			   	    if(rst = '1' or clr = '1') then
			    	    --Dout_final <= (others => '0');
					    Dout_int := (others => '0');
						Dout <= (others => '0');
						count <= 0;		
					else
						if(clk'event and clk = '1') then
							if(Din_valid_int = '1') then
								if count = points then
									count <= 1;
									Dout <= Dout_int(31 downto 32-output_width);
									Dout_int := ((31 downto input_width => Din_0_int(input_width-1))&Din_0_int) + 
												((31 downto input_width => Din_1_int(input_width-1))&Din_1_int) + 
												((31 downto input_width => Din_2_int(input_width-1))&Din_2_int) + 
												((31 downto input_width => Din_3_int(input_width-1))&Din_3_int) + 
												((31 downto input_width => Din_4_int(input_width-1))&Din_4_int);
									
								else 
									count <= count+1;
									Dout_int := Dout_int+ 
												((31 downto input_width => Din_0_int(input_width-1))&Din_0_int) + 
												((31 downto input_width => Din_1_int(input_width-1))&Din_1_int) + 
												((31 downto input_width => Din_2_int(input_width-1))&Din_2_int) + 
												((31 downto input_width => Din_3_int(input_width-1))&Din_3_int) + 
												((31 downto input_width => Din_4_int(input_width-1))&Din_4_int);
								    
								end if;
							end if;
						end if;
					end if;
				end process;
				
			end generate signed_in;
			
no_signed_in:	if(input_signed = FALSE) generate
	
					process(clk)
					variable Dout_int :	std_logic_vector(31 downto 0):=(others=>'0');
					begin	
						if(rst = '1' or clr = '1') then
							--Dout_final <= (others => '0');
							Dout_int := (others => '0');
							Dout <= (others => '0');
							count <= 0;
						else
							if(clk'event and clk = '1') then
								if(Din_valid_int = '1') then
									if count = points then
										count <= 1;
										Dout <= Dout_int(31 downto 32-output_width);
										Dout_int := ((31 downto input_width => '0')&Din_0_int) +
													((31 downto input_width => '0')&Din_1_int) + 
													((31 downto input_width => '0')&Din_2_int) + 
													((31 downto input_width => '0')&Din_3_int) +
													((31 downto input_width => '0')&Din_4_int);
									else
										count <= count+1;
										Dout_int := Dout_int + 
													((31 downto input_width => '0')&Din_0_int) +
													((31 downto input_width => '0')&Din_1_int) + 
													((31 downto input_width => '0')&Din_2_int) + 
													((31 downto input_width => '0')&Din_3_int) +
													((31 downto input_width => '0')&Din_4_int);
									    
									end if;	
								end if;
							end if;
						end if;
					end process;
					
				end generate no_signed_in;
				
--Dout <= Dout_final;	
--count_out <= count;
end Behavioral;
