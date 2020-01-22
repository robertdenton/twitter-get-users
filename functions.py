import os, json, logging, logging.handlers

# logger
logger = logging.getLogger('logger')

# Set current dir
dir_path = os.path.dirname(os.path.realpath(__file__))

def getSecret(service, token='null'):
    
    with open("{0}/secrets.json".format(dir_path)) as data:
        s = json.load(data)
        #print s
        #print s['{}'.format(service)]['{}'.format(token)]
        # If there is no token, return whole parent object
        if token == 'null':
            secret = s['{}'.format(service)]
        else:
            secret = s['{}'.format(service)]['{}'.format(token)]
        logger.debug("EXIT secrets: {}".format(len(secret)))
        return secret