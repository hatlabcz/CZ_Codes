library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all;

entity tuneable_clk is
  
  generic(
    frqeuency : integer := 50  --in MHz
  );
  
  port(
    clk_100 : in std_logic;
	clk_out : out std_logic
  );
  
end tuneable_clk;
  
architecture behave of tuneable_clk is

  signal toggle : std_logic :='0';
  signal count  : integer := 0;
  constant max  : integer := 50/frqeuency-1;
  

begin

  process(clk_100)  	
  begin 
    if(clk_100'event and clk_100='1') then
		if count = max then
		    toggle <= not toggle;
			count <= 0;
		else
			count <= count+1;
		end if;
	end if;
  end process;
  
  clk_out <= toggle; 

end behave;