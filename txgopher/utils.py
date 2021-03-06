import urlparse
import urllib2

from txgopher import const


def getClientParams(url=""):
    result = urlparse.urlparse(url)
    scheme = result.scheme
    host = const.defaultHost
    port = const.defaultPort
    item = const.defaultItem
    query = ""
    hostAndPort = [
        x for x in result.netloc.split(const.hostPortSeparator) if x]
    if len(hostAndPort) == 1:
        [host] = hostAndPort
    elif len(hostAndPort) == 2:
        host, port = hostAndPort
    # note that getting the item type from the URL can be handy, just not
    # always authoritative -- best to check the returned data directly
    itemAndSelector = result.path
    parts = [x for x in itemAndSelector.split(const.selectorSeparator) if x]
    if parts:
        firstElement = parts[0]
        if firstElement in const.ALL_ITEMS:
            parts.pop(0)
            item = firstElement
            if item == const.SEARCH:
                query = urllib2.unquote(result.query)
    selector = "/" + const.selectorSeparator.join(parts)
    return (item, selector, host, port, query)
