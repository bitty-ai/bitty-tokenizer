import json

correct = '<correct-file-path>'
testing = '<trained-file-path>'


with open(correct, 'r') as f:
    correct_data = json.load(f)

with open(testing, 'r') as f:
    testing_data = json.load(f)

for k1,v1 in correct_data.items():
    found = False
    for k2,v2 in testing_data.items():
        if v1 == v2:
            # print(f'Found matching for {v1}')
            found = True
            del testing_data[k2]
            break

    if found == False:
        print(f'Not found for {v1}')    

print('======')
for k,v in testing_data.items():
    print(f'Instead found {v}')
    