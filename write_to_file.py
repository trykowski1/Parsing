import mechanize
 
address = ["https://internetowykantor.pl/kursy-walut/","http://cinkciarz.pl/kantor/kursy-walut-cinkciarz-pl", 
           "https://liderwalut.pl/kursy-walut" ]

def to_file (name):
  br=mechanize.Browser()
  fo = open("foo.xml", "w")
  for i in name:
    br.open(i)
    the_page = br.response().readlines()
    try:
      fo.write("\n\n\n<!--******************** "+str(i)+" website content ********************-->\n\n\n")
      for j in the_page:
        fo.write(j.lstrip())
    except IOError,e:
      print "Error: can\'t write a file: ",e
    else:
      print"Content of website: \"%s\" written to a file succesfully!" % i  
  fo.close()
  
to_file(address)
