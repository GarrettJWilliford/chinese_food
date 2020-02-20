from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os_uwu
import os

def driver_init(headless = True):
    if not headless:
        return webdriver.Firefox()
    fop = Options()
    fop.add_argument('--headless')
    fop.add_argument('--window_size1920x1080')
    return webdriver.Firefox(options = fop)

def remove_dupe(data):
    new_data = []
    for d in data:
        if d not in new_data:
            new_data.append(d)
    return new_data




def china_stix(driver):
    driver.get('https://order.mealkeyway.com/merchant/69334f3478633036422b434e66474f55496e687867773d3d/main')
    time.sleep(5)
    title = 'CHINA_STIX'
    order_menu = ['Chicken/Pork', 'Soup Store', 'Beefeoli', 'Nice', 'Shrimp People', \
                  'Vegetales',  "Kid Krap"]
    try:
        [d for d in driver.find_elements_by_tag_name('div') if d.get_attribute('innerHTML') == 'OK'][0].click()
        title = 'CHINA_STIX(OFFLINE)'
    except:
        pass
    
    while True:
        try:
            span = driver.find_elements_by_tag_name('span')
            span = [s for s in span if s.get_attribute('innerHTML') not in ['+', '', \
                        "©2019 MenuSifu.com. All Rights Reserved.", 'China Stix']]
            span = [s for s in span if list(s.get_attribute('innerHTML'))[0] != '<']
        except:
            continue
        os.system('clear')
        command = os_uwu.ui_template(title, ['Chicken/Pork', 'Soups', 'Beef', 'Fried Rice/Noodle', 'Shrimp People', \
                  'Vegetales',  "Kid Krap"])
        
        if command in [s.get_attribute('innerHTML') for s in span] or command == 'Sauce':
            
            [s for s in span if s.get_attribute('innerHTML') == command][0].click()
            menu_items = driver.find_elements_by_class_name('mainPage_itemName__25d01')
            
            if command == 'Chicken/Pork':
                chicken_pork = [m for m in menu_items if 'Chicken' in m.get_attribute('innerHTML') or \
                            'Pork' in m.get_attribute('innerHTML')]
                command = os_uwu.ui_template(command, [c.get_attribute('innerHTML') for c in chicken_pork])
                
            if command == 'Soups':
                soup = [m for m in menu_items if 'Soup' in m.get_attribute('innerHTML')]
                command = os_uwu.ui_template(command, [c.get_attribute('innerHTML') for c in soup])

            if command == 'Beef':
                beef = [m for m in menu_items if 'Beef' in m.get_attribute('innerHTML')]
                command = os_uwu.ui_template(command, [b.get_attribute('innerHTML') for b in beef])

            if command == 'Fried Rice/Noodle':
                noodle = [m for m in menu_items if 'Rice' in m.get_attribute('innerHTML') or \
                          'Noodle' in m.get_attribute('innerHTML') or m.get_attribute('innerHTML') == 'Lo Mein' or \
                          m.get_attribute('innerHTML') == 'Pad Thai']
                command = os_uwu.ui_template(command, [b.get_attribute('innerHTML') for b in noodle])

            if command == 'Shrimp':
                shrimp = [m for m in menu_items if 'Shrimp' in m.get_attribute('innerHTML')]
                command = os_uwu.ui_template(command, [s.get_attribute('innerHTML') for s in shrimp])

            if command == 'Vegetable':
                veg = [m for m in menu_items if 'Vegetable' in m.get_attribute('innerHTML') or \
                       'Tofu' in m.get_attribute('innerHTML') or 'Broccoli' in m.get_attribute('innerHTML') or \
                       'Mushroom' in m.get_attribute('innerHTML')]
                command = os_uwu.ui_template(command, [v.get_attribute('innerHTML') for v in veg])
                
            if command == "Kid's Corner":
                kid = [m for m in menu_items if 'Kid' in m.get_attribute('innerHTML')]
                command = os_uwu.ui_template(command, [k.get_attribute('innerHTML') for k in kid])
        command = input('Pick')
        try:
            [choice for choice in driver.find_elements_by_class_name('mainPage_itemName__25d01') if \
                   command in choice.get_attribute('innerHTML')][0].click()
            print([choice.get_attribute('innerHTML') for choice in driver.find_elements_by_class_name('mainPage_itemName__25d01') if command in choice.get_attribute('innerHTML')][0])
            driver.find_element_by_class_name('comboPanel_rmSubmitBnt__1JSbi').click()
            contin = input('<<|%s|>>_ADDED_TO_CART' % (command))
        except:
            er = input('error')
                

            

            














