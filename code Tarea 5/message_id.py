import imaplib
conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
gmail_user = 'lorenzolaab'
gmail_pwd = 'XXXXXXXXX'

conn.login(gmail_user, gmail_pwd)
conn.select()
status, data = conn.search(None, '(FROM "messages-noreply@linkedin.com")') # search with label key 'messages-noreply@linkedin.com' 
#status, data = conn.search(None, 'SUBJECT', '"subject string"')   # This is though subject key search
for index, num in enumerate(data[0].split()):
    #print(num) # get all message IDs
    #status, raw_mail = conn.fetch(num, '(RFC822)')
    typ, dat = conn.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
    print(f"{index+1}: {dat[0][1]}")