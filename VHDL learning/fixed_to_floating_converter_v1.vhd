library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;

entity fix_to_flo is
  Generic (
		input_width : integer := 16;
		exp_bits_num : integer := 6 -- the whole file need to be re-writed if this value is changed
	);
  Port (
		input  : in std_logic_vector(input_width-1 downto 0);
		output : out std_logic_vector(input_width-1 downto 0); --assume that input_width=output_width
		clk : in std_logic;
		rst : in std_logic
	);
end fix_to_flo;

architecture behavioral of fix_to_flo is

  signal complement : std_logic_vector(input_width-1 downto 0);

  
  

begin

  output(input_width-1) <= '1' when(input(input_width-1)='1') else '0';
  complement <= not(input)+1 when(input(input_width-1)='1') else input;
  
  process(clk,rst)
	begin
		if(rst = '1') then
			output <= (others => '0');
		else
			if(clk'event and clk = '1') then
			        
					
					if (complement(input_width-1)='1') then
				        output(input_width-2 downto input_width-exp_bits_num-1) <= "001111";
				    	output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-2 downto exp_bits_num);
						
			    	elsif (complement(input_width-1 downto input_width-2)= "01") then
				        output(input_width-2 downto input_width-exp_bits_num-1) <= "001110";
			    		output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-3 downto exp_bits_num-1);
						
			        elsif (complement(input_width-1 downto input_width-3)= "001") then
				        output(input_width-2 downto input_width-exp_bits_num-1) <= "001101";
				    	output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-4 downto exp_bits_num-2);
						
			    	elsif (complement(input_width-1 downto input_width-4)= "0001") then
			    	    output(input_width-2 downto input_width-exp_bits_num-1) <= "001100";
			    		output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-5 downto exp_bits_num-3);
						
		    		elsif (complement(input_width-1 downto input_width-5)= "00001") then
		    		    output(input_width-2 downto input_width-exp_bits_num-1) <= "001011";
		    			output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-6 downto exp_bits_num-4);
						
		    		elsif (complement(input_width-1 downto input_width-6)= "000001") then
		    		    output(input_width-2 downto input_width-exp_bits_num-1) <= "001010";
		    			output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-7 downto exp_bits_num-5);
						
		    		elsif (complement(input_width-1 downto input_width-7)= "0000001") then
	    			    output(input_width-2 downto input_width-exp_bits_num-1) <= "001001";
		    			output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-8 downto exp_bits_num-6);
						
		    		elsif (complement(input_width-1 downto input_width-8)= "00000001") then
		    		    output(input_width-2 downto input_width-exp_bits_num-1) <= "001000";
		    			output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-9 downto 0)&"0";
						
		    		elsif (complement(input_width-1 downto input_width-9)= "000000001") then
		    		    output(input_width-2 downto input_width-exp_bits_num-1) <= "000111";
		    			output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-10 downto 0)&"00";
						
		    		elsif (complement(input_width-1 downto input_width-10)= "0000000001") then
		    		    output(input_width-2 downto input_width-exp_bits_num-1) <= "000110";
		    			output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-11 downto 0)&"000";
				        
			    	elsif (complement(input_width-1 downto input_width-11)= "00000000001") then
			    	    output(input_width-2 downto input_width-exp_bits_num-1) <= "000101";
			    		output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-12 downto 0)&"0000";
						
			    	elsif (complement(input_width-1 downto input_width-12)= "000000000001") then
			    	    output(input_width-2 downto input_width-exp_bits_num-1) <= "000100";
		    			output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-13 downto 0)&"00000";
					    
		    		elsif (complement(input_width-1 downto input_width-13)= "0000000000001") then
		    		    output(input_width-2 downto input_width-exp_bits_num-1) <= "000011";
			    		output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-14 downto 0)&"000000";
						
			    	elsif (complement(input_width-1 downto input_width-14)= "00000000000001") then
		    		    output(input_width-2 downto input_width-exp_bits_num-1) <= "000010";
			    		output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-15 downto 0)&"0000000"; 
						
			    	elsif (complement(input_width-1 downto input_width-15)= "000000000000001") then
			    	    output(input_width-2 downto input_width-exp_bits_num-1) <= "000001";
			    		output(input_width-exp_bits_num-2 downto 0) <= complement(input_width-16 downto 0)&"00000000";	
						
				    else
			    	    output(input_width-2 downto input_width-exp_bits_num-1) <= "000000";
			    		output(input_width-exp_bits_num-2 downto 0) <= "000000000";
						
			    	end if;
			end if;
		end if;	
    end process;
 end behavioral;