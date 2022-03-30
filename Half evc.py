print('-Evcplus-')
# creating new pin for the user
create_pin1 = input('Fadlan geli pin cusub ')
create_pin2 = input('ku celi pinkaaga ')
# checking while pin created same 
while create_pin1 != create_pin2:
    print('-Ismalahan labada number-')
    create_pin1 = input('Fadlan geli pin cusub ')
    create_pin2 = input('ku celi pinkaaga ')
    if create_pin1 == create_pin2:
        print('Waad ku guuleysatay inaa iska diiwaangelisay adeegan!')
        break
    else:
        continue
# Login with pin 
pin = input('Fadlan geli pin-kaaga ')
if pin == create_pin2:
    print('Evcplus')
    print('1.Itus haraagaaga')
    print('2.kaarka hadalka ')
    print('3.Bixi bill')
    print('4.Uwareeji Evcplus')
    print('5.Warbixin kooban ')
    print('6.Salaam bank')
    print('7.kordhi xisaabtaada')
    print('8.Maareynta ')
    print('9.Bill payment')
else:
	print('pinkaaga waa khalad')
# operation after login 
system = input(' ')
if system == '1':
	print('Haraagaagu waa 20$')
elif system == '2':
	print('1.ku shubo airtime')
	print('2.ugu shub airtime')
	k = input('')
	if k == '1':
		n = input('Geli lacagta ')
	else:
		i = input('Geli numberka ')
elif system == '4':
	j = input('Geli numberka aad u direyso ')
	l = input('Geli lacagta ')
	print('Uwareeji $', l, 'numberka', j, '?')
	print('1.Haa')
	print('2.Maya')
	v = input('')
	if v == '1':
		print('[-EVCPlus-] $ ' ,l ,  '  ayaad uwareejisay ' , j , ' Tar: 29/   03/22 06:46:40, Haraagaagu waa $ 19.')

