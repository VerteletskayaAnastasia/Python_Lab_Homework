# TODO решите задачу
import json
def task() -> float:
    with open('input.json', "r", encoding='utf-8') as f:
        ans=[_['score']*_['weight'] for _ in json.load(f)]
        ans=sum(ans)
    return round(ans,3)
print(task())
