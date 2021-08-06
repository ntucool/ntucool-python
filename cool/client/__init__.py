import atexit
import urllib.parse

import requests
import lxml.html

from cool.api import objects


class Client(objects.Interface):

    def __init__(self, session=None, base_url: str = 'https://cool.ntu.edu.tw/') -> None:
        if session is None:
            session = requests.Session()
            atexit.register(session.close)
        super().__init__(session=session, base_url=base_url)

    def saml(self, username, password):
        url = urllib.parse.urljoin(self.base_url, '/login/saml')
        response = self._session.request('GET', url)
        response.raise_for_status()
        html: lxml.html.HtmlElement = lxml.html.document_fromstring(response.text)
        form: lxml.html.FormElement = html.xpath('//*[@id="MainForm"]')[0]
        url = urllib.parse.urljoin(response.url, form.action)
        data = form.fields
        data['ctl00$ContentPlaceHolder1$UsernameTextBox'] = username
        data['ctl00$ContentPlaceHolder1$PasswordTextBox'] = password
        response = self._session.request(form.method, url, data=data)
        response.raise_for_status()
        html: lxml.html.HtmlElement = lxml.html.document_fromstring(response.text)
        form: lxml.html.FormElement = html.xpath('/html/body/form[@name="hiddenform"]')[0]
        url = urllib.parse.urljoin(response.url, form.action)
        data = form.fields
        response = self._session.request(form.method, url, data=data)
        response.raise_for_status()
