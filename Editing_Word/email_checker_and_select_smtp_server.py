import sys
import re

def domain_name (email):

    domain = ""
    error = False

    try :
        email_length = email.split('@')
        user,domain = email.split('@')

        test_email = len(email_length)

        if (test_email != 2 or domain == ""):
            error = True
            #print ("This is not a correct email address...")
            #sys.exit()

        #print ("Email: " + email + " | Domain: " + domain)
    except ValueError :
        error = True
        #print ("This is not a correct email address...")
        #sys.exit()


    try :
        domain_length = domain.split('.')
        domain_name,domain_register =  domain.split('.')
        test_domain = len(domain_length)

        if (test_domain != 2 or domain_register == ""):
            error = True
            #print ("This is not a correct domain for email address...")
            #sys.exit()

        #print ("Domain Name: " + domain_name + " | Domain Register: " + domain_register)
    except ValueError :
        error = True
        #print ("This is not a correct domain for email address...")
        #sys.exit()

    return domain,error

def hotmail():
    print ("SMTP Hotmail (Outlook)")
    smtp_server = "Smtp.live.com"
    return smtp_server

def gmail():
    print ("SMTP Gmail")
    smtp_server = "smtp.gmail.com"
    return smtp_server

def yahoo():
    print ("SMTP Yahoo")
    smtp_server = "Mail.yahoo.com"
    return smtp_server

switcher = {
        1: hotmail,
        2: gmail,
        3: yahoo
        }

def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "This email is not recognized")
    # Execute the function
    return func()

    # Get the function from switcher dictionary
    #func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    #print (func)

def get_smtp_server(domain):
    if re.search(rf"hotmail|outlook", domain, re.IGNORECASE):
        output = numbers_to_strings(1)
        print (output)
    elif re.search(rf"gmail", domain, re.IGNORECASE):
        output = numbers_to_strings(2)
        print (output)
    elif re.search(rf"yahoo", domain, re.IGNORECASE):
        output = numbers_to_strings(3)
        print (output)
    else:
        print ("SMTP Server Not found...")

############################## Following lines are for testing purposes

try:
    output = get_smtp_server("gmail")

except TypeError :
    print ("This is not a valid email domain server...")

#email = input ("Please enter your email address: " )

#domain,error = domain_name(email)

#print ("This is the domain: " + domain + " | The domain is not correct: " + str(error))
