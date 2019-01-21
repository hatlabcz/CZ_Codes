library ieee;
    use ieee.std_logic_1164.all;
    use ieee.std_logic_arith.all;
    use ieee.std_logic_unsigned.all;

    entity circ is
    port (  a    :in std_logic_vector (15 downto 0);
    b    :in std_logic_vector (15 downto 0);
    c    :out  std_logic_vector (31 downto 0)
        );

    end entity;

    architecture data of circ is
    begin
process(a,b)
begin
c<= '0';   
for i in 15 to 0 loop
if (b(i) = '1') then
c<=c+a;
end if;
END LOOP;

end process;
    end data;