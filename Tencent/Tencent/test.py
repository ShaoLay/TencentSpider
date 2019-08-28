#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Hamdi
import re


string = 'http://careers.tencent.com/jobdesc.html?postId=1154192479168237568'
content = re.findall(r'\d+', string)
print content[0]