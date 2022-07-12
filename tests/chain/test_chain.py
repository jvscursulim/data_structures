from chain import Chain, Node


def test_add_node():
    
    test_chain = Chain()
    circular_chain = Chain(circular = True)
    
    nodes1 = [Node(info = i, address = i) for i in range(3)]
    nodes2 = [Node(info = i, address = i) for i in range(3)]
    
    for node in nodes1:
    
        test_chain.add_node(node = node)
    
    for node in nodes2:
        
        circular_chain.add_node(node = node)
    
    assert len(test_chain.nodes_list) == 3
    assert test_chain.nodes_list[2].next_node_address is None
    assert test_chain.nodes_list[1].next_node_address == test_chain.nodes_list[2].address
    assert test_chain.nodes_list[0].next_node_address == test_chain.nodes_list[1].address
    assert len(circular_chain.nodes_list) == 3
    assert circular_chain.nodes_list[0].next_node_address == circular_chain.nodes_list[1].address
    assert circular_chain.nodes_list[1].next_node_address == circular_chain.nodes_list[2].address
    assert circular_chain.nodes_list[2].next_node_address == circular_chain.nodes_list[0].address
    

def test_delete_chain():
    
    test_chain = Chain()
    
    nodes = [Node(info = i, address = i) for i in range(3)]
    
    for node in nodes:
        
        test_chain.add_node(node = node)
    
    test_chain.delete_chain()
    
    assert len(test_chain.nodes_list) == 0


def test_is_chain_empty():
    
    test_chain = Chain()
    test_chain_empty = Chain()

    nodes = [Node(info = i, address = i) for i in range(3)]
    
    for node in nodes:
        
        test_chain.add_node(node = node)
    
    assert test_chain_empty.is_chain_empty()
    assert not test_chain.is_chain_empty()


def test_remove_node():
    
    test_chain = Chain()
    test_circular = Chain()

    nodes1 = [Node(info = i, address = i) for i in range(3)]
    nodes2 = [Node(info = i, address = i) for i in range(3)]
    
    for node in nodes1:
        
        test_chain.add_node(node = node)
        
    for node in nodes2:
        
        test_circular.add_node(node = node)
        
    test_chain.remove_node(element = 1)
    test_circular.remove_node(element = 1)
    
    assert len(test_chain.nodes_list) == 2
    assert test_chain.nodes_list[0].next_node_address == test_chain.nodes_list[-1].address
    assert not test_chain.search_element(element = 1)
    assert len(test_circular.nodes_list) == 2
    assert test_circular.nodes_list[0].next_node_address == test_circular.nodes_list[-1].address
    assert not test_circular.search_element(element = 1)
 
    
def test_search_element():
    
    test_chain = Chain()

    nodes = [Node(info = i, address = i) for i in range(3)]
    
    for node in nodes:
        
        test_chain.add_node(node = node)
    
    assert test_chain.search_element(element = 1)
    assert not test_chain.search_element(element = 4)
