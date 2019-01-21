----------------------------------------------------------------------------------
-- Company: Hatlab@Pitt
-- Author : Chao Zhou
-- Reference : "quake3-1.32b/code/game/q_math.c". Quake III Arena. id Software. Retrieved 2017-01-21.
-- Create Date: 07/27/2018
-- Description : Fast inverse square root, based on the reference.(Totally amazed, shocked and mindfucked)
----------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;
use ieee.numeric_std.all;

entity Inv_Sqrt is
  port(
    D_in_flt   : in std_logic_vector(31 downto 0);
	
	D_out_flt  : out std_logic_vector(31 downto 0) := (others =>'0');
	
	rst : in std_logic;
	clk : in std_logic
  );
end Inv_Sqrt;

architecture fpga of Inv_Sqrt is

  constant M : std_logic_vector(31 downto 0) := "01011111001101110101100111011111";  --The Maaaaaaaaaaaaaaaag!c Number
  constant threehalf : integer := 196608;
  signal   I         : std_logic_vector(31 downto 0) := (others =>'0');
  signal   X         : std_logic_vector(31 downto 0) := (others =>'0');
  signal   IIDhalf   : integer :=0;
  signal   I_mants_2 : integer :=0;
  signal   I_exp_2   : integer :=0;
  
  begin
  
  process(clk, rst)
	variable Dhalf     : std_logic_vector(31 downto 0) := (others =>'0');
	variable X_mants   : integer :=0;
	variable I_mants   : integer :=0;
	variable I_exp     : integer :=0;
	variable D_out_mants   : std_logic_vector(23 downto 0);
	
  begin
	if rst='1' then
		Dhalf    := (others =>'0');
		I     <= (others =>'0');
	    D_out_flt <= (others =>'0');
		
		
    else
        if(clk'event and clk = '1') then
			Dhalf    := '0'& D_in_flt(31 downto 1);   --D_in/2
			I        <= M + not Dhalf + 1;              ---- M - Dhalf   -- 1
			I_mants  := to_integer(unsigned('1'&I(22 downto 18)));
			I_exp	 := to_integer(unsigned(I(30 downto 23)));
			X        <= D_in_flt;                                        -- 1
			X_mants  := to_integer(unsigned('1'&X(22 downto 18)));
			
			I_mants_2 <= I_mants;         --2
			I_exp_2   <= I_exp;           --2
			
			IIDhalf   <= I_mants * I_mants * X_mants/2;           --2
			D_out_mants := std_logic_vector(to_unsigned(I_mants_2*(threehalf - IIDhalf), 24));
			
			if D_out_mants(23)='0' then
				D_out_flt <= '0'&std_logic_vector(to_unsigned(I_exp_2-1, 8))& D_out_mants(21 downto 0)&'0';       --3
			else 
				D_out_flt <= '0'&std_logic_vector(to_unsigned(I_exp_2, 8))& D_out_mants(22 downto 0);
			end if;
		end if;
	end if;
	
  end process;
end fpga;			
		
  
  


