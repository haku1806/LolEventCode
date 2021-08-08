import requests, re, time, os, ctypes, sys
import autoit
import pyautogui
import match

reg = r"LOL[A-Z0-9]{10}"
post = input("post: ")
access_token = ""
# access_token = input("token: ")

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

# Su dung autoit
def redeem(code):
    point_extended = 50
    # Check client LOL exists
    autoit.win_activate('League of Legends')
    time.sleep(0.5)
    # Input code
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("screenshot.png")
    point_x, point_y  = match.bypass_captcha('.\\images\\code.PNG', 'screenshot.png')
    autoit.mouse_click('left', point_x+point_extended, point_y+point_extended)
    time.sleep(0.5)
    autoit.send("^a")
    autoit.send(code)
    os.remove("screenshot.png")
    
    # Click submit
    # autoit.mouse_click('left', 1094+point_x, 710+point_y)
    autoit.send('{ENTER}')
    time.sleep(0.5)
    
    point_extended_x = 155
    point_extended_y = 30
    # Check if error code
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("screenshot.png")
    point_x, point_y  = match.bypass_captcha('.\\images\\error_code.PNG', 'screenshot.png')
    autoit.mouse_click('left', point_x+point_extended_x, point_y+point_extended_y)
    autoit.mouse_move(point_x+point_extended_x+100, point_y+point_extended_y+100)
    os.remove("screenshot.png")
    
    # Click OK
    time.sleep(2)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("screenshot.png")
    point_x, point_y  = match.bypass_captcha('.\\images\\error_code.PNG', 'screenshot.png')
    # if (point_x > 800):     
    autoit.mouse_click('left', point_x+point_extended_x, point_y+point_extended_y)
    autoit.mouse_move(point_x+point_extended_x+100, point_y+point_extended_y+100)
    os.remove("screenshot.png") 
        
    # Click OK 2
    time.sleep(2)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("screenshot.png")
    point_x, point_y  = match.bypass_captcha('.\\images\\error_code.PNG', 'screenshot.png')
    autoit.mouse_click('left', point_x+point_extended_x, point_y+point_extended_y)
    autoit.mouse_move(point_x+point_extended_x+100, point_y+point_extended_y+100)
    os.remove("screenshot.png")
    
def main():
    code = ''
    count = 0
    if not isAdmin():
            print('Please run as admin!')
            sys.exit(0)
            
    while True:                  
        # get lastest comment from graph api
        r = requests.get(f"https://graph.facebook.com/{post}/comments?order=reverse_chronological&access_token={access_token}&limit=1")
        cmt = r.json()['data'][0]['message']
        # regex & split LOL Code
        rs = re.findall(reg, cmt)
        if (len(rs) > 0):
            # check if code is new code
            if ("LOL" + rs[0] != code):
                count += 1
                print("STT: " + str(count) + "\t| " + rs[0])
                code = rs[0]
                redeem(code)
            
if __name__ == "__main__":
    main()