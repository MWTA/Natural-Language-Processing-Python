#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
	Remove numeros
'''
import re

text_with_numbers = 'O numero da nossa casa 56, apto 306'
text_without_numbers = re.sub('[-|0-9]',' ', text_with_numbers)
print text_without_numbers

text_with_numbers_2 = "i'm back baby!!!, Data Science ??;;;()"
print re.sub(r'[-./?!,":;()\']',' ',text_with_numbers_2)