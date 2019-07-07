"""
Реализация класса Simple Tree
"""

class SimpleTreeNode:
# Реализация узла дерева

    def __init__(self, val, parent):
        # Инициализация узла дерева 
        self.NodeValue=val
        self.Parent=parent
        self.Children=[]

class SimpleTree:
    #Реализация дерева

    def __init__(self, root):
        #Инициализация класса SimpleTree
        self.Root=root

    def AddChild(self, ParentNode, NewChild):
        #Добавление дочернего узла к предыдущему
        if self.Root is None and ParentNode==None and NewChild!=None:
            self.Root=NewChild
        elif self.Root!=None and ParentNode!=None and NewChild!=None:
            NewChild.Parent=ParentNode
            ParentNode.Children.append(NewChild)
        else:
            pass
  
    def GetAllNodes(self,allNodes=None):
        # ваш код выдачи всех узлов дерева в определённом порядке
        if allNodes is None:
            allNodes=[]
        if self.Root is None:
            return allNodes
        else:
            if not (self.Root in allNodes): 
                allNodes.append(self.Root)
            if self.Root.Children!=None:
                children_massive=self.Root.Children
                for children in children_massive:
                    self.Root=children
                    allNodes.extend(self.GetAllNodes())           
        return_massive=allNodes
        self.Root=return_massive[0]
        allNodes=None 
        return return_massive

    def SearchLinks(self,TreeNode):
        #Метод выдает кол-во вершин в дереве и связь типа родитель-потомки для конкретной вершины
        if TreeNode==None or TreeNode.NodeValue==None:
            return None
        else:
            Q_ty=1
            parent=[]
            children=[]
            parent.append(TreeNode)
            while len(parent)!=0:
                for everynode in range(0,len(parent)):
                    if len(parent[everynode].Children)!=None:
                        for everyChildren in range(0,len(parent[everynode].Children)):
                            if parent[everynode].Children[everyChildren].NodeValue!=None:
                                children.append(parent[everynode].Children[everyChildren])
                Q_ty=Q_ty+len(children)
                parent.clear()
                for i in range(0,len(children)):
                    parent.append(children[i])
                children.clear()
        return Q_ty
    
    def Q_tyStructure(self):
        #Расчет кол-ва элементов при удалении элементов
        All_Vertex=self.GetAllNodes() 
        Q_ty_matrix=[]
        for everyvertex in range(0,len(All_Vertex)):
            Q_ty_for_vertex=self.SearchLinks(All_Vertex[everyvertex])
            Q_ty_matrix.append(Q_ty_for_vertex)
        Out=[[None]*2 for i in range(0,len(All_Vertex))] 
        for everynode in range(0,len(All_Vertex)):
                Out[everynode][0]=All_Vertex[everynode]
                Out[everynode][1]=Q_ty_matrix[everynode]
        return Out

    def EvenTrees(self):
        allNodes=self.GetAllNodes()
        if len(allNodes)%2!=0 or len(allNodes)<=2:
            return None
        else:
            edges=[]
            for everynode in range(0,len(allNodes)):
                q_ty_for_parent=self.SearchLinks(allNodes[everynode])
                if len(allNodes[everynode].Children)!=0:
                    for everychildren in range(0,len(allNodes[everynode].Children)):
                        q_ty_for_children=self.SearchLinks(allNodes[everynode].Children[everychildren])
                        if q_ty_for_children>1:
                            if (q_ty_for_parent-q_ty_for_children)%2==0:
                                edges.append(allNodes[everynode].NodeValue)
                                edges.append(allNodes[everynode].Children[everychildren].NodeValue)
                            else:
                                pass
                        else:
                            pass
                else:
                    pass
        return edges

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        if val!=None and self.GetAllNodes()!=None:
            output=[]
            Nodes_in_Tree=self.GetAllNodes()
            for everynode in range(self.Count()):
                if Nodes_in_Tree[everynode].NodeValue==val:
                    output.append(Nodes_in_Tree[everynode])
            return output
        else: 
            return None 

    def Count(self):
        # количество всех узлов в дереве
        nodes_qty=self.GetAllNodes()
        return len(nodes_qty)

    def Print_all_Nodes(self):
        # печать значений элементов
        all_Nodes=self.GetAllNodes()
        all_Nodes_for_print=[]
        for i in range(self.Count()):
            all_Nodes_for_print.append(all_Nodes[i].NodeValue)
        print(all_Nodes_for_print)
        
    def DeleteNode(self, NodeToDelete):
        # ваш код удаления существующего узла NodeToDelete
        if NodeToDelete!=None and NodeToDelete!=self.Root:
            Nodes_in_Tree=self.GetAllNodes()
            if NodeToDelete in Nodes_in_Tree:
                Parent_Node=NodeToDelete.Parent
                Parent_Node_Children=Parent_Node.Children
                i=0
                q_ty=len(Parent_Node_Children)
                while i<q_ty:
                    if Parent_Node_Children[i]==NodeToDelete:
                        Parent_Node_Children.remove(NodeToDelete)
                        break
                    i+=1
                Parent_Node.Children=Parent_Node_Children
                Children=NodeToDelete.Children
                for everynode in Children:
                    everynode.Parent=Parent_Node
                    Parent_Node.Children.append(everynode)
                NodeToDelete.Parent=None
                NodeToDelete.Children=None
                NodeToDelete.NodeValue=None
        elif NodeToDelete==self.Root or NodeToDelete==None:
            pass


    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом -- 
        # в качестве дочернего для узла NewParent
        all_Nodes_for_move=self.GetAllNodes()
        if NewParent and OriginalNode in all_Nodes_for_move:
            if NewParent==OriginalNode.Parent:
                pass
            elif NewParent!=OriginalNode.Parent:
                old_Parent=OriginalNode.Parent
                old_Parent.Children.remove(OriginalNode)
                OriginalNode.Parent=NewParent
                NewParent.Children.append(OriginalNode)
        elif OriginalNode in all_Nodes_for_move and NewParent==None:
            pass
        else:
            pass

    def LeafCount(self):
        # количество листьев в дереве
        all_Nodes=self.GetAllNodes()
        all_leaf=[]
        for everynode in all_Nodes:
            if everynode.Children==[]:
                all_leaf.append(everynode)
            else:
                pass
        return len(all_leaf)
    
"""

A1=SimpleTreeNode(1,None)
A2=SimpleTreeNode(2,None)
A3=SimpleTreeNode(3,None)
A4=SimpleTreeNode(4,None)
A5=SimpleTreeNode(5,None)
A6=SimpleTreeNode(6,None)
A7=SimpleTreeNode(7,None)
A8=SimpleTreeNode(8,None)
A9=SimpleTreeNode(9,None)
A10=SimpleTreeNode(10,None)
A11=SimpleTreeNode(11,None)
A12=SimpleTreeNode(12,None)
Tree=SimpleTree(A1)
Tree.AddChild(A1,A2)

Tree.AddChild(A1,A3)
Tree.AddChild(A1,A4)
Tree.AddChild(A2,A5)
Tree.AddChild(A3,A6)
Tree.AddChild(A4,A7)
Tree.AddChild(A6,A8)
Tree.AddChild(A6,A9)
Tree.AddChild(A7,A10)
Tree.AddChild(A8,A11)
Tree.AddChild(A10,A12)

print(Tree.GetAllNodes())
print(Tree.Count())
Tree.Print_all_Nodes()
print(Tree.EvenTrees())
"""




