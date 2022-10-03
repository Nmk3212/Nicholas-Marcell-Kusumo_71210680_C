class Node_Tabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def insert_head(self,no_rekening, nama, saldo):
        baru = Node_Tabungan(no_rekening, nama, saldo)
        if self.isEmpty()==True:
            self._head = baru
            self._tail = baru
            self._tail.next = None
        else:
            baru.next = self._head
            self._head = baru
        self._size += 1

    def deleteFirst(self):
        if self.isEmpty()==False:
            d = ""
            if self._head.next==None:
                d = self._head.no_rekening
                self._head=None
                self._tail=None
            else:
                hapus = self._head
                d = hapus.no_rekening
                self._head = self._head.next
                hapus.next=None
                del hapus
            self._size -= 1

    def deleteLast(self):
        if self.isEmpty() == False:
            d = None
            bantu = self._head
            if(self._head != self._tail):
                while bantu.next != self._tail:
                    bantu = bantu.next
                hapus = self._tail
                self._tail = bantu
                d = hapus.saldo
                del hapus
                self._tail.next = None
            else:
                d = self._tail.saldo
                self._head=tail=None
            self._size -= 1
                
            

    def print(self):
        if self.isEmpty()==False:
            bantu = self._head
        while(bantu!=None):
            print("Norek:", bantu.no_rekening ," ")
            print("Nama:", bantu.nama ," ")
            print("Saldo:", bantu.saldo ," ")
            bantu = bantu.next
            print()
        else:
            print("Kosong")

slnc = SLNC()
slnc.insert_head(201,"Hanif", 250000)
slnc.insert_head(110,"Yudha", 150000)
slnc.print()
slnc.filter(100)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()