library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity heartbeat is
    generic (
        COUNTER_WIDTH : positive := 4
    );
    port (
        clk   : in  std_logic;
        rst   : in  std_logic;
        pulse : out std_logic
    );
end entity heartbeat;

architecture rtl of heartbeat is
    signal count : unsigned(COUNTER_WIDTH - 1 downto 0) := (others => '0');
begin
    process (clk)
    begin
        if rising_edge(clk) then
            if rst = '1' then
                count <= (others => '0');
                pulse <= '0';
            else
                pulse <= '0';
                if count = (count'range => '1') then
                    count <= (others => '0');
                    pulse <= '1';
                else
                    count <= count + 1;
                end if;
            end if;
        end if;
    end process;
end architecture rtl;
