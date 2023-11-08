# TODO Напишите функцию find_common_participants
def find_common_participants(first_group,second_group,separator=","):
    first_group,second_group=first_group.split(separator),second_group.split(separator)
    second_group=set(second_group)
    intersection = second_group.intersection(first_group)
    intersection=list(intersection)
    intersection.sort()
    return intersection

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,'|'))