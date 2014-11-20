#-*- coding: UTF-8 -*-
import re
from write_to_file import Write
import time


class Extract():
  def __init__(self,regxp ):
    #currency_list: EUR, USD, CHF, GBP; values_list: [(Buy, 4,5667),...]
    #self.currency_list = []
    #self.values_list = []
    self.exchange = {}
    #"currency_reg" - regexp to extract currency, "value_reg" - regexp to extract value
    self.regxp = regxp
  def extract(self):
    status = ["buy","sell"]
    fil = open('foo.xml', 'r')
    for f in fil:
      #extract currency symbols
      m = re.search(r"%s" % self.regxp['currency'], f, re.M) 
      if m: 
        i = 0
        #print m.group(2)
        self.exchange[m.group(2)] = {}
        #self.currency_list.append(m.group(2))
        for w in fil:
          #extract currency values
          mn = re.search(r"%s" % self.regxp['value'], w, re.M)
          if mn:
            i += 1
            #print mn.group(2),mn.group(4)
            self.exchange[m.group(2)][status[i-1]] = mn.group(4)
            #self.values_list.append((status[i-1],mn.group(4)))
            if i == 2:
              break
    fil.close()

class Input_output_data():
  def __init__(self):
    self.kantor_data = {}
    
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

class Create_timer():
  def __init__(self,time, time_handler):
    self.time = time
    self.time_handler = time_handler
  def start(self):
    while True:
      self.time_handler() 
      time.sleep(self.time)

    
input_output = Input_output_data()
input_output.input_data()
timer = Create_timer(4,input_output.output_data)
timer.start()

print input_output.kantor_data



