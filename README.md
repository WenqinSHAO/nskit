# nskit

_nskit_ is not an effort to re-engineer [netkit](http://wiki.netkit.org/index.php/Main_Page) or  [Kathara](https://github.com/Kidel/Kathara) or [mininet](https://github.com/mininet/mininet).
I just find [network namesapce](https://lwn.net/Articles/580893/) a simple yet sufficient tool to deploy and simulate networks within a single machine.
Therefore, I try to (for the sake of my own pleasure and trouble) to facilitate the following tasks:
1. topology specification via json or an interactive js script run on browser;
2. network topology visualization from topology file and runtime deployment;
3. network deployment according to topology file using network namespace; part of the mininet code shall be really useful here;
4. extensible automation for network related configurations, say the net.ip4/6.conf.* entries in sysctl;
5. some basic deployment support for routing/switching functions, say BIRD, linux bridge;
6. save and resume from runtime network config;
7. application deployemnt is probably a no-goal, but have dhcpd, radvd such basic network configuration related applications set up autmatically is somewhat tempting.


