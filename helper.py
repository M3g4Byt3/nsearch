import dbmodule
from dbmodule import *

class Helper:

  def __init__(self,args="",commnad=""):
    self.args = args
    self.commnad = commnad

  #process the commnads
  def process(self):
    if self.commnad == "search":
      if not self.args:
        dbmodule.lastresults = dbmodule.searchAll()
        for row in dbmodule.lastresults.items():
          print('\033[1;32m'+str(row[0])+"."+row[1]+'\033[0m')
      else:
        dbmodule.lastresults = dbmodule.searchByCriterial(**self.__searchparams())
        self.printlastResult()
    elif self.commnad == "addfav":
      dbmodule.createFavorite(**self.__addfavparams())
    elif self.commnad == "delfav":
      dbmodule.deleteFavorite(**self.__delfavparams())
    elif self.commnad == "showfav":
      dbmodule.lastresults = dbmodule.getFavorites(**self.__showfavparams())
      self.printlastResult()
    else:
      print "Error"

  # Display the last results
  def printlastResult(self):
    for k,v in dbmodule.lastresults.items():
      print('\033[1;32m'+str(k)+"."+v+'\033[0m')

  # Display the documentation per script
  def displayDoc(self):
    scriptFile = open(dbmodule.scriptsPath+self.args,'r')
    lines = scriptFile.read().splitlines()
    for line in lines:
      if line.startswith("license"):
        break
      print('\033[1;96m'+line+'\033[0m')
    scriptFile.close()

  # used for the autocomplete
  def resultitems(self):
    i = 0
    items = []
    for k,v in dbmodule.lastresults.items():
      items.insert(i,v)
      i = i + 1
    return items

  # private function to set params for search command
  def __searchparams(self):
    argsdic = {}
    if self.args.find('name:') != -1 or self.args.find('category:') != -1 or self.args.find('author:') != -1:
      if len(self.args.split(":")) >= 4:
        argsdic.update({
          self.args.split(":")[0]:self.args.split(":")[1].split(" ")[0],
          self.args.split(":")[1].split(" ")[1]:self.args.split(":")[2].split(" ")[0],
          self.args.split(":")[2].split(" ")[1]:self.args.split(":")[3].split(" ")[0]})
      elif len(self.args.split(":")) == 3:
        argsdic.update({
          self.args.split(":")[0]:self.args.split(":")[1].split(" ")[0],
          self.args.split(":")[1].split(" ")[1]:self.args.split(":")[2].split(" ")[0]})
      elif len(self.args.split(":")) == 2:
        argsdic.update({self.args.split(":")[0]:self.args.split(":")[1].split(" ")[0]})
      else:
        print "Plase enter a correct commands"
    return argsdic

  #private funtion to set params for addfav command
  def __addfavparams(self):
    argsdic ={}
    if self.args.find('name:') != -1 or self.args.find('ranking:') != -1:
      if len(self.args.split(":")) == 3:
        argsdic.update({
          self.args.split(":")[0]:self.args.split(":")[1].split(" ")[0],
          self.args.split(":")[1].split(" ")[1]:self.args.split(":")[2].split(" ")[0]})
      elif len(self.args.split(":")) == 2:
        argsdic.update({self.args.split(":")[0]:self.args.split(":")[1].split(" ")[0]})
      else:
        print "Plase enter a correct commands"
    return argsdic

  #private funtion to set params for delfav command
  def __delfavparams(self):
    argsdic ={}
    if self.args.find('name:') != -1:
      if len(self.args.split(":")) == 2:
        argsdic.update({self.args.split(":")[0]:self.args.split(":")[1].split(" ")[0]})
      else:
        print "Plase enter a correct commands"
    return argsdic

  #private function to set params for modfav command
  def __modfavparams(self):
    return None

  #private function to set paramas for showfav command
  def __showfavparams(self):
    argsdic ={}
    if self.args.find('name:') != -1 or self.args.find('ranking:') != -1:
      if len(self.args.split(":")) == 3:
        argsdic.update({
          self.args.split(":")[0]:self.args.split(":")[1].split(" ")[0],
          self.args.split(":")[1].split(" ")[1]:self.args.split(":")[2].split(" ")[0]})
      elif len(self.args.split(":")) == 2:
        argsdic.update({self.args.split(":")[0]:self.args.split(":")[1].split(" ")[0]})
      else:
        print "Plase enter a correct commands"
    return argsdic
