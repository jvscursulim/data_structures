from queue import DoubleQueue


def test_add_item_at_the_end():
    
    test_double_queue = DoubleQueue()
    
    for i in range(3):
        
        test_double_queue.add_item_at_the_end(i)
        
    last_item = test_double_queue.item_list[-1]
    
    assert len(test_double_queue.item_list) == 3
    assert last_item == 2
    

def test_add_item_at_the_start():
    
    test_double_queue = DoubleQueue()
    
    for i in range(3):
        
        test_double_queue.add_item_at_the_start(i)
        
    first_item = test_double_queue.item_list[0]
    
    assert len(test_double_queue.item_list) == 3
    assert first_item == 2
    
    
def test_delete_double_queue():
    
    test_double_queue = DoubleQueue()
    
    for i in range(3):
        
        test_double_queue.add_item_at_the_start(i)
        
    test_double_queue.delete_double_queue()
    
    assert len(test_double_queue.item_list) == 0


def test_is_double_queue_empty():
    
    test_double_queue = DoubleQueue()
    test_empty_double_queue = DoubleQueue()
    
    for i in range(3):
        
        test_double_queue.add_item_at_the_end(i)
        
    assert test_empty_double_queue.is_double_queue_empty()
    assert not test_double_queue.is_double_queue_empty()
    

def test_remove_item_at_the_end():
    
    test_double_queue = DoubleQueue()
    
    for i in range(3):
        
        test_double_queue.add_item_at_the_end(i)
        
    last_item = test_double_queue.item_list[-1]
    
    test_double_queue.remove_item_at_the_end()
    
    assert len(test_double_queue.item_list) == 2
    assert not last_item in test_double_queue.item_list
    

def test_remove_item_at_the_start():
    
    test_double_queue = DoubleQueue()
    
    for i in range(3):
        
        test_double_queue.add_item_at_the_start(i)
        
    first_item = test_double_queue.item_list[0]
    
    test_double_queue.remove_item_at_the_start()
    
    assert len(test_double_queue.item_list) == 2
    assert not first_item in test_double_queue.item_list
    
    
    
    
    