def maxima_points(intervals):
    result = []
    for i in range(len(intervals)):
        try:
            if intervals[i] == 'positive' and intervals[i + 2] == 'negative':
                result.append(intervals[i + 1])
        except IndexError:
            pass
    if len(result) == 0:
        result.append(None)
    return result