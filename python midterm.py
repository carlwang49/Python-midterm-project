import pyautogui, time, os 
import numpy as np

# Food order constants
BIITORO = 'biitoro' #ピートロ
TORIKAWA = 'torikawa' #鶏皮
TAN = 'tan' #タン
NEGIMA = 'negima' #ねぎま
SUNAGIMO = 'sunagimo' #すなぎも
KASHIRA = 'kashira'#カシラ
ERINGI = 'eringi' #エリンギ
ALL_ORDER_TYPES = (BIITORO, TORIKAWA, TAN, NEGIMA, SUNAGIMO, KASHIRA, ERINGI)

stick = np.array([False,False,False,False,False])
i = 0
count = 0
sub = 0

def main():
    """"game steps"""
    open_game()
    time.sleep(3)
    getGameRegion()
    start_game()
    time.sleep(2)
    set_coordinates()
    time.sleep(1.5)
    play_game()
       
"""repeat for get customer orders"""
def play_game():
    start_time = int(time.time())
    now = int(time.time()) 
    while (now - start_time < 500) :
        barbecue()
        time.sleep(6.7)
        delivery_food()
        time.sleep(0.2)
        now = int(time.time())

      

def imPath(filename):
    """A shortcut for joining the 'Takoyaki/'' file path"""
    return os.path.join('Takoyaki', filename)

def getGameRegion():
    """Obtains the region"""
    global GAME_REGION
    region = pyautogui.locateOnScreen(imPath('top_right_corner.png'))
    a1 = region[0] // 2
    b1 = region[1] // 2
    
    if region is None:
        raise Exception('Could not find game on screen. Is the game visible?')

    # calculate the region of the entire game
    topRightX = a1 + region[2] # left + width
    topRightY = b1 # top
    GAME_REGION = (topRightX - 640, topRightY, 640, 350)
    print(GAME_REGION)
    
    
def open_game():
    """"open the game"""
    pyautogui.moveTo(1440,0)
    pyautogui.moveTo(1345,12)
    pyautogui.click()
    pyautogui.typewrite('safari')
    pyautogui.press('enter')
    pyautogui.moveTo(687,50)
    pyautogui.click()
    pyautogui.typewrite('http://games.twtop.net/fgameplay.php?id=2424')
    pyautogui.press('enter')
    
def start_game():
    pos = pyautogui.locateCenterOnScreen(imPath('start_button.png'),confidence=0.5)
    x = pos[0] // 2
    y = pos[1] // 2
    print(x,y)
    pyautogui.click(x,y)

def set_coordinates():
    """set up all the button of its coordinates"""
    global BIITORO_COORDS, TORIKAWA_COORDS, TAN_COORDS, NEGIMA_COORDS, SUNAGIMO_COORDS, KASHIRA_COORDS, ERINGI_COORDS
    global STICK0_COORDS, STICK1_COORDS, STICK2_COORDS, STICK3_COORDS, STICK4_COORDS
    global PLATE0_COORDS,  PLATE1_COORDS, PLATE2_COORDS
    global CUSTORMER_1,CUSTORMER_2, CUSTORMER_3
 
    #food_coordinates
    BIITORO_COORDS = (GAME_REGION[0] + 75, GAME_REGION[1] + 207)
    TORIKAWA_COORDS = (GAME_REGION[0] + 75, GAME_REGION[1] + 241)
    TAN_COORDS = (GAME_REGION[0] + 75, GAME_REGION[1] + 275)
    NEGIMA_COORDS = (GAME_REGION[0] + 75, GAME_REGION[1] + 314)
    SUNAGIMO_COORDS = (GAME_REGION[0] + 490, GAME_REGION[1] + 224)
    KASHIRA_COORDS = (GAME_REGION[0] + 490, GAME_REGION[1] + 257)
    ERINGI_COORDS = (GAME_REGION[0] + 490, GAME_REGION[1] + 294)
    #stick_coordinates
    STICK0_COORDS = (GAME_REGION[0] + 149, GAME_REGION[1] + 338)
    STICK1_COORDS = (GAME_REGION[0] + 215, GAME_REGION[1] + 338)
    STICK2_COORDS = (GAME_REGION[0] + 280, GAME_REGION[1] + 338)
    STICK3_COORDS = (GAME_REGION[0] + 345, GAME_REGION[1] + 338)
    STICK4_COORDS = (GAME_REGION[0] + 412, GAME_REGION[1] + 338)
    #plate_coordinates
    PLATE0_COORDS = (GAME_REGION[0] + 135, GAME_REGION[1] + 154)
    PLATE1_COORDS = (GAME_REGION[0] + 285, GAME_REGION[1] + 154)
    PLATE2_COORDS = (GAME_REGION[0] + 440, GAME_REGION[1] + 154)
    #the position of custormershttp:
    CUSTORMER_1 = (GAME_REGION[0] + 50,  GAME_REGION[1], 680,1000)
    CUSTORMER_2 = (GAME_REGION[0] + 680, GAME_REGION[1], 620,1000)
    CUSTORMER_3 = (GAME_REGION[0] + 1000, GAME_REGION[1], 680,1000)

"""scope of customer postition"""
def order_position(customer) :     
    if customer == 0 :
        return CUSTORMER_1 
    elif customer == 1 :        
        return CUSTORMER_2
    elif customer == 2 :    
        return CUSTORMER_3
        
"""get the customer's orders"""        
def get_order():
    global sub
    orders = {}
    while True:
        for orderType in (ALL_ORDER_TYPES):
            allOrders = pyautogui.locateAllOnScreen(imPath('%s_order.png' % orderType), confidence=0.9,grayscale = True,region = order_position(sub))
            for order in allOrders:
                orders[order] = orderType     
        if len(orders) != 0 :
            sub = (sub + 1) % 3
            break 
        else :
            sub = (sub + 1) % 3
                                
                                     
    return orders

"""determine the postition of custormer """
def get_key(array):
    global key , count
    for x in (array):
        key = x[0]
        break
    key = key //  2
    if (410 < key < 570):
        count = 0
    elif(580 < key <720):
        count = 1
    elif(740 < key < 880):
        count = 2

"""barbecue function"""
def barbecue():
    current_orders = get_order()
    get_key(current_orders.keys())
    for x in current_orders.values():
        if x == BIITORO :
            pyautogui.moveTo(BIITORO_COORDS)
        elif x == TORIKAWA :
            pyautogui.moveTo(TORIKAWA_COORDS)
        elif x == TAN:
            pyautogui.moveTo(TAN_COORDS)   
        elif x == NEGIMA:
            pyautogui.moveTo(NEGIMA_COORDS)   
        elif x == SUNAGIMO:
            pyautogui.moveTo(SUNAGIMO_COORDS) 
        elif x == KASHIRA:
            pyautogui.moveTo(KASHIRA_COORDS)
        elif x == ERINGI:
            pyautogui.moveTo(ERINGI_COORDS)
        y = free_stick()
        z1 = stick_postion(y)
        pyautogui.dragTo(z1)
        stick[y] = True
    
"""determine the stick postion"""        
def stick_postion(x):
    if x == 0 :
        return STICK0_COORDS
    elif x == 1 :
        return STICK1_COORDS
    elif x == 2 :
        return STICK2_COORDS
    elif x == 3 :
        return STICK3_COORDS
    elif x == 4 :
        return STICK4_COORDS
    
"""determine the plate postion"""   
def plate_postion(x):
    if x == 0 :
        return PLATE0_COORDS
    elif x == 1 :
        return PLATE1_COORDS
    elif x == 2 :
        return PLATE2_COORDS
    
"""search for free stick"""
def free_stick():
    for i in range(4):
        if stick[i] == False:
            return i
        else:
            i = i + 1
            
"""delivery food to customers"""
def delivery_food():
    for i in range(4):
        if stick[i] == True:
            z2 = stick_postion(i)
            pyautogui.moveTo(z2)
            if (count == 0):
                pyautogui.dragTo(plate_postion(0))
            elif (count == 1):
                pyautogui.dragTo(plate_postion(1))
            elif (count == 2):
                pyautogui.dragTo(plate_postion(2))
            stick[i] = False
                
"""call main fuction"""
main()