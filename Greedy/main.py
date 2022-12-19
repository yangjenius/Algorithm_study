input_data = input()
data_arr = input_data.split('-')
result = []
output_data = 0

for i in data_arr:
    result.append(i.lstrip("0"))
    
output_data = eval(result[0])

for j in result[1:]:
    eval(j)
    output_data -= eval(j)
    
print(output_data)