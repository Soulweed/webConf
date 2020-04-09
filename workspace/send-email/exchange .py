from exchangelib import Configuration, Account, DELEGATE, Credentials
from exchangelib import Message, Mailbox, FileAttachment, protocol
import time
import requests

from datetime import datetime, timedelta


from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter


def connect(server, email, username, password):
    """
    Get Exchange account cconnection with server
    """
    creds = Credentials(username=username, password=password)
    
    config = Configuration(server=server, credentials=creds)
    # account = Account(primary_smtp_address=email, autodiscover=False, config=config, access_type=DELEGATE)
    
    
    # ews_url = account.protocol.service_endpoint
    # ews_auth_type = account.protocol.auth_type
    
    # config_cache = Configuration(service_endpoint=ews_url, credentials=creds, auth_type=ews_auth_type)
    
    
    return Account(primary_smtp_address=email, autodiscover=False, config=config, access_type=DELEGATE)

def send_email_register(emp_email, line_id, id):
    try:
        recipient_list = [emp_email]
        print('receipient list', recipient_list)
        server = '202.151.5.104'
        # server = 'email.pea.co.th'
        email = 'peacovid19@pea.co.th'
        username = 'peacovid19'
        password = 'peacovid19'
        
        
        BaseProtocol.USERAGENT ='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
        
        
        account = connect(server, email, username, password)
        subject = 'ยืนยันการลงทะเบียน jjj'
        body = 'รหัสพนักงานของท่าน {} ได้มีการลงทะเบียนกับ PEA COVID-19\n\n' \
            'กรุณาเริ่มต้นการใช้งาน โดยยืนยันตัวตนของท่านผ่านข้อความฉบับนี้ โดยคลิกตาม link ด้านล่างนี้\n\n ' \
            'https://pea-covid19-test.herokuapp.com/register/{}{}/ \n\n' \
            'เพื่อกรอกข้อมูลส่วนตัว และประเมินความเสี่ยงเบื้องต้น \n\n' \
            'ขอขอบพระคุณที่ท่านร่วมเป็นส่วนหนึ่งกับเรา ในการผ่านวิกฤติ COVID-19 ไปด้วยกัน\n\n' \
            'PEA COVID-19 \n' \
            'By PEA Innovation Hub'.format(id, line_id, id)
        m = Message(account=account,
                    subject=subject,
                    body=body,
                    to_recipients=recipient_list)
        m.send_and_save()
        
        protocol.close_connections()
        print('email register send: {} : {}'.format(id, emp_email))
        return True
    
    except Exception as e:
        print(" >>>> Fail: {}".format(e)) 
        return False

if __name__ == "__main__":
    
    flag = False
    while flag == False :
        flag = send_email_register('nontachai.yoo@pea.co.th', 'xxx', '123')
        if flag == True:
            break
        time.sleep(5)
    
    print("+++++++++++  Send Email Complete  +++++++++++++")