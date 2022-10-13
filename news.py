import json
from textwrap import indent


class NewsData :
  def __init__(self,id,title,contents,images):
    self.id = id
    self.title = title
    self.contents = contents
    self.images = images
  def toString(self):
	  return f'id:{self.id},title:{self.title},contents:{self.contents},images:{self.images}'


a = NewsData(1,'제목1','내용1','이미지1')
print(a.toString())

s = json.dumps(a, default=lambda o:o.__dict__, ensure_ascii= False)
print(s)
#json 저장
file_path = './sample.json'

with open(file_path,"w",encoding='UTF-8-sig') as outfile:
  json.dump(a.toString(),outfile,ensure_ascii=False,indent=4)









