from queue import Queue


def test_add_item():
    
    test_queue = Queue()
    
    for i in range(3):
        
        test_queue.add_item(i)
        
    assert len(test_queue.item_list) != 0
    assert test_queue.item_list.index(2) == len(test_queue.item_list) - 1
    

def test_delete_queue():
    
    test_queue = Queue()
    
    for i in range(3):
        
        test_queue.add_item(i)
        
    test_queue.delete_queue()
    
    assert len(test_queue.item_list) == 0
    
    
def test_is_queue_empty():
    
    test_queue = Queue()
    test_empty_queue = Queue()
    
    for i in range(3):
        
        test_queue.add_item(i)
        
    assert test_empty_queue.is_queue_empty()
    assert not test_queue.is_queue_empty()
    
    
def test_remove_item():
    
    test_queue = Queue()
    
    for i in range(3):
        
        test_queue.add_item(i)
        
    first_element = test_queue.item_list[0]
    
    test_queue.remove_item()
    
    assert len(test_queue.item_list) == 2
    assert not first_element in test_queue.item_list