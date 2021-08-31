# prg 오픈채팅방

문제출처 -[코딩테스트 연습 - 오픈채팅방 | 프로그래머스 (programmers.co.kr)](https://programmers.co.kr/learn/courses/30/lessons/42888)

문제 요약 

 	1. 오픈채팅방 왕래 추적

input - 

```
record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
```

output-

```
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
```

해설코드 

```
def solution(record):
    total = []
    func=[]
    id={}
    ans=[]
    for i in (record):
        k=i.split()
        # print(k)
        z=k[0]
        # print(z)
        x=k[1]
        if z in ['Enter', 'Change']:
            person = k[2]
            id[x]=person
        ans.append([x,z])
    # print(ans)
    # print(id)
    for i in ans:
        if i[1]=='Enter':
            total.append(f'{id[i[0]]}님이 들어왔습니다.')
        elif i[1]=='Leave':
            total.append(f'{id[i[0]]}님이 나갔습니다.')
        elif i[1] == 'Change':
            pass
    # print(total)
    return total

record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

solution(record)
```



