import mechanize
 

class Write():
  def __init__(self, address):
      self.address = address
      
  def to_file (self):
    br=mechanize.Browser()
    fo = open("foo.xml", "w")
    for i in self.address:
      try:
        br.open(i)
        the_page = br.response().readlines()
        try:
          fo.write("\n\n\n<!--******************** "+str(i)+" website content ********************-->\n\n\n")
          for j in the_page:
            fo.write(j.lstrip())
        except IOError,e:
          print "Error: can\'t write to a file: ",e
        #else:
          #print"Content of website: \"%s\" written to a file succesfully!" % i  
      except:
        print "Error: cannot read a website content: %s" % i
    fo.close()
  
