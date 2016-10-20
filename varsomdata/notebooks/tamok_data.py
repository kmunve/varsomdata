#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from runmatrix import pickle_warnings
import makepickle as mp

import openpyxl as xl

'''


__author__ = 'kmu'
'''

regions = [129]
date_from = "2014-12-01"
date_to = "2015-06-01"
pickle_file_name = "tamok_2014_2015.pck"


# pickle_warnings(regions, date_from, date_to, pickle_file_name)


data_set = mp.unpickle_anything(pickle_file_name)

"""https://automatetheboringstuff.com/chapter12/"""
wb = xl.Workbook()
type(wb)

#wb.get_sheet_names()

sheet = wb.active
sheet.title = 'Tamok 2014_2015'
print(wb.get_sheet_names())

for i in range(10):
    cellno = "A"+str(i)
    sheet[cellno] = data_set[i].danger_level_name

wb.save('tamok.xlsx')

a=1