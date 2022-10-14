import json

class Test:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
a = [1,2,3,4,5]
b = ["jung","song","kim","lee","pack"]


data = []
data.append(b)


#work = Test(1,b[1])

i = 0     #i값 초기화
newData = []   #newData 배열 초기화
while i < 5:   
  newData.append(Test(i,b[i]).__dict__) #반복될동안 newData 배열에 인스턴스 삽입
  i = i+1

print(newData)  # newData 배열 출력


file_path = "./sample.json"
with open(file_path,"w") as outfile:
  json.dump(newData,outfile)


