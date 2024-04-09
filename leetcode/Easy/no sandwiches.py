def count_students(students, sandwiches):
    queue = students[:]
    count = 0


    while queue and sandwiches:
        if queue[0] == sandwiches[0]:

            queue.pop(0)
            sandwiches.pop(0)
            count = 0
        else:

            queue.append(queue.pop(0))
            count += 1


        if count == len(queue):
            break

    return len(queue)


students = [1, 1,1,0, 0,1]
sandwiches = [1,0,0,0,1,1]

print(count_students(students, sandwiches))


