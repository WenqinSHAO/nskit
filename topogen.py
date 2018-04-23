import networkx as nx


def star(n=2, star='sw'):
    """Generates a simple star topology

    Args:
        n (int): number of endhost attached to the central, the name pattern is 'h%d'
        star (str): the name of the central, the default value is 'sw'

    Returns:
        topo (nx.Graph): the generated network
    """
    topo = nx.Graph()
    hosts = ['h%d' % j for j in range(n)]
    topo.add_nodes_from(hosts)
    topo.add_node(star)
    topo.nodes[star]['interfaces'] = []
    sw_intf_idx = 0
    for n in topo.nodes():
        if 'h' in n:
            h_intf = '%s-eth0' % n
            sw_intf = '%s-eth%d' % (star, sw_intf_idx)
            topo.nodes[n]['interfaces'] = []
            topo.nodes[n]['interfaces'].append(h_intf)
            topo.nodes[star]['interfaces'].append(sw_intf)
            topo.add_edge(n, star)
            topo[n][star]['interfaces'] = [h_intf, sw_intf]
            sw_intf_idx += 1
    return topo



