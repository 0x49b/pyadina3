from fpdf import FPDF
import os

'''
sudo apt-get update && sudo apt-get install cups cups-client lpr

import os
os.system("lpr -P 'ZJ-58' printMe.txt")

# Printer Name
# ZJ-58
'''


class Printing(object):
    page_width = 52
    config = None
    current_y = 0

    def __init__(self, config):
        print("starting printer")
        self.config = config
        print(self.config)

    def print_receipt(self, order, order_num, customer=True, filename='', printFontSize=8):

        pdf = FPDF(orientation='P', unit='mm')
        pdf.add_page()
        pdf.set_font("helvetica", "B", 24)

        # Neo-Phyt Logo
        if customer:
            pdf.image('./static/logo.jpeg', w=35, h=35, x=6, y=5)

        # Order Number
        order_no = "#{}".format(order_num)
        order_num_width = pdf.get_string_width(order_no)

        if customer:
            self.current_y = 42
        else:
            self.current_y = 5
        pdf.set_y(self.current_y)
        pdf.set_x((self.page_width / 2) - (order_num_width / 2) - 2)
        pdf.cell(w=order_num_width, h=16, txt=order_no, align='L')

        # Order
        pdf.set_font("helvetica", '', size=printFontSize)

        if customer:
            self.current_y = 55
        else:
            self.current_y = 15

        if order["0"] > 0:
            self.piadina_list(pdf, "0", order)
        if order["1"] > 0:
            self.piadina_list(pdf, "1", order)
        if order["2"] > 0:
            self.piadina_list(pdf, "2", order)
        if order["3"] > 0:
            self.piadina_list(pdf, "3", order)


        # Footer
        if customer:
            self.current_y = self.current_y + 10
            pdf.image('./static/instagram.jpeg', w=5, h=5, x=0, y=self.current_y)
            pdf.set_y(self.current_y - 1.5)
            pdf.set_x(6)
            ist = 'neophytbadenfahrt'
            iwi = pdf.get_string_width(ist)
            pdf.cell(w=iwi, h=8, txt=ist)
        else:
            self.current_y = self.current_y + 5
            pdf.set_y(self.current_y)
            ts = order['timestamp']
            ftimestamp = 'Bestellt: ' + ts[11:19]
            timestamp_width = pdf.get_string_width(ftimestamp)
            pdf.cell(w=timestamp_width-5, h=10, txt=ftimestamp, align='L')

        pdf.output(filename)
        self.current_y = 0
        os.system("lpr -P ZJ-58 " + filename)

    def piadina_list(self, pdf, piadina, order):
        piadina_string = "{} x {}".format(order[piadina], self.config[piadina]["name"])
        piadina_string_width = pdf.get_string_width(piadina_string)

        pdf.set_y(self.current_y)
        pdf.set_x((self.page_width / 2) - (piadina_string_width / 2) - 2)
        pdf.cell(w=piadina_string_width, h=16, txt=piadina_string)
        self.current_y = self.current_y + 5
