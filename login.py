from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from passes import username, password
import time

#Vi bruger modulet "pynput" til at simulere et tastetryk. 
#Vi opretter et "keyboard" objekt som en instans af "Controller()" funktionen.
from pynput.keyboard import Key, Controller
keyboard = Controller()

#Vi definerer en funktion, som simulerer et tryk af højre piletast
def nextSlide():
    keyboard.press(Key.right)
    keyboard.release(Key.right)

#Vi opretter et "driver" objekt som en instans af den indbyggede webdriver.
driver = webdriver.Firefox()

#Vi peger webdriveren til Google's login-skærm på Stackoverflow. 
driver.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A194f1fbfee5ebbc1%2C10%3A1603027434%2C16%3A00b098428e9842dc%2Cd85d9ab9b7cd183e7690bccc0e28d6337260352897174f4dafd18b8e237a31d5%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%228b87e68733bc4927ba09fc5cb1eb0d22%22%7D&response_type=code&flowName=GeneralOAuthFlow')

#Vi opretter et "id_box" objekt, som peger webdriveren til det ønskede felt.
id_box = driver.find_element_by_id('identifierId')

#Vi får webdriveren til at indsende brugernavn, som er gemt i "username" variablet.
id_box.send_keys(username)

#Vi peger webdriveren til det ønskede element og får den til at klikke.
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

#Vi sætter en kort forsinkelse for at lade siden indlæse.
time.sleep(3)

#Vi peger webdriveren til det ønskede element 
#og får den til at indsende kodeordet, som er gemt i "password" variablet.
driver.find_element_by_css_selector("input[type=password]").send_keys(password)

#Vi peger webdriveren til det ønskede element og får den til at klikke.
driver.find_element_by_id('passwordNext').click()

#Vi sætter en kort forsinkelse for at lade siden indlæse.
time.sleep(10)

#Vi peger webdriveren til vores Google Slides præsentation.
driver.get('https://docs.google.com/presentation/d/1iSVkMCQeMsxMs-fZ2DJxtQZs_ZuEzPiEUaaHWEFGxxg/edit#slide=id.p')

#Vi sætter en kort forsinkelse for at lade siden indlæse.
time.sleep(3)

#Vi peger webdriveren til det ønskede element og får den til at klikke.
driver.find_element_by_xpath('//*[@id="punch-start-presentation-left"]').click()

#Vi sætter en kort forsinkelse for at lade siden indlæse.
time.sleep(7)

#Vi kører vores funktion, som skifter til næste slide.
nextSlide()