if __name__=='__main__':
    students=[]
    for _ in range(int(input())):
        name=input()
        score=float(input())
        students.append([name,score])
    grades=sorted(set([garde for _,garde in students]))
    second_lowest_garde=grades[1]  
    result=sorted([name for name, grade in students if grade==second_lowest_garde])
    
    for student in result:
        print(student)
      