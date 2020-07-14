import sys

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
    
    
    
#email = input ("Please enter your email address: " )

#domain,error = domain_name(email)

#print ("This is the domain: " + domain + " | The domain is not correct: " + str(error)) 