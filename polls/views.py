from django.http import HttpResponse
from django.shortcuts import render
import pymysql
from django.template import loader
keywords_list = [['健身']]
cookies = """BIDUPSID=D4324DC8BC1C635DCE413B86B126DA94; PSTM=1628175502; __yjs_duid=1_e0be1922c1c05926cbb6e8f61582b5641628175781888; BAIDUID=5BF0D0E2322DB2174CC036653B10C90A:FG=1; BDUSS=UJyNGdVZn5ZZS10bEFTc1BSSjdvc3JHRGZmWDRSLVBQSlRnZUNGWUZXSFdIRXhpSVFBQUFBJCQAAAAAAAAAAAEAAAB4dXJfy~vU2rjmy9~E42kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANaPJGLWjyRiU; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%221601336696%22%2C%22scope%22%3A1%7D%7D; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1653792540,1656145907; bdindexid=dk9cj2r0b2rlk6jphts4ccj6e7; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1656145986; BDUSS_BFESS=UJyNGdVZn5ZZS10bEFTc1BSSjdvc3JHRGZmWDRSLVBQSlRnZUNGWUZXSFdIRXhpSVFBQUFBJCQAAAAAAAAAAAEAAAB4dXJfy~vU2rjmy9~E42kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANaPJGLWjyRiU; ab_sr=1.0.1_NjRlOWY1MWNjZjIzNTM4YjY0YzJiYmE5ZWQxOWJmMDk0MDRiOTg3NGU2N2YxYzhlYmQ0NWRlZGNiZWZmM2YwMzcwNGU4MjRkODFkOGZjNGFlZTY3OTE1NTRjMjJlNzFiMzQxZTdjNTcwOTA1YzEyYWZlMjIzZGI3NTU2ODc1YjU5MzQ3NzNjOWMxZDBkYTdlMTA1MjVlNjRiZjE3NzNlYg==; BA_HECTOR=2kakaka080212l8h201hbdi5h15; ZFY=6YO7SZVgX:AbnNBClYGgzVZ8M2cqEeTjpbCk24pl24JM:C; BAIDUID_BFESS=C0A20B6C2E671ABAE788FE4E51B1C5A9:FG=1; H_PS_PSSID=36550_36625_36673_36454_36666_36452_36692_36165_36695_36696_26350_36469; RT="z=1&dm=baidu.com&si=up7biz9ptw&ss=l4tmiga3&sl=c&tt=61c&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1qne&ul=1s91e"""

def test_get_search_index():
    """获取搜索指数"""

def index(request):
    db = pymysql.connect(host="81.68.243.156", user="root", password="ccgj1999", database='rwdata')
    cursor = db.cursor()
    sql = "select * from bdindex"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    date=[]
    value=[]
    for s in myresult:
        d1=s[1][-5:]
        v1=int(s[2])
        date.append(d1)
        value.append(v1)
    context = {"date": date,'value':value}
    return render(request,'polls/index.html',context)