EXIT = ['q','ex','exit','quit']


shopping_list = list()


def show_item(my_list : list):
    for item in my_list:
        print(f'> {item}')

def help_shopping():
    print('Enter `Quit` exit to shopping list')
    print('Enter `Help` show help for easier shopping')

def add_item(my_list : list , item : str):
    my_list.append(item)
    return my_list

while True:
    item = input('Enter a item: ')
    item = item.casefold()
    
    if item in EXIT:
        show_item()
        break
    elif item == 'help':
        help_shopping()
    elif item == 'show':
        show_item(shopping_list)
    else:
        if item in shopping_list:
            print("this item is repetitious")
        else:
            add_item(shopping_list,item)
            print(f'{item} add in my list , there is total {len(shopping_list)} in list')