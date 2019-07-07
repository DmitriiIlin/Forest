class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 0
        for i in range(0,depth+1):
            tree_size=tree_size+2**i
        self.Tree = [None] * tree_size # массив ключей
	
    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        if key!=None and self.Tree[0]!=None:
            i=0
            while i<=len(self.Tree):
                node=self.Tree[i]
                if key>node:
                    i=2*i+2
                elif key<node:
                    i=2*i+1
                else:
                    return i
                if i>len(self.Tree):
                    return None                    
        else:
            return None # не найден
	
    def AddKey(self, key):
        # добавляем ключ в массив
        i=0
        if self.Tree[i]==None:
            self.Tree[i]=key
            return i
        while i<=len(self.Tree):
            if key < self.Tree[i]:
                i=i*2+1
                if i>len(self.Tree):
                    return -1
            elif key>self.Tree[i]:
                i=i*2+2
                if i>len(self.Tree):
                    return -1
            else:
                return -1
            if self.Tree[i]==None:
                self.Tree[i]=key
                return i
            elif self.Tree[i]!=None:
                pass 
        return -1
        # индекс добавленного/существующего ключа или -1 если не удалось
"""
A=aBST(2)
print(A.AddKey(24))
print(A.AddKey(25))
print(A.AddKey(26))
print(A.AddKey(27))
print(A.AddKey(26))
print(A.Tree)
print(A.FindKeyIndex(245))
print(A.AddKey(226))
"""