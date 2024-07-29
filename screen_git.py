# 最終更新日：2024/4/10
#  事前準備：Android Studio でエミュレータを起動
#            アプリを起動し、アップデートを確認


# メモ

# 引数を受け取るように設定
# プログラムの途中から実行できるようにする


def screenshot():
   import pyautogui
   import time
   time.sleep(2)
   pyautogui.moveTo(25,492)
   pyautogui.hotkey('command', 'shift','4')
   time.sleep(2)
   pyautogui.dragTo(319,250,1,button='left')
   time.sleep(2)
   #戻るボタン
   pyautogui.click(x=34, y=101)
   time.sleep(2)

def scroll(a,b):
   time.sleep(0.5)
   pyautogui.moveTo(c,a)
   time.sleep(1)
   pyautogui.dragTo(c,b,2,button='left')
   time.sleep(0.5)

import time
import pyautogui

#アプリを選択する
pyautogui.click(x=282, y=121)

c=100

#初期位置　最初にクリックするボタンのy座標
#1.Medetterenian Herbor
mede=229
#2.American Waterfront
amw=260
#3.Port Discovery
pd=367
#4.Lost River Delta
lostriver=306
#5.Arabian Coast
arab=280
#6.Mermaid Ragoon
merm=180
#7.Mysterious Ialand
mystery_=550

mede_down=573
mede_up=130
amw_down=605
amw_up=188
pd_down=600
pd_up=600-368
lostriver_down=600
lostriver_up=280
arab_down=600
arab_up=140
merm_down=500
merm_up=208


for i in range(156):
#1.メディテレニアンハーバー
   
   pyautogui.click(x=c, y=mede)
   screenshot()
   print('Venetian Gondolas')
   pyautogui.click(x=c, y=mede+71)
   screenshot()
   print('DisneySea Transit Steamer Line(Mediterranean Harbor)')
#   pyautogui.click(x=c, y=mede+71+71)
#   screenshot()
#   print('Fortress Explorations')
   pyautogui.click(x=c, y=mede+71+71+71)
   screenshot()
   print('The Leonardo Challenge')
   pyautogui.click(x=c, y=mede+71+71+71+71)
   screenshot()
   print('Soaring: Fantastic Flight')
   
   scroll(mede_down,mede_up)
   print('-----')
   time.sleep(5)
#2.アメリカンウォーターフロント
   pyautogui.click(x=c, y=amw)
   screenshot()
   print('Turtle Talk')
   pyautogui.click(x=c, y=amw+71)
   screenshot()
   print('Tower of Terror')
   pyautogui.click(x=c, y=amw+71+71)
   screenshot()
   print('DisneySea Electric Railway(American Waterfront)')
   pyautogui.click(x=c, y=amw+71+71+71)
   screenshot()
   print('DisneySea Transit Steamer Line(American Waterfront)')
#   pyautogui.click(x=c, y=amw+71+71+71+71)
#   screenshot()
#   print('Toy Story Mania!')
   pyautogui.click(x=c, y=amw+70+70+70+70+65)
   screenshot()
   print('Big City Vehicles')

   scroll(amw_down,amw_up)
   print('-----')
   time.sleep(5)
#3.ポートディスカバリー
   pyautogui.click(x=c, y=pd)
   screenshot()
   print('Aquatopia')
   #pyautogui.click(x=c, y=pd+71)
   #screenshot()
   #print('DisneySea Electric Railway(Port Discovery)')
   pyautogui.click(x=c, y=pd+71+71)
   screenshot()
   print('Nemo & Friends SeaRider')

   scroll(pd_down,pd_up)
   print('-----')
   time.sleep(5)
#4.ロストリバーデルタ
   pyautogui.click(x=c, y=lostriver)
   screenshot()
   print('Indiana Jones')
   #pyautogui.click(x=c, y=lostriver+71)
   #screenshot()
   #print('DisneySea Transit Steamer Line(Lost River Delta)')
# 休止中のため
#   pyautogui.click(x=c, y=lostriver+71+71)
#   screenshot()
#   print('Raging Spirits')

   scroll(lostriver_down,lostriver_up)
   print('-----')
   time.sleep(5)
#5.アラビアンコースト
   
   pyautogui.click(x=c, y=arab)
   screenshot()
   print('Caravan Carousel')
   pyautogui.click(x=c, y=arab+71)
   screenshot()
   print('Jasmines Flying Carpets')
   pyautogui.click(x=c, y=arab+71+71)
   screenshot()
   print('Sindbads Storybook Voyage')
   pyautogui.click(x=c, y=arab+71+71+71)
   screenshot()
   print('The Magic Lamp Theater')

   scroll(arab_down,arab_up)
   print('-----')
   time.sleep(5)
#6.マーメイドラグーン
   
   pyautogui.click(x=c, y=merm)
   screenshot()
   print('Ariels Playground')
   pyautogui.click(x=c, y=merm+71)
   screenshot()
   print('Jumpin Jellyfish')
   pyautogui.click(x=c, y=merm+71+71)
   screenshot()
   print('Scuttles Scooters')
   pyautogui.click(x=c, y=merm+71+71+71)
   screenshot()
   print('Flounders Flying Fish Coaster')
   pyautogui.click(x=c, y=merm+71+71+71+71)
   screenshot()
   print('Blowfish Balloon Race')
   #pyautogui.click(x=c, y=merm+71+71+71+71+71)
   #screenshot()
   #print('Mermaid Lagoon Theater')
   pyautogui.click(x=c, y=merm+71+71+71+71+71+71)
   screenshot()
   print('The Whirlpool')

   scroll(merm_down,merm_up)

   time.sleep(5)
#7.ミステリアスアイランド
   pyautogui.click(x=c, y=mystery_)
#   screenshot()
#####
   time.sleep(2)
   pyautogui.moveTo(25,592)
   pyautogui.hotkey('command', 'shift','4')
   time.sleep(2)
   pyautogui.dragTo(319,250,1,button='left')
   time.sleep(2)
   #戻るボタン
   pyautogui.click(x=34, y=101)
   time.sleep(2)

#####
   print('20,000 Leages Under the Sea')
   pyautogui.click(x=c, y=mystery_+71)
   screenshot()
   print('Journey to the Center of the Earth')

   for i in range(5):
      scroll(200,650)
