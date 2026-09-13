if __name__ == '__main__':
    students = []
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        marks.append(score)
        
def sec_low(students,score):
    my_set = sorted(set(score))
    x= my_set[1]
    results = []
    for student in students:
        if student [1]==x:
            results.append(student[0])
    for result in sorted(results):
        print(result)
                
sec_low(students,marks)
