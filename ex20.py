
if __name__ == '__main__':
    user = {
          'name':'anna'
        , 'mail': 'anna@no.com'
        , 'phone':'111-22-33'
        , 'age':30
    }   

    for item in user.items():
        key,value = item
        print(f'key={key} value={value}') 