def meter_handling(meter, user_input):
    if user_input > list(meter.keys())[-1]:
        item = meter[list(meter.keys())[-1]]
    else:
        item = meter[user_input]
    
    return item

def kind_1_score_meter(level):
    level_score_meter = {
        1: 1,
        2: 2,
        3: 4,
        4: 6,
        5: 8
    }
    # This handle level larger than 5
    score = meter_handling(level_score_meter, level)
     
    return score

def kind_2_score_meter(level):
    level_score_meter = {
        1: 1,
        2: 3,
        3: 5,
        4: 7,
        5: 9
    }
    # This handle level larger than 5
    score = meter_handling(level_score_meter, level)
    return score

def obs_2_sr_meter(connected):
    connected_sr_meter = {
        3: 5,
        4: 6,
        5: 7,
        6: 8,
        7: 9
    }
    # This handle connection larger than 7
    sr = meter_handling(connected_sr_meter, connected)
    return sr
