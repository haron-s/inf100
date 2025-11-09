import json
from datetime import datetime

def hot_period(temperatures, threshold):
    i_array, i_list = [], []
    for i, temp in enumerate(temperatures):
        if temp >= threshold:
            i_list.append(i)
        elif i_list:
            i_array.append(i_list)
            i_list = []
    if i_list:
        i_array.append(i_list)
    
    if i_array:
        longest_stretch = max(i_array[::-1], key=len)
        longest_period = (longest_stretch[0], longest_stretch[-1])
    else:
        longest_period = (None, None)

    return longest_period

def convert(datetime_str):
    format = '%Y-%m-%d'
    datetime_object= datetime.strptime(datetime_str, format)

    return datetime_object