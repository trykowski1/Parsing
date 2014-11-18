#-*- coding: UTF-8 -*-
import re
from write_to_file import Write


class Kantor:
  def __init__(self):
    #currency: EUR, USD, CHF, GBP; values: [(Buy, 4,5667),...]
    self.currency = []
    self.values = []
  def extract(self):
    fil = open('foo.xml', 'r')
    for f in fil:
      #extract currency symbols
      m = re.search(r'^(<a.+)(EUR|USD|CHF|GBP)(\W+a>)$', f, re.M) 
      if m: 
        print m.group(2)
        self.currency.append(m.group(2))
        for w in fil:
          #extract currency values
          mn = re.search(r'(<td.+currency_table_)([a-z]+)(\W+)(\d,\d+)', w, re.M)
          if mn:
            print mn.group(2),mn.group(4)
            self.values.append((mn.group(2),mn.group(4)))
            if mn.group(2) == "sell":
              break
    fil.close()
    
class Cinkciarz:
  def __init__(self):
    #currency: EUR, USD, CHF, GBP; values: [(Buy, 4,5667),...]
    self.currency = []
    self.values = []
  def extract(self):
    status = ["buy","sell"]
    fil = open('foo.xml', 'r')
    for f in fil:
      #extract currency symbols
      m = re.search(r'(<td><span.+)(EUR|USD|CHF|GBP)(.+td>)', f, re.M) 
      if m: 
        i = 0
        print m.group(2)
        self.currency.append(m.group(2))
        for w in fil:
          #extract currency values
          mn = re.search(r'(<td.+cur_\w+\W+)(\d,\d+)(\W+td>)', w, re.M)
          if mn:
            i += 1
            print status[i-1], mn.group(2)
            self.values.append((status[i-1], mn.group(2)))
            if i == 2:
              break
    fil.close()
    
    

      
address = ["https://internetowykantor.pl/kursy-walut/","http://cinkciarz.pl/kantor/kursy-walut-cinkciarz-pl", 
           "https://liderwalut.pl/kursy-walut" ]

#to_file = Write(address)
#to_file.to_file()
      
kantor = Kantor()
kantor.extract()
cinkciarz = Cinkciarz()
cinkciarz.extract()

print kantor.currency
print kantor.values

print cinkciarz.currency
print cinkciarz.values


