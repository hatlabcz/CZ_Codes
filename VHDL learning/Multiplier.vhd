library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
Library UNISIM;
use UNISIM.vcomponents.all;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity Multiplier is	
	Generic (
		bus_ina_width : integer := 16;
		ina_signed : boolean := TRUE; 
		bus_inb_width : integer := 16;
		inb_signed : boolean := TRUE;
		bus_output_width : integer := 17;
		latch_input : boolean := FALSE
	);
	
	Port (
		A : in std_logic_vector(bus_ina_width-1 downto 0); 
		B : in std_logic_vector(bus_inb_width-1 downto 0);
		Dout : out std_logic_vector(bus_output_width-1 downto 0);
		clk : in std_logic;
		rst : in std_logic
	);
	
end Multiplier;

architecture Behavioral of Multiplier is

signal A_in:	std_logic_vector (29 downto 0);
signal B_in:	std_logic_vector (17 downto 0);
signal P_out:	std_logic_vector (47 downto 0);

begin

A_input_29:	if(bus_ina_width = 29) generate
				A_in <= 	'0'&A when (ina_signed = FALSE) else
							A(28)&A when (ina_signed = TRUE) else (others => '0');
			end generate A_input_29;
			
A_input_28:	if(bus_ina_width = 28) generate
				A_in(29 downto 28) <= (others => '1') when (ina_signed and A(bus_inb_width-1) = '1') else (others => '0');
				A_in(bus_ina_width-1 downto 0) <= 	A;
			end generate A_input_28;

A_input_low:	if(bus_ina_width < 28) generate
					A_in(29 downto bus_ina_width) <=(others => '1') when (ina_signed and A(bus_inb_width-1) = '1') else (others => '0');
					A_in(bus_ina_width-1 downto 0) <= A;
				end generate A_input_low;			
			
B_input_17:	if(bus_inb_width = 17) generate
				B_in <= 	'0'&B when (inb_signed = FALSE) else
							B(16)&B when (inb_signed = TRUE) else (others => '0');
			end generate B_input_17;
			
B_input_16:	if(bus_inb_width = 16) generate
				B_in(17 downto 16) <= (others => '1') when (inb_signed and B(bus_inb_width-1) = '1') else (others => '0');
				B_in(bus_inb_width-1 downto 0) <= 	B;
			end generate B_input_16;

B_input_low:	if(bus_inb_width < 16) generate
					B_in(17 downto bus_inb_width) <= (others => '1') when (inb_signed and B(bus_inb_width-1) = '1') else (others => '0');
					B_in(bus_inb_width-1 downto 0) <= 	B;
				end generate B_input_low;			
				
out_signed_44:	 if(ina_signed = TRUE and inb_signed = TRUE and bus_output_width = 44) generate
				    Dout <= P_out(bus_ina_width+bus_inb_width-1 downto bus_ina_width+bus_inb_width-bus_output_width);
			     end generate out_signed_44;
			
out_signed_l44:	    if(ina_signed = TRUE and inb_signed = TRUE and bus_output_width < 44) generate
                        Dout <= P_out(bus_ina_width+bus_inb_width-2 downto bus_ina_width+bus_inb_width-bus_output_width-1);
                    end generate out_signed_l44;			
			
out_def:	if(ina_signed = FALSE or inb_signed = FALSE) generate
				Dout <= P_out(bus_ina_width+bus_inb_width-1 downto bus_ina_width+bus_inb_width-bus_output_width);
			end generate out_def;

DSP_REG: if(latch_input) generate
DSP48E1_inst : DSP48E1
   generic map (
      -- Feature Control Attributes: Data Path Selection
      A_INPUT => "DIRECT",               -- Selects A input source, "DIRECT" (A port) or "CASCADE" (ACIN port)
      B_INPUT => "DIRECT",               -- Selects B input source, "DIRECT" (B port) or "CASCADE" (BCIN port)
      USE_DPORT => FALSE,                -- Select D port usage (TRUE or FALSE)
      USE_MULT => "MULTIPLY",            -- Select multiplier usage ("MULTIPLY", "DYNAMIC", or "NONE")
      USE_SIMD => "ONE48",               -- SIMD selection ("ONE48", "TWO24", "FOUR12")
      -- Pattern Detector Attributes: Pattern Detection Configuration
      AUTORESET_PATDET => "NO_RESET",    -- "NO_rst", "rst_MATCH", "rst_NOT_MATCH" 
      MASK => X"3fffffffffff",           -- 48-bit mask value for pattern detect (1=ignore)
      PATTERN => X"000000000000",        -- 48-bit pattern match for pattern detect
      SEL_MASK => "MASK",                -- "C", "MASK", "ROUNDING_MODE1", "ROUNDING_MODE2" 
      SEL_PATTERN => "PATTERN",          -- Select pattern value ("PATTERN" or "C")
      USE_PATTERN_DETECT => "NO_PATDET", -- Enable pattern detect ("PATDET" or "NO_PATDET")
      -- Register Control Attributes: Pipeline Register Configuration
      ACASCREG => 1,                     -- Number of pipeline stages between A/ACIN and ACOUT (0, 1 or 2)
      ADREG => 0,                        -- Number of pipeline stages for pre-adder (0 or 1)
      ALUMODEREG => 0,                   -- Number of pipeline stages for ALUMODE (0 or 1)
      AREG => 1,                         -- Number of pipeline stages for A (0, 1 or 2)
      BCASCREG => 1,                     -- Number of pipeline stages between B/BCIN and BCOUT (0, 1 or 2)
      BREG => 1,                         -- Number of pipeline stages for B (0, 1 or 2)
      CARRYINREG => 0,                   -- Number of pipeline stages for CARRYIN (0 or 1)
      CARRYINSELREG => 0,                -- Number of pipeline stages for CARRYINSEL (0 or 1)
      CREG => 0,                         -- Number of pipeline stages for C (0 or 1)
      DREG => 0,                         -- Number of pipeline stages for D (0 or 1)
      INMODEREG => 1,                    -- Number of pipeline stages for INMODE (0 or 1)
      MREG => 0,                         -- Number of multiplier pipeline stages (0 or 1)
      OPMODEREG => 1,                    -- Number of pipeline stages for OPMODE (0 or 1)
      PREG => 1                          -- Number of pipeline stages for P (0 or 1)
   )
   port map (
      -- Cascade: 30-bit (each) output: Cascade Ports
      ACOUT => open,                   -- 30-bit output: A port cascade output
      BCOUT => open,                   -- 18-bit output: B port cascade output
      CARRYCASCOUT => open,     -- 1-bit output: Cascade carry output
      MULTSIGNOUT => open,       -- 1-bit output: Multiplier sign cascade output
      PCOUT => open,                   -- 48-bit output: Cascade output
      -- Control: 1-bit (each) output: Control Inputs/Status Bits
      OVERFLOW => open,             -- 1-bit output: Overflow in add/acc output
      PATTERNBDETECT => open, -- 1-bit output: Pattern bar detect output
      PATTERNDETECT => open,   -- 1-bit output: Pattern detect output
      UNDERFLOW => open,           -- 1-bit output: Underflow in add/acc output
      -- Data: 4-bit (each) output: Data Ports
      CARRYOUT => open,             -- 4-bit output: Carry output
      P => P_out,                           -- 48-bit output: Primary data output
      -- Cascade: 30-bit (each) input: Cascade Ports
      ACIN => (others => '0'),                     -- 30-bit input: A cascade data input
      BCIN => (others => '0'),                     -- 18-bit input: B cascade input
      CARRYCASCIN => '0',       -- 1-bit input: Cascade carry input
      MULTSIGNIN => '0',         -- 1-bit input: Multiplier sign input
      PCIN => (others => '0'),                     -- 48-bit input: P cascade input
      -- Control: 4-bit (each) input: Control Inputs/Status Bits
      ALUMODE => (others => '0'),               -- 4-bit input: ALU control input
      CARRYINSEL => (others => '0'),         -- 3-bit input: Carry select input
      CLK => clk,                       -- 1-bit input: Clock input
      INMODE => "10001",                 -- 5-bit input: INMODE control input
      OPMODE => "0000101",                 -- 7-bit input: Operation mode input
      -- Data: 30-bit (each) input: Data Ports
      A => A_in,                           -- 30-bit input: A data input
      B => B_in,                           -- 18-bit input: B data input
      C => (others => '0'),                           -- 48-bit input: C data input
      CARRYIN => '0',               -- 1-bit input: Carry input signal
      D => (others => '0'),                           -- 25-bit input: D data input
      -- rst/Clock Enable: 1-bit (each) input: rst/Clock Enable Inputs
      CEA1 => '1',                     -- 1-bit input: Clock enable input for 1st stage AREG
      CEA2 => '0',                     -- 1-bit input: Clock enable input for 2nd stage AREG
      CEAD => '0',                     -- 1-bit input: Clock enable input for ADREG
      CEALUMODE => '0',           -- 1-bit input: Clock enable input for ALUMODE
      CEB1 => '1',                     -- 1-bit input: Clock enable input for 1st stage BREG
      CEB2 => '0',                     -- 1-bit input: Clock enable input for 2nd stage BREG
      CEC => '0',                       -- 1-bit input: Clock enable input for CREG
      CECARRYIN => '0',           -- 1-bit input: Clock enable input for CARRYINREG
      CECTRL => '1',                 -- 1-bit input: Clock enable input for OPMODEREG and CARRYINSELREG
      CED => '0',                       -- 1-bit input: Clock enable input for DREG
      CEINMODE => '1',             -- 1-bit input: Clock enable input for INMODEREG
      CEM => '0',                       -- 1-bit input: Clock enable input for MREG
      CEP => '1',                       -- 1-bit input: Clock enable input for PREG
      RSTA => rst,                     -- 1-bit input: rst input for AREG
      RSTALLCARRYIN => '0',   -- 1-bit input: rst input for CARRYINREG
      RSTALUMODE => '0',         -- 1-bit input: rst input for ALUMODEREG
      RSTB => rst,                     -- 1-bit input: rst input for BREG
      RSTC => '0',                     -- 1-bit input: rst input for CREG
      RSTCTRL => '0',               -- 1-bit input: rst input for OPMODEREG and CARRYINSELREG
      RSTD => '0',                     -- 1-bit input: rst input for DREG and ADREG
      RSTINMODE => rst,           -- 1-bit input: rst input for INMODEREG
      RSTM => '0',                     -- 1-bit input: rst input for MREG
      RSTP => rst                      -- 1-bit input: rst input for PREG
   );
   
end generate DSP_REG;

DSP_NO_REG: if(latch_input = FALSE) generate
DSP48E1_inst : DSP48E1
   generic map (
      -- Feature Control Attributes: Data Path Selection
      A_INPUT => "DIRECT",               -- Selects A input source, "DIRECT" (A port) or "CASCADE" (ACIN port)
      B_INPUT => "DIRECT",               -- Selects B input source, "DIRECT" (B port) or "CASCADE" (BCIN port)
      USE_DPORT => FALSE,                -- Select D port usage (TRUE or FALSE)
      USE_MULT => "MULTIPLY",            -- Select multiplier usage ("MULTIPLY", "DYNAMIC", or "NONE")
      USE_SIMD => "ONE48",               -- SIMD selection ("ONE48", "TWO24", "FOUR12")
      -- Pattern Detector Attributes: Pattern Detection Configuration
      AUTORESET_PATDET => "NO_RESET",    -- "NO_rst", "rst_MATCH", "rst_NOT_MATCH" 
      MASK => X"3fffffffffff",           -- 48-bit mask value for pattern detect (1=ignore)
      PATTERN => X"000000000000",        -- 48-bit pattern match for pattern detect
      SEL_MASK => "MASK",                -- "C", "MASK", "ROUNDING_MODE1", "ROUNDING_MODE2" 
      SEL_PATTERN => "PATTERN",          -- Select pattern value ("PATTERN" or "C")
      USE_PATTERN_DETECT => "NO_PATDET", -- Enable pattern detect ("PATDET" or "NO_PATDET")
      -- Register Control Attributes: Pipeline Register Configuration
      ACASCREG => 0,                     -- Number of pipeline stages between A/ACIN and ACOUT (0, 1 or 2)
      ADREG => 0,                        -- Number of pipeline stages for pre-adder (0 or 1)
      ALUMODEREG => 0,                   -- Number of pipeline stages for ALUMODE (0 or 1)
      AREG => 0,                         -- Number of pipeline stages for A (0, 1 or 2)
      BCASCREG => 0,                     -- Number of pipeline stages between B/BCIN and BCOUT (0, 1 or 2)
      BREG => 0,                         -- Number of pipeline stages for B (0, 1 or 2)
      CARRYINREG => 0,                   -- Number of pipeline stages for CARRYIN (0 or 1)
      CARRYINSELREG => 0,                -- Number of pipeline stages for CARRYINSEL (0 or 1)
      CREG => 0,                         -- Number of pipeline stages for C (0 or 1)
      DREG => 0,                         -- Number of pipeline stages for D (0 or 1)
      INMODEREG => 1,                    -- Number of pipeline stages for INMODE (0 or 1)
      MREG => 0,                         -- Number of multiplier pipeline stages (0 or 1)
      OPMODEREG => 1,                    -- Number of pipeline stages for OPMODE (0 or 1)
      PREG => 1                          -- Number of pipeline stages for P (0 or 1)
   )
   port map (
      -- Cascade: 30-bit (each) output: Cascade Ports
      ACOUT => open,                   -- 30-bit output: A port cascade output
      BCOUT => open,                   -- 18-bit output: B port cascade output
      CARRYCASCOUT => open,     -- 1-bit output: Cascade carry output
      MULTSIGNOUT => open,       -- 1-bit output: Multiplier sign cascade output
      PCOUT => open,                   -- 48-bit output: Cascade output
      -- Control: 1-bit (each) output: Control Inputs/Status Bits
      OVERFLOW => open,             -- 1-bit output: Overflow in add/acc output
      PATTERNBDETECT => open, -- 1-bit output: Pattern bar detect output
      PATTERNDETECT => open,   -- 1-bit output: Pattern detect output
      UNDERFLOW => open,           -- 1-bit output: Underflow in add/acc output
      -- Data: 4-bit (each) output: Data Ports
      CARRYOUT => open,             -- 4-bit output: Carry output
      P => P_out,                           -- 48-bit output: Primary data output
      -- Cascade: 30-bit (each) input: Cascade Ports
      ACIN => (others => '0'),                     -- 30-bit input: A cascade data input
      BCIN => (others => '0'),                     -- 18-bit input: B cascade input
      CARRYCASCIN => '0',       -- 1-bit input: Cascade carry input
      MULTSIGNIN => '0',         -- 1-bit input: Multiplier sign input
      PCIN => (others => '0'),                     -- 48-bit input: P cascade input
      -- Control: 4-bit (each) input: Control Inputs/Status Bits
      ALUMODE => (others => '0'),               -- 4-bit input: ALU control input
      CARRYINSEL => (others => '0'),         -- 3-bit input: Carry select input
      CLK => clk,                       -- 1-bit input: Clock input
      INMODE => (others => '0'),                 -- 5-bit input: INMODE control input
      OPMODE => "0000101",                 -- 7-bit input: Operation mode input
      -- Data: 30-bit (each) input: Data Ports
      A => A_in,                           -- 30-bit input: A data input
      B => B_in,                           -- 18-bit input: B data input
      C => (others => '0'),                           -- 48-bit input: C data input
      CARRYIN => '0',               -- 1-bit input: Carry input signal
      D => (others => '0'),                           -- 25-bit input: D data input
      -- rst/Clock Enable: 1-bit (each) input: rst/Clock Enable Inputs
      CEA1 => '0',                     -- 1-bit input: Clock enable input for 1st stage AREG
      CEA2 => '0',                     -- 1-bit input: Clock enable input for 2nd stage AREG
      CEAD => '0',                     -- 1-bit input: Clock enable input for ADREG
      CEALUMODE => '0',           -- 1-bit input: Clock enable input for ALUMODE
      CEB1 => '0',                     -- 1-bit input: Clock enable input for 1st stage BREG
      CEB2 => '0',                     -- 1-bit input: Clock enable input for 2nd stage BREG
      CEC => '0',                       -- 1-bit input: Clock enable input for CREG
      CECARRYIN => '0',           -- 1-bit input: Clock enable input for CARRYINREG
      CECTRL => '1',                 -- 1-bit input: Clock enable input for OPMODEREG and CARRYINSELREG
      CED => '0',                       -- 1-bit input: Clock enable input for DREG
      CEINMODE => '1',             -- 1-bit input: Clock enable input for INMODEREG
      CEM => '0',                       -- 1-bit input: Clock enable input for MREG
      CEP => '1',                       -- 1-bit input: Clock enable input for PREG
      RSTA => rst,                     -- 1-bit input: rst input for AREG
      RSTALLCARRYIN => '0',   -- 1-bit input: rst input for CARRYINREG
      RSTALUMODE => '0',         -- 1-bit input: rst input for ALUMODEREG
      RSTB => rst,                     -- 1-bit input: rst input for BREG
      RSTC => '0',                     -- 1-bit input: rst input for CREG
      RSTCTRL => '0',               -- 1-bit input: rst input for OPMODEREG and CARRYINSELREG
      RSTD => '0',                     -- 1-bit input: rst input for DREG and ADREG
      RSTINMODE => rst,           -- 1-bit input: rst input for INMODEREG
      RSTM => '0',                     -- 1-bit input: rst input for MREG
      RSTP => rst                      -- 1-bit input: rst input for PREG
   );
   
end generate DSP_NO_REG;

end Behavioral;
