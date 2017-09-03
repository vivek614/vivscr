#To check the number of aps in swarm and get a count of each ap types
from controller import *
import secret   #username and ip address file

iap_command_list = ["show aps"]

iaphandle, iapprompt = iap_login(secret.iapip, secret.iapuser, secret.iappaswd)
print 'iapprompt is', iapprompt
print 'iaphandle is', iaphandle
iap_exec(iaphandle, iapprompt, iap_command_list[0])
print iaphandle.before

apnotfound = 1
apdict = {'325':0, '205':0, '225':0, '207':0, '203H':0, '305':0} 

for line in iaphandle.before.split('\n'):
    if re.compile(r'.+?:.+?:.+?:.+?:.+?:').search(line):    #check if the line contains mac address
        try:
            linesplit = line.split()
            print linesplit[1],
            print linesplit[5],
            print linesplit[-2]
            for ap in apdict:
#                if linesplit.split('(')[0] == ap
                if ap in linesplit[5]:
                    apdict[ap] += 1     #take ap count
                    apnotfound = 0
            if apnotfound:
                print 'new ap model found', linesplit[5]
                apdict[linesplit.split('(')[0]] = 1     #if a new model is found, add it to apdict
        except:
            pass
print apdict
