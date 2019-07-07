import unittest

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
            print(node.value,'Output by print all nodes')
            node=node.next

    def lenght_list(self):
        # Метод класса LL, расчитывающий кол-во э-в класса Node в LL (длина LL)
        node=self.head
        l=0
        while node is not None:
            l+=1
            node=node.next
        return l 
        

    def delete_node(self,val,parametr=1):
        # Метод удаляет узел из списка по значению узла
        node = self.head
        while node is not None:
            if (node.value==self.head.value) and (node.value==val):
                new_head=node.next
                node.prev=None
                self.head=new_head
                parametr=1
                if parametr==1:
                    break
            elif (node.value==self.tail.value) and (node.value==val):
                parametr=1
                self.tail=self.tail.prev
                self.tail.next=None
                if parametr==1:
                    break 
            elif (node.value == val):
                parametr=1  
                node_pr=node.prev
                node_next=node.next
                node_pr.next=node.next
                node_next.prev=node_pr.value
                if parametr==1:
                   break
            node=node.next 

    def insert_node(self,number,val):
        # Метод класса LL позволяющий вставить э-т Node в LL, после э-та number
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
                    new_node.next=next_node
                    new_node.prev=curr_node
                    curr_node.next=new_node
                    break
                count+=1    
                curr_node=curr_node.next
def equal_linked_list(List_1,List_2):
    # Метод проверяющий равенство значений эл-тов связанных списков 
    Max_lenght_list=max(List_1.lenght_list(),List_2.lenght_list())
    node_1=List_1.head
    node_2=List_2.head
    for i in range(0,Max_lenght_list+1):
        print(node_1.value==node_2.value,'for ',i,' Node')

def linked_list_test_1():
    # Тест на равенство двух списков. Проверка равенства э-тов после удаления  одного э-та.
    print('****Test_1****')
    first_list=Linked_List_2()
    second_list=Linked_List_2()
    Qty=int(input('Enter q-ty off items in LinkedList '))
    for i in range(0,Qty):
        Linked_List_2_item=Node_2(int(input('Enter Node, it must be int. format ')))
        first_list.add_in_tail(Linked_List_2_item)
    print('****Initial data****')
    first_list.print_all_nodes()    
    Deleted_item=int(input('Enter deleted Node '))
    input('Now You should enter updated Linked List without deleted Node. Please press Enter ')
    for i in range(0,Qty-1):
        Linked_List_2_item=Node_2(int(input('Enter Node, it must be int. format ')))
        second_list.add_in_tail(Linked_List_2_item)
    print('****List with deleted (by program) Node, 1st list after deleted****')
    first_list.delete_node(Deleted_item)
    first_list.print_all_nodes()
    print('****2d List ****')
    second_list.print_all_nodes()
    print('********************')
    equal_linked_list(first_list,second_list)
    print('#First head',first_list.head.value,'# First tail',first_list.tail.value,'# List lenght' ,first_list.lenght_list(),'#')
    print('#Second head',second_list.head.value,'# Second tail',second_list.tail.value,'# List lenght', second_list.lenght_list(),'#')
    print('********************')

def linked_list_test_2():
    # Тест на равенство двух списков. Проверка равенства э-тов после добавления одного э-та.
    print('****Test_2****')
    first_list=Linked_List_2()
    second_list=Linked_List_2()
    Qty=int(input('Enter q-ty off items in LinkedList '))
    for i in range(0,Qty):
        Linked_List_2_item=Node_2(int(input('Enter Node, it must be int. format ')))
        first_list.add_in_tail(Linked_List_2_item)
    print('****Initial data****')    
    first_list.print_all_nodes()
    insert_item=int(input('Enter inserted Node '))
    number_after_insert=int(input('Enter number after that we insert Node '))
    first_list.insert_node(number_after_insert,insert_item)
    print('****List with inserted (by program) Node, 1st list after inserted****')
    first_list.print_all_nodes()
    input('Now You should enter updated Linked List with inserted Node. Please press Enter ')
    for i in range(0,Qty+1):
        Linked_List_2_item=Node_2(int(input('Enter Node, it must be int. format ')))
        second_list.add_in_tail(Linked_List_2_item)
    print('****Second List****')
    second_list.print_all_nodes()
    print('********************')
    equal_linked_list(first_list,second_list) 
    print('#First head',first_list.head.value,'# First tail',first_list.tail.value,'# List lenght' ,first_list.lenght_list(),'#')
    print('#Second head',second_list.head.value,'# Second tail',second_list.tail.value,'# List lenght', second_list.lenght_list(),'#')
    print('********************')

dicision=int(input('Enter 1 if You want to run Test_1, 2 if You want run Test_2, other number-will be starting both tests '))
if dicision==1:
    linked_list_test_1()
elif dicision==2:
    linked_list_test_2()
else: 
    linked_list_test_1()
    linked_list_test_2() 
input('Press any key')  

