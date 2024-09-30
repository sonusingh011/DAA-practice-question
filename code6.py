def maximum_units(boxTypes, truckSize):
   
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    
    total_units = 0
    
    for boxes, units_per_box in boxTypes:
        if truckSize > 0:
            
            boxes_to_take = min(truckSize, boxes)
            total_units += boxes_to_take * units_per_box
            truckSize -= boxes_to_take
        else:
            break 
    
    return total_units

# Example usage:
boxTypes = [[1, 3], [2, 2], [3, 1]]  
truckSize = 4

result = maximum_units(boxTypes, truckSize)
print(f"Maximum units that can be loaded: {result}")
