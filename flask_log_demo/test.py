# -*- coding: utf-8 -*-
# @Author: Catcher
# @Date: 2020-04-12 17:17:40
# @Email: catcheryp@gmail.com
# @Last Modified by: Catcher
# @Last Modified time: 2020-04-12 17:26:37

import time 

n = 0
while True:
	f = open('test.log', 'a')
	f.write(str(n)*15 + "\n")
	n += 1
	time.sleep(3)
	print n
	f.close()