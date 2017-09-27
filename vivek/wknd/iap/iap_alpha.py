#To check the number of aps in swarm and get a count of each ap types
from controller import *
import secret   #username and ip address file
import csv
import string


iap_command_list = ["show aps"]

iaphandle, iapprompt = iap_login(secret.iapip, secret.iapuser, secret.iappaswd)
print 'iapprompt is', iapprompt
print 'iaphandle is', iaphandle
iap_exec(iaphandle, iapprompt, iap_command_list[0])
print iaphandle.before

#apdict = {'325':0, '205':0, '225':0, '207':0, '203H':0, '305':0} 

apdict = {}

apmac = []
apip = []
aptype = []
apuptime = []


for line in iaphandle.before.split('\n'):
    apnotfound = 1
#    print 'taking line ---->', line #DBUG
    if re.compile(r'.+?:.+?:.+?:.+?:.+?:').search(line):    #check if the line contains mac address
        try:
            linesplit = line.split()
            apmac.append(linesplit[0])
            apip.append(linesplit[1])
            print apip,
            aptype.append(linesplit[5])
            print linesplit[5],
            apuptime.append(linesplit[-2])
            print apuptime,
            for ap in apdict:
#                if linesplit.split('(')[0] == ap
#                print 'value of ap is', ap #DBUG
                if ap in linesplit[5]:
#                    print 'checking if {} in {}'.format(ap, linesplit[5]) #DBUG
                    apdict[ap] += 1     #take ap count
                    apnotfound = 0
            if apnotfound:
                    print 'new ap model found', linesplit[5]
                    print 'new ap model is', linesplit[5].split('(')[0]
                    apdict[linesplit[5].split('(')[0]] = 1     #if a new model is found, add it to apdict
        except:
            pass

apstr = ""
aplist = []
with open('alpha_report.csv', 'w') as fp:
    writer = csv.writer(fp)
    for ele in apdict:
        apstr = apstr + ele + ' - ' + str(apdict[ele]) + ', '
    aplist.append(apstr.rstrip(', '))
    print apstr
    print aplist

    writer.writerow(aplist)
    writerlist = zip(apmac, apip, aptype, apuptime)
    writer.writerow(['Name', 'IP Address', 'Type', 'UP Time'])
    for row in writerlist:
        writer.writerow(row)

print apdict
