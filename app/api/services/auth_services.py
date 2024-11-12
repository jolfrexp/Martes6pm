def login(user:str,password:str,usuarios):
    i=0
    log =0 
    while i<len(usuarios):
        if user == usuarios[i].correo:
            if password == usuarios[i].contrasena:
                return i
        i=i+1
    return log
