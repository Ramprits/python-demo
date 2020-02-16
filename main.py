# password = input('enter your password! ')
password = '1245785415'
secure_password = len( password[0:-4])
show_password = password[secure_password:]
hidden_password = '*'* secure_password
print(f'{hidden_password}{show_password}')
