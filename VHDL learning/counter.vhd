library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all;

entity counter is
  
  generic(
    start : integer := 1; -- can be negative, start < stop 
	stop  : integer := 5  --maxmium: 32767 ,minimum:-32768
  );
  
  port(
    clk : in std_logic;
	rst : in std_logic;
	count : out std_logic_vector(15 downto 0)
  );
  
end counter;
  
architecture behave of counter is
begin

  process(clk,rst)  
    variable number : integer := start;  	
  begin 
    if(rst='1') then
		number := start;
	else
        if(clk'event and clk='1') then
		    number := number+1;
			if number > stop then
			    number := start;
			end if;
		end if;
	end if;
	count <= std_logic_vector(to_signed(number, count'length));
   end process;
   
  

end behave;