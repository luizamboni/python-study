import imaplib
import email
import re
import argparse


def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--imap-host', type=str)
    parser.add_argument('--imap-port', type=str)
    parser.add_argument('--email-user', type=str)
    parser.add_argument('--email-password', type=str)
    parser.add_argument('--look-for', type=str)
    return parser.parse_args()

args = get_cli_args()

imap_host = args.imap_host
imap_port = args.imap_port
email_user = args.email_user
email_password = args.email_password
look_for = args.look_for

print(f"look for {look_for}")
imap = imaplib.IMAP4_SSL(imap_host, imap_port)

imap.login(email_user, email_password)

mailbox = 'Inbox'

# list folders
# print(imap.list(mailbox))

imap.select(mailbox)

stat, data = imap.search(None, 'ALL')

if stat == "OK":
    # from older to newer
    for mailid in data[0].split():
        print(mailid)
        message = imap.fetch(mailid, '(RFC822)')
        msg = email.message_from_bytes(message[1][0][1])  


        senders = msg.get_all("from", [])
        
        for sender in senders:
            try:
                name, address = email.utils.parseaddr(sender)
                print(address)
                if look_for in sender:
                    body = ''
                    if msg.is_multipart():
                        for part in msg.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))

                            # skip any text/plain (txt) attachments
                            if ctype == 'text/plain' and 'attachment' not in cdispo:
                                body = part.get_payload(decode=True)  # decode
                                break
                            # not multipart - i.e. plain text, no attachments, keeping fingers crossed
                    else:
                        body = msg.get_payload(decode=True)

                    print(body[:200])
            except Exception as e:
                print(e)

imap.close()
imap.logout()

