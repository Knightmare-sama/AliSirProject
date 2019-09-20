import bs4,mechanize
from xlwt import Workbook

def marksGenerator(i):

    br = mechanize.Browser()
    br.open("https://www.osmania.ac.in/res07/20190855.jsp")
    br.select_form('FrontPage_Form1')
    br.form['htno'] = '160418733'+str(i)

    response1 = br.submit()
    raw = response1.read()
    soup = bs4.BeautifulSoup(raw,"html5lib")
    containers = soup.findAll("td",{"width":"50%"})
    return containers[10].text[10:14]


wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 0, 'roll numbers')
sheet1.write(0, 1, "result")
for i in range(1,10):
    sheet1.write(i,0,i)
    sheet1.write(i,1,(marksGenerator("00"+str(i))))

for i in range(10,100):
    sheet1.write(i,0,i)
    sheet1.write(i,1,(marksGenerator("0"+str(i))))

for i in range(100,121):
    sheet1.write(i,0,i)
    sheet1.write(i,1,(marksGenerator(str(i))))

wb.save('results.xls')