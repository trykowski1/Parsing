#-*- coding: UTF-8 -*-
import re
from write_to_file import Write
import time


class Extract():
  def __init__(self,regxp ):
    self.exchange = {}
    self.regxp = regxp
  def extract(self):
    status = ["buy","sell"]
    fil = open('foo.xml', 'r')
    for f in fil:
      #extract currency symbols
      m = re.search(r"%s" % self.regxp['currency'], f, re.M) 
      if m: 
        i = 0
        self.exchange[m.group(2)] = {}
        for w in fil:
          #extract currency values
          mn = re.search(r"%s" % self.regxp['value'], w, re.M)
          if mn:
            i += 1
            self.exchange[m.group(2)][status[i-1]] = mn.group(4)
            if i == 2:
              break
    fil.close()

class Input_output_data():
    
  def input_data(self):
    address = ["https://internetowykantor.pl/kursy-walut/","http://cinkciarz.pl/kantor/kursy-walut-cinkciarz-pl", 
           "https://liderwalut.pl/kursy-walut" ]  
    kantor_regxp = {'currency':"^(<a.+)(EUR|USD|CHF|GBP)(\W+a>)$", 'value':"(<td.+currency_table_)([a-z]+)(\W+)(\d,\d+)"}    
    cinkciarz_regxp = {'currency':'(<td><span.+)(EUR|USD|CHF|GBP)(.+td>)', 'value':'(<td.+)(cur_)(\w+\W+)(\d,\d+)(\W+td>)'}  
    lider_regxp = {'currency':'(<td>)(EUR|USD|CHF|GBP)(</td>)', 'value':'(<td.+)(bid|ask)(.+)(\d\.\d+)(<\/td>)'}  

    self.to_file = Write(address)
    self.kantor = Extract(kantor_regxp)
    self.cinkciarz = Extract(cinkciarz_regxp)
    self.lider = Extract(lider_regxp)

  def output_data(self):
    self.to_file.to_file()
    self.kantor.extract()
    self.cinkciarz.extract()
    self.lider.extract()
    self.kantor_data = self.kantor.exchange
    self.cinkciarz_data = self.cinkciarz.exchange
    self.lider_data = self.lider.exchange

class Create_timer():
  def __init__(self,time, time_handler):
    self.time = time
    self.time_handler = time_handler
  def start(self):
    while True:
      self.time_handler.output_data() 
      printing = Print(self.time_handler.kantor_data, self.time_handler.cinkciarz_data, self.time_handler.lider_data )
      printing.printing()
      time.sleep(self.time)
      
class Print():
    def __init__(self, *to_print):
        self.to_print = to_print
        
    def printing(self):
        for i in self.to_print:
         print i

'''    
input_output = Input_output_data()
input_output.input_data()
timer = Create_timer(8,input_output)
timer.start()
'''





