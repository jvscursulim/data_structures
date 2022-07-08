from stack import Stack


def test_delete_stack():
    
    test_stack = Stack()
    
    for i in range(3):
        
        test_stack.push_item(i)
        
    test_stack.delete_stack()
    
    assert len(test_stack.item_list) == 0
    
    
def test_is_stack_empty():
    
    test_stack_empty = Stack()
    test_stack = Stack()
    
    for i in range(3):
        
        test_stack.push_item(i)
        
    assert test_stack_empty.is_stack_empty()
    assert not test_stack.is_stack_empty()
    

def test_pop_item():
    
    test_stack = Stack()
    
    for i in range(3):
        
        test_stack.push_item(i)
        
    last_element = test_stack.item_list[-1]
    
    test_stack.pop_item()
    
    assert len(test_stack.item_list) == 2
    assert not last_element in test_stack.item_list


def test_push_item():
    
    test_stack = Stack()
    
    for i in range(3):
        
        test_stack.push_item(i)
    
    assert len(test_stack.item_list) != 0
    assert test_stack.item_list.index(2) == len(test_stack.item_list) - 1
    