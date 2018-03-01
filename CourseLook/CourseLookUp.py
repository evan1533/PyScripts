from pyvt import Timetable
import smtplib
import SimpleEncryption as enc


phrase = str.lower(enc.decrypt_text("EAOLFIJHD"));
server = smtplib.SMTP('smtp.gmail.com:587');
server.ehlo()
server.starttls()
server.login("evan.a.ott@gmail.com",phrase);
class_insert = "Hey! These classes are open:\n\n";
is_open = False;

def sendBenMessage(class_message):
    msg = "\r\n".join([
        "From: user_me@gmail.com",
        "To: user_you@gmail.com",
        "THE CHAMBER OF SECRETS HAS BEEN OPENED",
        class_message]);
    server.sendmail("evan.a.ott@gmail.com", "8049378336@vtext.com", msg);

def sendMessage(class_message):
    msg = "\r\n".join([
        "From: user_me@gmail.com",
        "To: user_you@gmail.com",
        "Open Classes",
        class_message]);
    server.sendmail("evan.a.ott@gmail.com", "8049378336@vtext.com", msg);

timetable = Timetable();
f = open("C:\\Users\\Basketlord\\Desktop\\CourseLook\\SpringCRNs.txt","r")
crn_list = [];
for line in f:
    crn_list.append(int(line));
f.close();
Ben_Section = [13836, 13821, 13827, 18847];
ben_open = False;

for i in range(len(crn_list)):
    curClass = timetable.crn_lookup(str(crn_list[i]),term_year=201801,open_only=True)
    if curClass != None:
        is_open = True;
        class_insert += str(curClass)+" "+curClass.instructor+"\n";
        if int(curClass.crn) in Ben_Section:
            ben_open = True;
            sendBenMessage(class_insert);
        sendMessage(class_insert);
    class_insert = "Hey! These classes are open:\n\n";
            

