#funs to connect to controller, linux machine and execute commands

import pexpect
import secret
import re

enpaswd = secret.enablepaswd

def controller_connect(ipaddr, user, paswd):
    print 'ssh ' + user + '@' + ipaddr
    child = pexpect.spawn('ssh ' + user + '@' + ipaddr)
    prompt = child.expect(['(yes/no)?', 'password: ', '>'])
    if prompt == 0:
        print 'sending yes'
        child.sendline('yes')
        print 'expecting passwd'
        child.expect('password: ')
        print 'sending passwd'
        child.sendline(paswd)
        prompt1 = child.expect(['#', '>'])
        if prompt1 == 0:
            child.sendline(' ')
        elif prompt1 == 1:
            child. sendline('enable')
            child.expect(':')
            child.sendline(enpaswd)
    elif prompt == 1:
        child.sendline(paswd)
    elif promt == 2:
        child.sendline('enable')
        child.expect(':')
        child.sendline(enpaswd)


    child.expect('#')
#    child.sendline('no paging')
#    child.expect('#')
#    child.sendline('show version')
#    child.expect('#')
#    a = child.before
#    print a
#    print (child.after)
    return child

def lin_login(linip, linuser, linpaswd):
    print 'ssh ' + linuser + '@' + linip
    linchild = pexpect.spawn('ssh ' + linuser + '@' + linip)
    prompt = linchild.expect(['(yes/no)?', 'word: '])
    if prompt == 0:
        print 'sending yes'
        linchild.sendline('yes')
        print 'expecting passwd: after yes'
        linchild.expect('word: ')
        print 'sending passwd after yes'
        linchild.sendline(linpaswd)
        print 'expecting #'
        linchild.expect('#')
    else:
        print 'sending passwd'
        linchild.sendline(linpaswd)
        linchild.expect('#')
    return linchild

def iap_login(iapip, iapuser, iappaswd):
    print 'ssh ' + iapuser + '@' + iapip
    iapchild = pexpect.spawn('ssh ' + iapuser + '@' + iapip)
    prompt = iapchild.expect(['(yes/no)? ', 'password: '])
    print "prompt is {}".format(prompt)
    if prompt == 1:
        print 'sending yes'
        iapchild.sendline('yes')
        print 'expecting password: after yes'
        iapchild.expect('word: ')
        print 'sending password after yes'
        iapchild.sendline(iappaswd)
        print 'expecting #'
        iapchild.expect('#')
    elif prompt == 0:
        print 'sending paswd'
        iapchild.sendline(iappaswd)
        iapchild.expect('#')
    iapchild.sendline('show version')
    iapchild.expect('#')
    print 'iapchild.b4 is ', iapchild.before
    iapmac_match = re.search('\n(.*)$', iapchild.before)
    iapprompt = iapmac_match.group(1) + '#'
    print 'iapmac is {}'.format(iapprompt)
    return iapchild, iapprompt

def iap_exec(iaphandle, iapprompt, cmd):
    print 'sending ' + cmd + ' to iap'
    iaphandle.sendline(cmd)
    iaphandle.expect(iapprompt)

def lin_exec(linhandle, cmd):
    print 'sending ' + cmd + ' to lin'
    linhandle.sendline(cmd)
    linhandle.expect('#')

def con_exec(conhandle, cmd):
    print 'sending' + cmd + ' to controller'
    conhandle.sendline(cmd)
    conhandle.expect('#')

def file_open():
    result_file = open("memleak_result.log", "a")
    return result_file

def file_write(fp, data):
    fp.write(data)

def file_close(fp):
    fp.close()



