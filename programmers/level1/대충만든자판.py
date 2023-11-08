def solution(keymap, targets):
    answer = []
    keyboard = {}
    for keys in keymap:
        for index, key in enumerate(keys):
            if key not in keyboard or keyboard[key] > index: 
                keyboard.update({key: index + 1})
    for target in targets:
        click = 0
        for alphabet in target:
            if alphabet not in keyboard:
                click = 0
                break
            else:
                click += keyboard[alphabet]
        if click == 0:
            answer.append(-1)
        else:                
            answer.append(click)
    return answer
keymap = ["AA"]
targets = ["B"]
print(solution(keymap, targets))