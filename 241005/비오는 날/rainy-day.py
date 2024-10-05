class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
N = int(input())
datas = []
for i in range(N):
    a, b, c = input().split()
    datas.append(Data(a,b,c))
sorted_data = sorted(datas,key= lambda data: data.date) 
for j in datas:
    if j.weather == 'Rain':
        print(f'{j.date} {j.day} {j.weather}')
        break;