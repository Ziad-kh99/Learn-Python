file_name = input('Enter file name: ')

try:
    file_handle = open(file_name)
except:
    print(f'Cannot open file: {file_name}')
    exit()


emails_dict = dict()

for line in file_handle:
    if line.startswith('From '):
        email = line.split()[1]
        email = email.split('@')[1]
        emails_dict[email] = emails_dict.get(email, 0) + 1


print(emails_dict)



