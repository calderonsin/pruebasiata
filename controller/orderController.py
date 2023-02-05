from datetime import date
def validateDate(fechapago:date):
    if fechapago.day % 2 == 0:
        return True
    else:
        return False

