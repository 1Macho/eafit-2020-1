import mechanize
import log

def downloadSchedule(username, password):
    log.pushOrigin("Schedule downloader")
    log.printLogNormal("Loading Ulises login page.")
    br = mechanize.Browser()
    br.open("https://app.eafit.edu.co/ulises/login.do")
    br.select_form("loginForm")
    br.form["login"] = username
    br.form["clave"] = password
    loginResponse = br.submit()
    loginResponseText = loginResponse.read()
    if "Recuerde que debe ser el login y clave".encode() in loginResponseText:
        log.printLogError("Unable to log into Ulises.")
        log.popOrigin()
        return 0
    log.printLogNormal("Loading schedule page.")
    scheduleResponse = br.open("https://app.eafit.edu.co/ulises/consultas/consultaHorarios.do")
    log.popOrigin()
    return 1
