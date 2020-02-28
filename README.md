# arpalert-howto
how to configure arpalert to notify by mail you about new devices on your network

**Steps:**
* _**installation:**_ \
sudo apt update\
sudo apt upgrade\
sudo apt install arpalert\
sudo apt install sendmail\
git clone https://github.com/illethrias/arpalert-howto.git

* _**configuration:**_\
_edit the python script to use your e-mail address_\
sudo cp ./arpalert-howto/arpwatch_mail.py /usr/local/bin/\
sudo chmod 755 /usr/local/bin/arpwatch_mail.py\
_edit config: /etc/arpalert/arpalert.conf:_\
``catch only arp = false``\
``action on detect = "/usr/local/bin/arpwatch_mail.py"``

follow rest of the documentation: https://www.arpalert.org/arpalert.html \
TLDR;
* once all devices on your network were seen, copy the file _/usr/local/arpalert/var/lib/arpalert/arpalert.leases_ into the maclist.allow file: \
 ``cat /usr/local/arpalert/var/lib/arpalert/arpalert.leases > /usr/local/arpalert/etc/arpalert/maclist.allow``