def merge(intervals):
    
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    
    for interval in intervals:
        
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example usage
if __name__ == "__main__":
    intervals = [[1, 4], [3, 6], [7, 10], [13, 20]]
    result = merge(intervals)
    print("Merged intervals:", result)