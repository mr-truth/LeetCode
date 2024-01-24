# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    #создаем множество
    seen = set()
    # начинаем обход элементов списка
    for num in nums:
        # если элемент из списка уже есть в сете, возвращаем True
        if num in seen:
            return True
        # иначе добавляем элемент в сет
        seen.add(num)
        #итерации продолжаются до тех пор, пока не найдется совпадение или не дойдем до конца списка
    return False


print(containsDuplicate(nums = [1,2,3,1]))