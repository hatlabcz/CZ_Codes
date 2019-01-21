----------------------------------------------------------------------------------
-- Company: Hatlab@Pitt
-- Author : Chao Zhou
-- Reference :
-- Create Date: 07/27/2018
-- Description : flo_to_fix for the output of Fast_Inverse_Sqrt_Initial_Guesss. 
-->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>The result is expended by 2^24<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
--               Since the Initial_Guesss result is in reange  2^-16 to 1 , the result of this step should be 2^8 to 2^24,
--               However, since the large inverse_sqrt means small input from the very begenning(which can be neglected), we just assume 
--               that the results between 2^16 to 2^24 all equal to 2^16.
--               So the final output is 16 bit unsigned. 
------------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;
use ieee.numeric_std.all;


entity flo_to_fix_16 is
  Port (
		I_in_flt   : in std_logic_vector(31 downto 0);         --
		I_out  : out std_logic_vector(15 downto 0) :=(others =>'0');
		
		D_in  : in std_logic_vector(15 downto 0) := (others =>'0');
	    D_out : out std_logic_vector(15 downto 0):= (others =>'0');
	
		rst : in std_logic;
		clk : in std_logic				
	);
end flo_to_fix_16;

architecture fpga of flo_to_fix_16 is

begin

  process(rst,clk)
	variable exp  : std_logic_vector(7 downto 0)  :=(others =>'0');
	variable mants: std_logic_vector(22 downto 0) :=(others =>'0');
	variable MSB  : integer :=15 ;
  begin
	if rst='1' then
		MSB  := 15;
		exp  := (others =>'0');
		mants:= (others =>'0');
		I_out <= (others =>'0');
		D_out <= (others =>'0');
    else
        if(clk'event and clk = '1') then
			exp   := I_in_flt(30 downto 23);
			mants := I_in_flt(22 downto 0);
			MSB   := to_integer(unsigned(exp))-103;  --bias =127 ,expanded by 24, 127-24=103, 
			D_out <=D_in;
			if MSB >15 then
				I_out <= (others =>'1');
			elsif MSB=15 then
				I_out <= '1'& mants(22 downto 8);
			elsif MSB>0 then
				I_out(15 downto MSB+1)  <= (others => '0');
				I_out(MSB downto 0) <= '1'& mants(22 downto 23-MSB);           --    8=<MSB<24
			end if;
		end if;
	end if;
  end process;

end fpga;