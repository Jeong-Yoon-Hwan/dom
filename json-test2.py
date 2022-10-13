
from bs4 import BeautifulSoup as Bs
import json

class data :
  def __init__(self,id,title):
    self.id = id
    self.title = title

  def __call__(self):
    print("data xited:",self.title.__name__)
 


a = data(1,"test")





