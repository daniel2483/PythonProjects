from exchangelib import Credentials, Account

credentials = Credentials('jrodrigue253@dxc.com', 'Jdrs2483$s')
account = Account('aldeaload@dxc.com', credentials=credentials, autodiscover=True)

for item in account.inbox.all().order_by('-datetime_received')[:5]:
    print(item.subject, item.sender, item.datetime_received)
