import requests,random,threading,time

User_Agen = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
]

header = {
    'User-Agent': random.choice(User_Agen),
    'Origin': 'http://xky.guet.edu.cn:82',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}

loginUrl = 'http://xky.guet.edu.cn:82/student/public/login.asp'
courseUrl = 'http://xky.guet.edu.cn:82/student/Select.asp'

def rub(username,password,classID):
    time.sleep(0.1)
    data = {
        'username': username,
        'passwd': password,
        'login': '%B5%C7%A1%C2%BC'
    }

    classinfo = {
        'course': classID,
        'lwBtnselect': '%CC%E0%BD%BB'
    }
    login = requests.Session()
    header['User-Agent'] = random.choice(User_Agen)
    login.headers.update(header)

    while 1:
        try:
            login.post(loginUrl, data=data, timeout=0.5)
            print('%s��¼�ɹ�'%data['username'])
            break
        except:
            print('%s��¼ʧ��'%data['username'])
            pass

    while 1:
        while 1:
            try:
                rub = login.post(courseUrl, data=classinfo, timeout=0.5)
                break
            except:
                print('%s���ڳ���ѡ��'%data['username'])
                pass
        try:
            if rub.text.index('�ѱ����뵽���ݿ���') != -1:
                print('%sѡ�γɹ���' % data['username'])
                with open('success.txt','a') as file:
                    file.write(data['username']+'\r\n')
                break
        except:
            try:
                if rub.text.index('ѡ����������') != -1:
                    print('%s��ѡ�γ�����'%data['username'])
                    break
            except:
                try:
                    if rub.text.index('���Ѿ�ѡ��') != -1:
                        print('%s��ѡ�ÿγ�'%data['username'])
                        break
                except:
                    try:
                        if rub.text.index('��ѡ�����ѳ���') != -1:
                            print('%s��ѧ����ѡ�γ�����'%data['username'])
                            break
                    except:
                        pass
            print('%sѡ��ʧ�ܣ�ԭ��δ֪'%data['username'])
            break

UserList = './SelectList.txt'
with open(UserList) as Users:
    lines = Users.readlines()
    myData = {}
    for line in lines:
        myData['user'] = myline[0]
        myData['passwd'] = myline[1]
        myData['courseID'] = myline[2]
        myThread = threading.Thread(name='User: ' + myData['user'], target=rub,args=(myData['user'], myData['passwd'], myData['courseID'],))
        myThread.start()
