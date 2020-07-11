import os
from exchangelib import Credentials, Account, FileAttachment

path = os.path.expanduser("~/Desktop/NSSR/")

credentials = Credentials('jrodrigue253@dxc.com', 'Jdrs2483$s')
account = Account('aldeaload@dxc.com', credentials=credentials, autodiscover=True)

inboxFolder = account.inbox

for item in inboxFolder.all().order_by('-datetime_received')[:5]:
    print("Reading Email: ",item.subject, item.sender, item.datetime_received)
    for attachment in item.attachments:
        if isinstance(attachment, FileAttachment):
            local_path = os.path.join(path, attachment.name)
            with open(path, 'wb') as f:
                f.write(attachment.content)
