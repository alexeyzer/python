# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            for arg in args:
                if arg in item:
                    yield item[arg]
    else:
        for item in items:
            new_item = {}
            for arg in args:
                if arg in item:
                    new_item[arg] = item[arg]
            if len(new_item.keys()) > 0:
                yield new_item


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'color': 'black'}
]
if __name__ == '__main__':
    for i in field(goods, 'title'):
        print (i)
   #field(goods, 'title', 'price')