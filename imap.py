import imaplib

mail = imaplib.IMAP4_SSL('poczta.interia.pl')

#imaplib.IMAP4_SSL('imap.interia.pl')
mail.login('mb.test99@interia.pl', 'aaa123')
mail.list()

# Out: list of "folders" aka labels in gmail.
mail.select("INBOX") # connect to inbox.
print 10 * '/'
print mail.select("INBOX")

# IMAP SEARCH FUNCTION - ON <date> Messages whose internal date (disregarding 
# time and timezone) is within the specified date.

### second part
today = mail.search(None, 'ON', '2016-08-10')
print today
''' 
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest
 
result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
raw_email = data[0][1] # here's the body, which is raw text of the whole email
print raw_email
# including headers and alternate payloads
'''
