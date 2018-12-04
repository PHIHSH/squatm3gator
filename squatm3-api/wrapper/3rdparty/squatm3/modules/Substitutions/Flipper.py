# -*- coding: latin-1 -*-
from tld import get_tld
import codecs
import urllib


class Flipper:
    def __init__(self, url):
        self.url = url
        self.list_of_chars = []
        self.dictionary = {}

    def flip_letters(self):
        '''
        The following function

        '''

        url = get_tld(self.url, as_object=True, fix_protocol=True)
        domain = url.domain
        new_urls_without_letter = []
        n = 0
        m = len(domain)

        

        if m == 1:
            new_urls_without_letter.append(domain)
        elif m == 2:
            new_urls_without_letter.append(domain[1] + domain[0])

        else:

            while n < m and m > 2:

                if n == 0 :
                    new_domain = domain[n + 1] + domain[n] + domain[n + 2:m]

                elif n == 1:
                    new_domain = domain[0] + domain[n + 1] + domain[n] + domain[n + 2:m]

                elif 1 < n < m - 1:
                    new_domain = domain[0:n] + domain[n + 1] + domain[n] + domain[n + 2:m]

                n = n + 1
                new_urls_without_letter.append(new_domain)
        new_urls_list = list(set(new_urls_without_letter))
        return new_urls_list
