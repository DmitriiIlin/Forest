class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit=None

class Stack:

    def __init__(self):
        self.stack=[]
    
    def pop(self):
        if len(self.stack)==0:
            return None
        return self.stack.pop(0)
    
    def push(self,data):
        if len(self.stack)>0:
            return self.stack.insert(0,data)
        else:
            return self.stack.append(data)

    def peek(self):
        if len(self.stack) <= 0:
            return None
        else:
            return self.stack[0]

    def size(self):
        return len(self.stack)

class Node:

    def __init__(self, v):
        #Инициализация класса Node
        self.value = v
        self.next = None

class Queue:

    def __init__(self):
        #Инициализация класса Queue
        self.head = None
        self.tail = None 

    def enqueue(self, item):
        # Добывление элемента в конец очереди 
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def dequeue(self):
        # Выдача элемента из головы списка
        if self.head==0:
            return None
        else: 
            node=self.head
            self.head=node.next
            return node

    def size(self):
        # Метод определяет размер очереди
        node=self.head
        l=0
        while node is not None:
            l+=1
            node=node.next
        return l 
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def Init_For_Hit(self):
        #Инициализация свойства hit всех узлов
        for everyvertex in range(0,len(self.vertex)):
            self.vertex[everyvertex].hit=False
        
    def Limit(self,VFrom,VTo):
        #Проверка кол-ва элементов в графе
        if len(self.vertex)>=2:     
            if VFrom!=None and VTo!=None:
                if (VFrom>=0 and VFrom<len(self.vertex)) and (VTo>=0 and VTo<len(self.vertex)): 
                    if self.vertex[VFrom]!=None and self.vertex[VTo]!=None:                   
                        return 1
                    else:
                        return -1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    
    def Vertex_Index(self,vertex):
        #Ищем индекс вершины в массиве vertex
        if vertex!=None:
            for everyvertex in range(0,len(self.vertex)):
                if vertex==self.vertex[everyvertex]:
                    out=everyvertex
                    break
                else:
                    pass
            return out
    
    def Stack_Inverse(self,input_massive):
        #Инверсия входных данных
        size=len(input_massive)
        output_massive=[]
        while size>0:
            output_massive.append(input_massive[size-1])
            size-=1
        return output_massive


    def DepthFirstSearch(self,VFrom,Vto):
        #Поиск пути в глубину, VFrom и VTo номера вершин
        self.Init_For_Hit() #Инициализация значений hit=False
        stack_for_path=Stack()
        res=self.Limit(VFrom,Vto)
        if res==-1:
            return stack_for_path.stack
        if VFrom==Vto:
            return stack_for_path.stack
        new_Peek_Number=None
        self.vertex[VFrom].hit=True       
        stack_for_path.push(self.vertex[VFrom])
        while len(stack_for_path.stack)!=0:
            current_Peek=stack_for_path.peek() #Считываем вершину стека
            current_Peek_Number=self.Vertex_Index(current_Peek) #Находим номер вершины в массиве Vertex
            links=[] # Список для связей текущей вершины
            for every_vertex in range(0,len(self.vertex)): #Цикл поиска связей  
                if self.m_adjacency[current_Peek_Number][every_vertex]==1: # Если связь есть 
                    links.append(self.vertex[every_vertex]) # Добавляем ее в список связей
            for vertex_in_links in range(0,len(links)): # Смотрим каждую связь 
                vertex_in_links_number=self.Vertex_Index(links[vertex_in_links]) # Определяем номер вершины у которой есть связь с текущей вершиной
                if vertex_in_links_number==Vto: # Если определенный номер вершины равен искомому то: 
                    stack_for_path.push(self.vertex[vertex_in_links_number]) # Проталкиваем искомую вершину в стек
                    return self.Stack_Inverse(stack_for_path.stack) # Возвращаем результат- стек в обратном порядке
            for every_vertex_in_links in range(0,len(links)): # Смотрим каждую связь на предмет hit==False
                if links[every_vertex_in_links].hit==False: #Если нашли вершину с hit==False
                    new_Peek_Number=self.Vertex_Index(links[every_vertex_in_links]) # Ищем индекс вершины в массиве Vertex
                    self.vertex[new_Peek_Number].hit=True # Мы посетили вершину, следовательно hit=True
                    stack_for_path.push(self.vertex[new_Peek_Number]) # Проталкваем ее в стек
                    break # Выходим из цикла поиска hit==False
            if new_Peek_Number==None: # Если не нашли вершину то:
                if len(stack_for_path.stack)>0: # Если в стеке что-то есть 
                    stack_for_path.pop() # Удаляем верхний элемент стека
                else: # иначе, если стек пуст
                    return stack_for_path.stack # возвращаем пустой стек, пути нет
            new_Peek_Number=None
            links=[]
        else:
            return stack_for_path.stack
            
    def FirstPath(self,VFrom,VTo):
        #Метод формирует массив в котором содержуться VFrom и VTo, а так же вершины которые были посещены
        self.Init_For_Hit() #Инициализация значений hit=False
        res=self.Limit(VFrom,VTo)
        if res==-1:
            return []
        if VFrom==VTo:
            return []
        current_Peek_Number=VFrom # Текущий номер вершины
        current_Peek=self.vertex[VFrom]
        queue=Queue()
        Peek_Number=0
        out=[]
        self.vertex[current_Peek_Number].hit=True #Начинаем с начальной вершины
        node=Node(self.vertex[current_Peek_Number]) #Создаем элемент node на базе self.vertex[current_Peek_Number]
        queue.enqueue(node) #Проталкиваем начальную вершину в очередь
        out.append(self.vertex[current_Peek_Number]) #Проталкиваем начальную вершину в выходной массив
        while queue.size()!=0: #Рабочий цикл
            if Peek_Number==None: # Если у вершины нет непосещенной связи то 
                if queue.size()>0: # и если в очереди есть элемент 
                    current_Peek=queue.dequeue().value # Удаляем первый элемент очереди и пресваиваем его переменной current_Peek
                    #print(queue.size())
                    current_Peek_Number=self.Vertex_Index(current_Peek) # Находим номер новой вершины
                else:
                    return [] # Очередь пуста , возвращаем пустой список
            else:
                pass 
            Peek_Number=None #Флаг для искомой вершины , равен номеру найденой вершины, в противном случае None
            for everylink in range(0,len(self.vertex)): #Смотрим каждую связь у вершины с номером current_Peek_Number
                if self.m_adjacency[current_Peek_Number][everylink]==1: # Если связь есть
                    if self.vertex[everylink].hit==False: #Если вершина не посещена
                        self.vertex[everylink].hit=True # Посетили
                        node=Node(self.vertex[everylink]) #Создали тип node 
                        queue.enqueue(node) # Протолкнули в очередь
                        out.append(self.vertex[everylink]) #Проталкиваем вершину в выходной список
                        Peek_Number=everylink # Присвоили флагу номер вершины
                        if everylink==VTo: # Если найденная вершина равна искомой 
                            return out # то возвращаем очередь
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            #print(queue.size(),"без удаления")
            
        else:
            return []

    def SecondPath(self,input,VFrom,VTo):
        #Метод отфильтровывает путь от VFrom до VTo в массиве input
        input_size=len(input) #Размер входного массива 
        if input_size==0: #Если равен 0, то пути нет, возвращаем пустой список
            return [] 
        else:
            pass
        startvertex=VTo # Начинаем поиск от конечной вершины
        finishvertex=VFrom # Вершина-цель, теперь это начальная вершина
        out=[] # Выходной массив
        out.append(self.vertex[VTo]) # Добавить стартовую вершину в массив
        while input_size!=0: # Внешний цикл обхода
            for everyvertex in range(0,len(self.vertex)): # Рабочий цикл
                if self.m_adjacency[startvertex][everyvertex]==1: # Если есть связь между вершинами и :
                    if self.vertex[everyvertex].hit==True and self.vertex[everyvertex] not in out: # Если мы посетили вершину и не занесли ее в выходной массив
                        out.append(self.vertex[everyvertex]) # Добавить в выходной массив
                        startvertex=everyvertex # Сделать стартовой вершиной новую
                        break # Выйти из цикла
                    else:
                        pass
                else:
                    pass
            if startvertex==finishvertex: # Если стартовая вершина равна финишной вершине, то заканчиваем работу
                break # Заванчиваем работу
            else:
                pass
        return self.Stack_Inverse(out) # Итоговый результат

    def BreadthFirstSearch(self,VFrom, VTo):
        #Метод поиска пути в ширину
        first_res=self.FirstPath(VFrom,VTo)
        second_res=self.SecondPath(first_res,VFrom,VTo)
        return second_res
        
    def AddVertex(self, v):
        # ваш код добавления новой вершины 
        # с значением value 
        # в свободное место массива vertex
        for every_vertex in range(0,len(self.vertex)):
            if self.vertex[every_vertex]==None:
                new_vertex=Vertex(v)
                self.vertex[every_vertex]=new_vertex
                break
        else:
            pass
        return every_vertex
	
    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        if self.vertex[v]==None or v>len(self.vertex)-1:
            pass
        else:
            for evere_edge in range(0,len(self.vertex)):
                self.m_adjacency[v][evere_edge]=0
                self.m_adjacency[evere_edge][v]=0
            self.vertex[v]=None
	
    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if self.vertex[v1]==None or self.vertex[v2]==None or v1>len(self.vertex)-1 or v2>len(self.vertex)-1:
            pass
        else:     
            if self.m_adjacency[v1][v2]==1 and self.m_adjacency[v2][v1]==1:
                return True
            else:
                return False
    

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if self.vertex[v1]==None or self.vertex[v2]==None or v1>len(self.vertex)-1 or v2>len(self.vertex)-1:
            pass
        else:   
            self.m_adjacency[v1][v2],self.m_adjacency[v2][v1]=1,1

	
    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        Edge=self.IsEdge(v1,v2)
        if Edge!=True:
            pass
        else:
            self.m_adjacency[v1][v2],self.m_adjacency[v2][v1]=0,0


       
"""
m=SimpleGraph(8)
vertex_0=m.AddVertex("Элемент 0")
vertex_1=m.AddVertex("Элемент 1")
vertex_2=m.AddVertex("Элемент 2")

vertex_3=m.AddVertex("Элемент 3")
vertex_4=m.AddVertex("Элемент 4")
vertex_5=m.AddVertex("Элемент 5")
vertex_6=m.AddVertex("Элемент 6")
vertex_7=m.AddVertex("Элемент 7")

m.AddEdge(0,1)

m.AddEdge(0,2)
m.AddEdge(0,3)
m.AddEdge(3,4)
#m.AddEdge(4,7)
m.AddEdge(4,5)
m.AddEdge(2,5)
m.AddEdge(5,6)
#m.AddEdge(6,7)
print(m.m_adjacency)

K=m.DepthFirstSearch(0,7)
print(K)
for i in range(0,len(K)):
    print(K[i].Value)
print("---------------")
Z=m.BreadthFirstSearch(0,7)
print(Z)
for i in range(0,len(Z)):
    print(Z[i].Value)
"""
