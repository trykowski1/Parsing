'''
import xml.etree.ElementTree as ET
tree = ET.parse('foo.xml')
root = tree.getroot()


for tr in root.findall('/html/body/div/div/div/div/div/table/tbody/tr'):
  currency = tr.get('data-currency-id')
  print currency
  for td in tr.findall('td'):
    if td.get('class')=='currency_table_buy':
      print ("Buy: ",td.text)
    if td.get('class')=='currency_table_sell':
      print ("Sell: ",td.text)



table = ET.XML('foo.xml')
rows = iter(table)


headers = [col.text for col in next(rows)]
print headers

for row in rows:
    values = [col.text for col in row]
    print dict(zip(headers, values))
'''


#-*- coding: UTF-8 -*-
import re

fil = open('foo.xml', 'r')

for f in fil:
  m = re.search(r'^<a.+(EUR|USD|CHF|GBP)\W+a>$', f, re.M)
  if m: 
    print f
    for w in fil:
      mn = re.search(r'^<td.+currency_table.+td>$', w, re.M)
      if mn:
        print w


fil.close()





















