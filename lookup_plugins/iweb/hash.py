from ansible import utils
from hashlib import md5

def pwapp(username, hostname):
    m = md5('%s%s%s' % ('SuperSecret', username, hostname))
    h = m.hexdigest()
    return h[:8]

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, inject=None, **kwargs):
        terms = utils.listify_lookup_plugin_terms(terms, self.basedir, inject)
        #print terms
        #if isinstance(basestring, terms):
        #    terms = [ terms ]
        return [pwapp(term, inject['inventory_hostname']) for term in terms]
