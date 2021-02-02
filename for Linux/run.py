# -*- coding: UTF-8 -*-

"""
author: Aaron
e-mail: w98987@126.com
wechat official account: 化院学生从不学化学
"""

import data
import ncovdata

all_data = data.get_data()
(n, s, f, a) = (0, 0, 0, 0)
for i in all_data:
    username = i[1]
    password = i[2]
    latitude = i[3]
    longitude = i[4]
    x = ncovdata.Clock(username, password, latitude, longitude)
    result = x.main()
    n += 1
    if result == 'success':
        s += 1
    elif result == 'already':
        a += 1
    elif result == 'fail':
        f += 1
print('%s complete:\n success: %s | already filled in: %s | fail: %s' % (n, s, a, f))
