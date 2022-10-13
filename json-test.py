from calendar import c
import json

from attr import field

customer = {
  "id" : 1,
  "name" : "정윤환",
  "history" : [
    {"data" : '2022-10-10', 'item': 'iPhone'},
    {"data" : '2022-11-10', 'item': 'Monitor'}
  ]
}

#JSON 인코딩
jsonString = json.dumps(customer)

# 문자열 출력
print(jsonString)
print(type(jsonString))


class MyName :
  def __init__(self,name,age,address):
    self.name = name
    self.age = age
    self.address = address

yoonhwan = MyName("yoonhwan",28,"대전")

print(yoonhwan.age,yoonhwan.name,yoonhwan.address)


a = [{'name':'jung','age':'28'}]

file_path = "./sample.json"
with open(file_path,"w") as outfile:
  json.dump(a, outfile, indent=4)  #indent : 탭 간격


i=1
for i in range(10):
  a.append({"name":yoonhwan.name,"age":yoonhwan.age})

with open(file_path,"w") as outfile:
  json.dump(a, outfile, indent=4 )
