def solution(name, yearning, photo):
    answer = []
    score = {key: value for value, key in enumerate(name)}
    for index, point in enumerate(yearning):
        score[name[index]] = point
    for pic in photo:
        sumNum = 0
        for person in pic:
            print(person)
            sumNum += score.get(person, 0)
        answer.append(sumNum)
    return answer
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
answer = solution(name, yearning, photo)
print(answer)