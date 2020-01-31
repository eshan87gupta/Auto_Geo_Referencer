item = '234/4/1'
new_item = '/'.join(str(item).split('/')[:-1])
print(new_item)