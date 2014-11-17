
#-*- coding: UTF-8 -*-
import re
from write_to_file import Write


class Kantor:
  
  def extract(self):
    fil = open('foo.xml', 'r')
    for f in fil:
      m = re.search(r'^<a.+(EUR|USD|CHF|GBP)\W+a>$', f, re.M)
      if m: 
        print f
        for w in fil:
          mn = re.search(r'(<td.+currency_table_)([a-z]+)', w, re.M)
          if mn:
            s = mn.group(2)
            print w
            if s == "avg":
              break
    fil.close()

      
address = ["https://internetowykantor.pl/kursy-walut/","http://cinkciarz.pl/kantor/kursy-walut-cinkciarz-pl", 
           "https://liderwalut.pl/kursy-walut" ]
to_file = Write(address)
to_file.to_file()
      
kantor = Kantor()
kantor.extract()























