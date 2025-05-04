# Note: When python runs a file it first set some specilal variables before even run any code. 
# And when python runs a file dirctory it sets __name__ special variable to '__main__'. 
# But when we import this file from another python module the __name__ variable become the name of that file.


print(f'First module\'s name: {__name__}')


################################


def main():
    print('This func runs only if the file runs directly.')


if __name__ == '__main__':
    main()
else:
    print(f'{__name__} imported here!')


