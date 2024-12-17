import common
import itertools
from datetime import *

output = ''
min_route = 100
max_route = 0
min_output = ''
start_at = datetime(year=2024,month=12,day=22,hour=11,minute=00)
for r in itertools.permutations(common.point_name):
    first_point = r[0]
    output = ''
    output += common.point_name[first_point]
    total_route = 0
    total_time = 0
    for i in range(1,9):
        next_point = r[i]
        try:
            distance = common.distance_2point[(r[i-1], r[i])]
        except KeyError:
            distance = common.distance_2point[(r[i], r[i-1])]
        output += ' -> ' + str(int(distance/1.1)) + '分'
        output +=  ' -> ' + common.point_name[next_point]
        total_route += distance
        total_time += int(distance/1.1)
        end_at = start_at + timedelta(minutes = total_time)
        output += str(end_at)
    #if min_route > total_route:
    if max_route < total_route:
        min_route = total_route
        min_output = output
        min_time = int(total_time)

print(min_output)
print(int(min_route)*10, 'm ', min_time , '分')
