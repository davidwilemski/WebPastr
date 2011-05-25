#!/usr/bin/env python

# Copyright (C) 2010, 2011 by David Wilemski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import urllib
from google.appengine.api import urlfetch

class PostHandler(webapp.RequestHandler):
    def get(self):
		text = str(self.request.get('code'))
		
		form_fields = {
		  "paste_code": text,
		  "paste_format": "text",
		  "paste_expire_date": "1M"
		}
		
		form_data = urllib.urlencode(form_fields)
		result = urlfetch.fetch(url="http://pastebin.com/api_public.php", payload=form_data, method=urlfetch.POST, headers={'Content-Type':'application/x-www-form-urlencoded'})
                        
		self.response.out.write(result.content)

def main():
    application = webapp.WSGIApplication([('/post', PostHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
