import console_util
import grid

def test_merge(i_grid):
    if i_grid.grid[1][1].lower() == 'b':
        print(console_util.center_text("Passed!"))
    else:
        print(console_util.center_text("Failed!"))
        
def test_merge_primal():
    console_util.print_spacer()
    try:
        test_grid = grid.grid(4)
        test_grid.grid_display()
    except Exception as e:
        print(e)
        return None
    
    ''' 
    'a' indicates just placed
    -----------------                                                                
    | . | A | . | . |                                                                
    -----------------                                                                
    | A | a | A | A |                                                                
    -----------------                                                                
    | . | . | . | . |                                                                
    -----------------                                                                
    | . | . | . | . |                                                                
    ----------------- 
    '''
    test_grid.resource_place(1,0,'a')
    test_grid.grid_update()
    test_grid.resource_place(0,1,'a')
    test_grid.grid_update()
    test_grid.resource_place(1,2,'a')
    test_grid.grid_update()
    test_grid.resource_place(1,3,'a')
    test_grid.grid_update()
    test_grid.resource_place(3,3,'a')
    test_grid.grid_update()
    # Preparation complete
    test_grid.resource_place(1,1,'a')
    test_grid.grid_update()
    
    test_grid.grid_update()
    test_merge(test_grid)
    
    '''
    should become
    -----------------                                                                
    | . | . | . | . |                                                                
    -----------------                                                                
    | . | b | . | . |                                                                
    -----------------                                                                
    | . | . | . | . |                                                                
    -----------------                                                                
    | . | . | . | . |                                                                
    -----------------
    '''
    console_util.print_spacer()