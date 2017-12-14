import pexpect
import getpass
import sys

USERNAME = raw_input('Type your username >')
password = getpass.getpass('Enter your account password >')

with open ('STP_SW') as f:
        for line in f:
                HOST = line.strip()
                print 'logging into ' + HOST
                child = pexpect.spawn ('ssh ' + USERNAME + '@' + HOST)
                out_put = child.expect (['(yes/no)' , 'password: '])
                if out_put == 0:
                        child.sendline('yes')
                        child.expect('password: ')
                        child.sendline(password)
                        child.expect('#')
                        print 'Logging to ' + HOST + '...'
                elif out_put == 1:
                        child.sendline(password)
                        child.expect('#')
                else:
                     	print 'Node is unreachable!'

                print 'Gathering information ... '

                child.sendline('terminal length 0')
                child.expect('#')
                child.sendline('show spanning-tree root | in /')
                child.expect('#')

                #saving the output.
                show_output = child.before
                save_output = open(HOST + '_conf' , 'w')
                save_output.write(show_output)
                save_output.write('\n')
                save_output.close()
                print "Gathering information has been done! " + HOST + '_conf' + " file has been created"
                
