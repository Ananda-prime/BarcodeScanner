import pandas as pd
import json

'''Opening JSON file'''
f = open("Employee_details.json")
'''returns JSON object as a dictionary'''
data = json.load(f)
print(data)
'''
df = pd.DataFrame.from_dict(data, orient ='index')

print(df)
result = df.to_string()
print(type(result))

'''

user_in = input("enter the value")
# print(user_in)
for key, value in data.items():
    if user_in == key:
        use = value
        print(use)
        str = str(use).replace("{", "").replace("}", "")
        print(type(str))
        print(str)


        '''
         df = pd.DataFrame.from_dict(value, orient='index')
        print(df)
        result = df.to_string()
        print(result)
        
        '''
