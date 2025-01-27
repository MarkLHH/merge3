import console_util
import invasion_grid
import test

def main():
    console_util.print_spacer()
    try:
        test_grid = invasion_grid.grid(4)
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
    test_grid.place_resource(1,0,'a')
    test_grid.check_merge_ava()
    test_grid.place_resource(0,1,'a')
    test_grid.check_merge_ava()
    test_grid.place_resource(1,2,'a')
    test_grid.check_merge_ava()
    test_grid.place_resource(1,3,'a')
    test_grid.check_merge_ava()
    # Preparation complete
    test_grid.place_resource(1,1,'a')
    test_grid.check_merge_ava()
    
    test.test_merge(test_grid)
    
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
main()