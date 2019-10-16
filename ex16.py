
if __name__ == '__main__':
    users = ['anna','john','maria','markus','me']
    mails = ['anna@no.com','john@no.com','maria@no.com','markus@no.com']
    

    for data in zip(users,mails): 
        name,mail = data
        print(f'{name} -> {mail}')