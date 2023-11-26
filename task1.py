# TODO решите задачу
import json
def task() -> float:
    with open('input.json', "r", encoding='utf-8') as f:
        ans=0
        for _ in json.load(f):
            ans= ans+float(_['score']*_['weight'])
        return (round(ans,3))
print(task())
