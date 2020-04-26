import json

class Scores:
    global __data
    def __init__(self,):
        foo = open('data.json',)
        self.data = json.load(foo)

    def add(self, key, points):
        self.data['gamers'][key] += int(points)
        self.data['gamers']=self.sort()
        self.update()

    def sub(self, key, points):
        self.data['gamers'][key] -= int(points)
        self.data['gamers'] = self.sort()
        self.update()
    
    def add_gamer(self, name):
        self.data['gamers'].update({name:0})
        with open('data.json','w') as outfile:
            json.dump(self.data,outfile)
    
    def sub_gamer(self, name):
        del self.data['gamers'][name]
        self.update()

    def names(self,index):
        i=index
        for x in self.data['gamers']:
            i-=1
            if i==0:return x

    def points(self,index):
        i=index
        for x in self.data['gamers']:
            i-=1
            if i==0:return self.data['gamers'][x]

    def sort(self):
        a = sorted(self.data['gamers'],key=self.data['gamers'].get)
        end={}
        i=len(a)-1
        for key in self.data['gamers']:
            end.update({a[i]:self.data['gamers'][a[i]]})
            i-=1
        return end
    
    def update(self):
        with open('data.json','w') as outfile:
            json.dump(self.data,outfile)

    def dict(self):
        return self.data['gamers']

    def length(self,):
        return len(self.data['gamers'])

if not isinstance(2700,int):
    print('yheeboi')
else:
    print('nahboi')