# Write your code here :-)
from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
from easyIO import *
import urequests

setScreenColor(0x222222)




label0 = M5TextBox(129, 88, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)


wifiCfg.doConnect('myaccesspoint', 'mypassword')
while True:
  label0.setText(str(digitalRead(36)))
  if (digitalRead(36)) == 1:
    req = urequests.get('https://maker.ifttt.com/trigger/open_window/with/key/gftZXYepmwf6fm1sz7ZxW4jT41O7hW2JxSJKIxpk0o_')

  wait_ms(2000)
