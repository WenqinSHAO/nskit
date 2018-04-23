from pyroute2 import netns, IPDB
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
    ip = IPDB()
    for (i, j, intf_pair) in topo.edges.data('interfaces'):
        ip.create(ifname=intf_pair[0], peer=intf_pair[1], kind='veth').commit()
        with ip.interfaces.intf_pair[0] as veth:
            veth.net_ns_fd = i
        with ip.interfaces.intf_pair[1] as veth:
            veth.net_ns_fd = j
    ip.release()

