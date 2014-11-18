import re

def extract():
    status = ["buy","sell"]
    fil = open('foo.xml', 'r')
    for f in fil:
      #extract currency symbols
      m = re.search(r'(<td><span.+)(EUR|USD|CHF|GBP)(.+td>)', f, re.M) 
      if m: 
        i = 0
        print m.group(2)
        #self.currency.append(m.group(2))
        for w in fil:
          #extract currency values
          mn = re.search(r'(<td.+cur_\w+\W+)(\d,\d+)(\W+td>)', w, re.M)
          if mn:
            i += 1
            print status[i-1], mn.group(2)
            #self.values.append((mn.group(2),mn.group(4)))
            if i == 2:
              break
    fil.close()
    
extract()

'''
d = '<td><span title="Frank szwajcarski"><a href="/kantor/kursy-walut-cinkciarz-pl/chf">CHFPLN</a></span></td>'

m = re.search(r'^(<td.+)(EUR|USD|CHF|GBP)(.+td>)$', d, re.M) 
if m:
  print m.group(2)
'''