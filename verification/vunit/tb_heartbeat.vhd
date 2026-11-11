library ieee;
use ieee.std_logic_1164.all;
library vunit_lib;
context vunit_lib.vunit_context;

entity tb_heartbeat is
    generic (runner_cfg : string);
end entity;

architecture test of tb_heartbeat is
    constant CLK_PERIOD : time := 10 ns;
    signal clk   : std_logic := '0';
    signal rst   : std_logic := '1';
    signal pulse : std_logic;
begin
    clk <= not clk after CLK_PERIOD / 2;

    dut : entity work.heartbeat
        generic map (COUNTER_WIDTH => 3)
        port map (clk => clk, rst => rst, pulse => pulse);

    main : process
    begin
        test_runner_setup(runner, runner_cfg);

        if run("reset_and_count") then
            wait until rising_edge(clk);
            wait until rising_edge(clk);
            rst <= '0';

            -- 3-bit counter pulses after eight active clock edges.
            for i in 0 to 6 loop
                wait until rising_edge(clk);
                wait for 1 ns;
                check_equal(pulse, '0');
            end loop;

            wait until rising_edge(clk);
            wait for 1 ns;
            check_equal(pulse, '1');
        end if;

        test_runner_cleanup(runner);
        wait;
    end process;
end architecture;
