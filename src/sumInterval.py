def sum_of_intervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = [merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1])]
        else:
            merged_intervals.append(interval)

    total_length = sum(interval[1] - interval[0] for interval in merged_intervals)

    return total_length

intervals = [[1, 2], [6, 10], [11, 15]]
result = sum_of_intervals(intervals)
print(result)