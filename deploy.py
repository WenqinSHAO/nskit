from pyroute2 import netns, IPDB, IPRoute
import networkx as nx


def deploy(topo):
    """Deploy a given topology with network namespace

    Args:
        topo (nx.Graph): the network topo to be deployed
    """
    # sanity check should be done outside
    # add nodes, each as a network namespace
    for n in topo.nodes():
        netns.create(n)
    # add links and attribute each interface to proper network namespace
    ip = IPRoute()
    for (i, j, intf_pair) in topo.edges.data('interfaces'):
        print(i, j, intf_pair)
        ip.link('add', ifname=intf_pair[0], kind='veth', peer=intf_pair[1])
        for ns, intf in zip([i,j], intf_pair):
            intf_idx = ip.link_lookup(ifname=intf)[0]
            ip.link('set', index=intf_idx, net_ns_fd=ns)

