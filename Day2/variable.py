import datetime
import json
## 整數型態
i1=10
print(f'i1: {i1}')
i2=10^3
print(f'i2: {i2}')

## string 

str1='12345'
str2=f'{str1}-{i2}' + str1
print(f'str2: {str2}')
## lists
list1 =[1, 2, 3, 4, 6]
print(f'list1: {list1}')

list2 = ['abc', 'cde', 'efg']
print(f'list2 : {list2}')


## object
angel={
    'name':"黃千倚",
    "age":18,
    "company":"asus"
}

print(f"angel:\n{json.dumps(angel, indent=2)}")