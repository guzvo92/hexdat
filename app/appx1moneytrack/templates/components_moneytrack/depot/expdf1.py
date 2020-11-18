def invoicepdf(request,d):
    if path.exists('media/invoice/%s.pdf'%d) == True: ----to check if file already exist for this order
        return HttpResponseRedirect('/media/invoice/%s.pdf'%d)  ---if so then return the pdf file
    else:

        if inv:
            cookie_list = request.COOKIES
            ---pass the cookies. You can add whatever other options you want to use
            options = {
                'cookie' : [
                    ('csrftoken', cookie_list['csrftoken']),
                    ('sessionid', cookie_list['sessionid']),
                    ],
                'page-size': 'A4',
                'margin-top': '0',
                'margin-right': '0',
                'margin-bottom': '0',
                'margin-left': '0',
                'encoding': 'UTF-16'

                }
            config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            pdfkit.from_url(request.get_host()+'/%s'%d, 'media/invoice/%s.pdf'%d,configuration=config,options=options)
            return HttpResponseRedirect('/media/invoice/%s.pdf'%d)
        else:
            messages.error(request, 'No order exist with this order no.')
            return HttpResponseRedirect('/orders')
