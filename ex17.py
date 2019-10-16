
if __name__ == '__main__':
    users = ['anna','john','maria','markus','me']
    mails = ['anna@no.com','john@no.com','maria@no.com','markus@no.com']
    hash = {}

    for data in zip(users,mails): 
        name,mail = data
        hash[name] = mail

    print(hash)