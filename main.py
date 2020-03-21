from requests_html import HTMLSession
from bs4 import BeautifulSoup


class Service:
    def __init__(self, name, status):
        self.name = name
        self.status = status.strip()

    def get_status(self):
        healthy = u'\U0001f44D'
        unhealthy = u'\U0000274C'
        status_txt = healthy if self.status == 'Available' else unhealthy
        return '{}: {}'.format(self.name, status_txt)


def get_html():
    session = HTMLSession()
    resp = session.get('https://www.apple.com/support/systemstatus/')
    resp.html.render()
    return resp.html.html


def main():
    services = []
    html_data = get_html()
    res = BeautifulSoup(html_data, 'lxml')
    tags = res.findAll('div', {'class': 'event'})
    print('--- {} ---'.format(res.title.text))

    for tag in tags:
        parsed_service = tag.text.split('-')
        services.append(
            Service(''.join(parsed_service[:-1]), parsed_service[-1]))

    output = ''
    for i, service in enumerate(services):
        print(service.get_status())


if __name__ == '__main__':
    main()
