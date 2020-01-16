from statistics import mean 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key, value in student_marks.items():
      if key == query_name:
        # d = float(sum(student_marks.value) / len(student_marks.value))
        # print(d)
        result = float(mean(value))
        print(format(result, '.2f'))