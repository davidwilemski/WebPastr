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

class MainHandler(webapp.RequestHandler):
    def get(self):
		content = """
		<h1>WebPastr</h1>
		<p>This is a project by <a href="davidwilemski.com">David Wilemski</a> that will create a new pastebin dump using just a url. I originally create this to use with <a href="alfredapp.com">Alfred</a> and to learn how a basic Google App Engine app works.</p>
		<p>Please send requests to /post</p>
		<div>
		Example:<br>
			<code>
				webpastr.appspot.com/post?code=testing%20WebPastr
			</code><br><br>
			Output:<br>
			<code>
				http://pastebin.com/XAe22ws6	
			</code>
		</div>

		<p>To learn more, read my <a href="http://davidwilemski.com/blog/85/building-a-quick-and-dirty-web-service-on-google-app-engine-webpastr/">blog post</a> about it. You can also see the code on <a href="github.com/davidwilemski/webpastr">github.</p>
		
		"""
		self.response.out.write(content)

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
