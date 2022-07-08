from chain import Chain, Node


def test_add_node():
    
    test_chain = Chain()
    
    test_node_0 = Node(info = 0, address = 0)
    test_node_1 = Node(info = 1, address = 1)
    test_node_2 = Node(info = 2, address = 2)
    
    test_chain.add_node(node = test_node_0)
    test_chain.add_node(node = test_node_1)
    test_chain.add_node(node = test_node_2)
    
    assert len(test_chain.nodes_list) == 3
    assert test_chain.search_element(element = 0)
    assert test_chain.search_element(element = 1)
    assert test_chain.search_element(element = 2)
    assert test_node_0.next_node_address is None
    assert test_node_1.next_node_address == test_node_0.address
    assert test_node_2.next_node_address == test_node_1.address
    

def test_delete_chain():
    
    test_chain = Chain()
    
    test_node_0 = Node(info = 0, address = 0)
    test_node_1 = Node(info = 1, address = 1)
    test_node_2 = Node(info = 2, address = 2)
    
    test_chain.add_node(node = test_node_0)
    test_chain.add_node(node = test_node_1)
    test_chain.add_node(node = test_node_2)
    
    test_chain.delete_chain()
    
    assert len(test_chain.nodes_list) == 0


def test_is_chain_empty():
    
    test_chain = Chain()
    test_chain_empty = Chain()

    test_node_0 = Node(info = 0, address = 0)
    test_node_1 = Node(info = 1, address = 1)
    test_node_2 = Node(info = 2, address = 2)
    
    test_chain.add_node(node = test_node_0)
    test_chain.add_node(node = test_node_1)
    test_chain.add_node(node = test_node_2)
    
    assert test_chain_empty.is_chain_empty()
    assert not test_chain.is_chain_empty()


def test_remove_node():
    
    test_chain = Chain()

    test_node_0 = Node(info = 0, address = 0)
    test_node_1 = Node(info = 1, address = 1)
    test_node_2 = Node(info = 2, address = 2)
    
    test_chain.add_node(node = test_node_0)
    test_chain.add_node(node = test_node_1)
    test_chain.add_node(node = test_node_2)
    
    test_chain.remove_node(element = 1)
    
    assert len(test_chain.nodes_list) == 2
    assert test_node_2.next_node_address == test_node_0.address
    assert not test_chain.search_element(element = 1)
 
    
def test_search_element():
    
    test_chain = Chain()

    test_node_0 = Node(info = 0, address = 0)
    test_node_1 = Node(info = 1, address = 1)
    test_node_2 = Node(info = 2, address = 2)
    
    test_chain.add_node(node = test_node_0)
    test_chain.add_node(node = test_node_1)
    test_chain.add_node(node = test_node_2)
    
    assert test_chain.search_element(element = 1)
    assert not test_chain.search_element(element = 4)
