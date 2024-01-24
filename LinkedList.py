# Узел связанного списка
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Функция для печати заданного связанного списка
def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')


# Наивная функция для реализации связанного списка, содержащего три узла
def construct():
    # создание отдельных узлов связанного списка
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    # переупорядочить ссылки, чтобы составить список
    head = first
    first.next = second
    second.next = third
    third.next = fourth

    # возвращает первый узел в списке
    return head


if __name__ == '__main__':
    # `head` указывает на головной узел связанного списка
    head = construct()

    # распечатать связанный список
    printList(head)