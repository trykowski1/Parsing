#-*- coding: UTF-8 -*-
import re
from write_to_file import Write


class Kantor:
  def __init__(self):
    self.price = {}
  def extract(self):
    fil = open('foo.xml', 'r')
    for f in fil:
      m = re.search(r'^(<a.+)(EUR|USD|CHF|GBP)(\W+a>)$', f, re.M)
      if m: 
        print m.group(2)
        for w in fil:
          mn = re.search(r'(<td.+currency_table_)([a-z]+)(\W+)(\d,\d+)', w, re.M)
          if mn:
            print mn.group(2),mn.group(4)
            if mn.group(2) == "avg":
              break
    fil.close()

      
address = ["https://internetowykantor.pl/kursy-walut/","http://cinkciarz.pl/kantor/kursy-walut-cinkciarz-pl", 
           "https://liderwalut.pl/kursy-walut" ]

to_file = Write(address)
to_file.to_file()
      
kantor = Kantor()
kantor.extract()
kantorek = {"EUR":{"Buy":4.2103,"Sell:":4.2403}}
