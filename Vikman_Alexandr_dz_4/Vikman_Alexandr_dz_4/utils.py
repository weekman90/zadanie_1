def currency_rates(url, currency):
    from requests import get, utils
    currency=str(currency).upper()
    currency_names=[]
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    for i in content.split('ID='):
        for j in i.split('><'):
            if currency in j:
                for k in i.split('><'):
                    for kk in k:
                        if 'Value' in k:
                                                    # магическое жанглирование для float
                            a = k.split('<')
                            c = a[0]
                            b = c.split('>')
                            m = b[1].split(',')
                            x = m[0]+'.'+m[1]
                return (float(x))

            else:
                pass