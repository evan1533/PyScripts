from lxml import html
import requests
import xlwt

years = range(2000,2018)
answers = [];
for yr in years:
    site_url = 'https://data.bls.gov/cgi-bin/cpicalc.pl?cost1=1.00&year1=' + str(yr) + '01&year2=201710';

    page = requests.get(site_url)
    tree = html.fromstring(page.content)

    answer = tree.xpath('//span[@id="answer"]/text()')
    inf_rate = answer[0]
    inf_rate = inf_rate[1:]
    print(inf_rate)
    answers.append(float(inf_rate))

print(answers)


def output(filename, sheet, list1):
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)
    for i in range(len(answers)):
        sh.write(i,0,years[i])
        sh.write(i,1,answers[i])

    book.save(filename)


output("Inflation Rates.xls",'inflation sheet',answers)
