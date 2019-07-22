import urllib.request, socket
import requests
import re


def is_bad_proxy(pip):
    try:
        proxy_handler = urllib.request.ProxyHandler({'https': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Gautam Sharma User Agent')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://requestbin.fullcontact.com/qz17aqqz')  # change the url address here
        sock=urllib.request.urlopen(req)
        print(req.full_url)
    except urllib.request.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print("ERROR:", detail)
        return 1

    return 0


if __name__ == '__main__':

    socket.setdefaulttimeout(10)
    parameters = {"type": 'https', "anon": 'elite', "country": 'US'}

    response = requests.get("https://www.proxy-list.download/api/v1/get", params=parameters)
    if response.status_code == 200:

        proxyList = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})', str(response.content))
        print('---------- ' + str(len(proxyList)) + ' Proxy IP Found ----------')
        working_ip =[]
        not_woring_ip = []
        for item in proxyList:
            if is_bad_proxy(item):
                not_woring_ip.append(item)
            else:
                working_ip.append(item)

        print('Total Working IP '+ str(len(working_ip)))

