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
        return self.stack.pop(-1)
    
    def push(self,data):
        if len(self.stack)>0:
            return self.stack.insert(0,data)
        else:
            return self.stack.append(data)

    def peek(self):
        if len(self.stack) <= 0:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

        
    def Limit(self,vertexstart,vertexend):
        #Проверка кол-ва элементов в графе
        if len(self.vertex)>=2:
            start=None
            finish=None
            out=[]
            for everyvertex in range(0,len(self.vertex)):
                print(vertexstart,vertexend,self.vertex[everyvertex])
                if self.vertex[everyvertex]==vertexstart:
                    start=everyvertex
                if self.vertex[everyvertex]==vertexend:
                    finish=everyvertex
                if start!=None and finish!=None:
                    break
            if start!=None and finish!=None:
                out.append(start)
                out.append(finish)
                return out
            else:
                return -1
        else:
            return -1

    def Q_ty_of_links(self,start_number):
        #Находим кол-во связей для каждой вершины start
        q_ty=0
        for every_link in range(0,len(self.vertex)):
            if self.m_adjacency[start_number,every_link]==1:
                q_ty+=1
        return q_ty




    def DepthFirstSearch(self,vertexstart,vertexend):
        #Поиск пути в глубину
        res=self.Limit(vertexstart,vertexend)
        if res==-1:
            return None
        start_number=res[0]   # номер стартовой вершины в массиве 
        finish_number=res[1]  # номер финишной вершины в массиве
        start=vertexstart 
        stack_for_path=Stack() 
        vertexstart.hit=True       
        stack_for_path.push(vertexstart)
        q_ty_of_links=0 # переменная для кол-ва связей вершины
        q_ty_of_true_hit=[[0]*self.max_vertex] # кол-во  связанных вершин которое обошли для каждой вершины "старт"
        while len(stack_for_path.stack)!=0:     #Внешний цикл обхода
            q_ty_of_links=self.Q_ty_of_links(start_number) # Ищем кол-во связей для вершины start_number
             
            for every_vertex in range(0,len(self.vertex)): #Смотрим на каждую вершину в матрице смежнести 
                if self.m_adjacency[start_number][every_vertex]==1: # Если есть связь проваливаемся глубже
                    if self.vertex[every_vertex].hit==False: # Если не посетили то надо посетить
                        self.vertex[every_vertex].hit=True 
                        q_ty_of_true_hit[start]+=1 
                        stack_for_path.push(self.vertex[every_vertex]) #Проталктваем ее в стек
                        start=stack_for_path.peek() #Делаем ее start для следующих итераций
                    else: 
                        pass
                    if stack_for_path.peek()==vertexend: #Если конечная вершина равна крайнему элементу то заканчиваем поиск
                        return stack_for_path.stack
                    if q_ty_of_links==q_ty_of_true_hit[start]: # Если у вершины Start число связей равно кол-ву вершин с True то удаляем ее из стека
                        if len(stack_for_path.stack)>0:
                            stack_for_path.stack.pop()
                        else:
                            pass 
                else:  # Если связи нет то проходим далее 
                    pass
        return None
                  
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


        

m=SimpleGraph(6)
vertex_0=m.AddVertex(1)
vertex_1=m.AddVertex(2)
vertex_2=m.AddVertex(3)
vertex_3=m.AddVertex(4)
vertex_4=m.AddVertex(5)
vertex_5=m.AddVertex(6)
print(m.vertex)
m.AddEdge(0,2)
m.AddEdge(2,3)
m.AddEdge(3,4)
m.AddEdge(4,5)
print(m.m_adjacency)
print(m.DepthFirstSearch(m.vertex[0],m.vertex[5]))

