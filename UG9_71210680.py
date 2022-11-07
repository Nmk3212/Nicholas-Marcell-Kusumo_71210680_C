class PriorityQueueSortedList:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def peek(self):
        if self.is_empty() is not True:
            x = 9999
            data = ''
            for i in range(len(self._data)):
                if self._data[i][1] > x:
                    pass
                else:
                    x = self._data[i][1]
                    data = self._data[i][0]
            print("Data prioritas tertinggi: ('"+data+"',",x,")")
        else:
            print('Priority Queue Kosong')

    def add(self, data, priority):
        self._data.append((data, priority))
        self._data=sorted(self._data, key=lambda x:x[1])  

    def update(self,prioBaru,dataBaru):
        if self.is_empty() is True:
            print("Priority Queue Kosong!")
        else:
            ind = []
            for i in range(len(self._data)):
                if self._data[i][1] == prioBaru:
                    self._data[i] = (dataBaru, prioBaru)
        
    def remove(self):
        if self.is_empty() is not True:
            x = 9999
            index = 0
            n = 0
            for i in range(len(self._data)):
                if self._data[i][1] > x:
                    pass
                else:
                    x = self._data[i][1]
                    index = i
                    n += 1
            del self._data[index]
        else:
            print("Priority Queue Kosong!") 

    def removeWithPrio(self,prio):
        if self.is_empty() is True:
            print("Priority Queue Kosong!")
        else:
            ind = []
            for i in range(len(self._data)):
                if self._data[i][1] == prio:
                    ind.append(self._data[i])
            for i in ind:
                self._data.remove(i)

    def printIsiQueue(self):
        print("Isi Semua Queue: ",end='')
        for i in range(len(self._data)):
            print(self._data[i], end=' ')

sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removeWithPrio(4)
sortedList.peek()
sortedList.printIsiQueue()
