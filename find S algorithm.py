import csv
file = open('test.csv')
all_rows = csv.reader(file)
data =[]
for row in all_rows:
    data.append(row)

hypothesis = []
for instance in data:
    if hypothesis:
        if instance[-1] == 'Yes':
            for attribute_index in range(len(hypothesis)):
                if instance[attribute_index] != hypoyhesis[attribute_index]:
                    hypothesis[attribute_index] = '?'
else:
        hypothesis = instance[:-1]                    
