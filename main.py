import pickle

passwd = 'passwd.dat'


def encrypt(msg):
    em = ''

    for l in msg:
        em += chr(ord(l)+2)

    return em


def save_new_cred(username, password):
    '''
    ADDING NEW CREDs
    '''

    with open(passwd, 'r+b') as file:
        content = pickle.load(file)

        content[username] = encrypt(password)
        print('write:', content)
        pickle.dump(content, file)



def test_login(username, password):
    '''
    TEST LOGIN
    '''

    with open(passwd, 'rb') as file:
        content = pickle.load(file)

        print(content)
        if username in content:
            if content[username] == encrypt(password):
                return True
    
    return False


if __name__ == '__main__':

    while True:
        print('SELECT BEST OPTION FOR YOU:')
        print('\t1. SAVE NEW CREDENTIAL')
        print('\t2. TEST LOGIN')
        print('\t3. EXIT')

        ch = int(input('ENTER YOUR CHOICE: '))


        match ch:
            case 1  :
                print('YOU CHOOSE *--SAVE NEW CREDENTIAL--*')

                username = input('Enter your username: ')
                password = input('Enter your password: ')

                save_new_cred(username, password)


            case 2  :
                print('YOU CHOOSE *--TEST LOGIN--*')
               
                username = input('Enter your username: ')
                password = input('Enter your password: ')

                ret  = test_login(username, password)

                if ret:
                    print('Success!')

                else:
                    print('Fail!')


            case 3  :
                print('THANKS FOR TRUSTING US!')
                exit()

            case _  :
                print('Wrong Choice')



