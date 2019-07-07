class Node_2():
    # Инициализация э-та двунаправленного списка
    def __init__(self,v):
        self.value=v
        self.prev=None
        self.next=None

class Linked_List_2:
    # Инициализация двунаправленного списка
    def __init__(self):
        self.tail=None
        self.head=None

    def add_in_tail(self,item):
        # Метод добавления э-та в конец двунаправленного списка
        if self.head is None:
            self.head=item
            item.prev=None
            item.next=None
        else:
            self.tail.next=item
            item.prev=self.tail
        self.tail=item

    def print_all_nodes(self):
        # Метод класса L_L_2, позволяющий вывести э-ты L_L_2 
        node=self.head
        while node!=None:
            print(node.value,'вывод print all nodes')
            node=node.next

    def delete_node(self,val,parametr=1):
        # Метод удаляет узел из списка по значению узла
        node = self.head
        while node is not None:
            print('Work')
            if (node.value==self.head.value) and (node.value==val):
                new_head=node.next
                node.prev=None
                self.head=new_head
                parametr=1
                print('1 part')
                if parametr==1:
                    break
            elif (node.value==self.tail.value) and (node.value==val):
                print('2 part')
                parametr=1
                self.tail=self.tail.prev
                self.tail.next=None
                if parametr==1:
                    break 
            elif (node.value == val):
                print('3 part') 
                parametr=1  
                node_pr=node.prev
                node_next=node.next
                node_pr.next=node.next
                node_next.prev=node_pr.value
                if parametr==1:
                   break
            node=node.next 

    def insert_node(self,number,val):
        # Метод класса LL позволяющий вставить э-т Node в LL
        count_iteration=0
        node_for_iter=self.head
        while node_for_iter != None:
            count_iteration+=1 
            node_for_iter=node_for_iter.next
        if self.head==None:
            self.tail=self.head=Node_2(val)
        elif number==0:
            new_node=Node_2(val)
            new_node.next=self.head
            self.head=new_node
        elif number>=count_iteration:
            new_node=Node_2(val)
            new_node.next=None
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
        else:
            curr_node=self.head
            count=1
            while curr_node != None:
                if count==number:
                    new_node=Node_2(val)
                    next_node=curr_node.next
                    print(new_node.value,'new_node.value')
                    new_node.next=next_node
                    print(new_node.next.value,'next.value')
                    new_node.prev=curr_node
                    curr_node.next=new_node
                    print(curr_node.next.value,'curr.next')
                    break
                count+=1    
                curr_node=curr_node.next
        
   


first_list=Linked_List_2()
n1=Node_2(34)
first_list.add_in_tail(n1)
n2=Node_2(45)
first_list.add_in_tail(n2)
first_list.add_in_tail(Node_2(76))
first_list.add_in_tail(Node_2(789))
first_list.add_in_tail(Node_2(8))
first_list.add_in_tail(Node_2(7855))
first_list.add_in_tail(Node_2(78))
print('********************')
first_list.print_all_nodes()
first_list.delete_node(789)
print('********************')
print('Удаление')
first_list.print_all_nodes()
print('********************')
print('Вставка')
first_list.insert_node(2,234)
first_list.print_all_nodes()
input('Enter')