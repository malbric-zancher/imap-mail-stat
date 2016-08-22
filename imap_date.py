import getpass
import imaplib

#opening the server:pass:login formatted txt file
logins = open('data.txt', 'r').readline()
creds = logins.strip().split(':') #split on the : separator

mail = imaplib.IMAP4_SSL(creds[0]) #access 1st part - server name
mypassword = creds[1] #access 2nd part - pass
address = creds[2] #access 3rd part - login

mail.login(address, mypassword)
mail.select("inbox")
print("Checking for new e-mails for %s.") % address
typ, messageIDs = mail.search(None, '(ON "29-May-2013")')

messageIDsString = str(messageIDs[0])
listOfSplitStrings = messageIDsString.split(" ")
if len(listOfSplitStrings) == 0:
    print("You have no new e-mails.")
elif len(listOfSplitStrings) == 1:
    print("You have %d new e-mail.") % len(listOfSplitStrings)
else:
    print("You have %d new e-mails.") % len(listOfSplitStrings)
