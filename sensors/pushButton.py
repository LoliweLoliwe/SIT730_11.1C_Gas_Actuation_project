from gpiozero import Button

gasBtn = Button(4)      # The number of the pushbutton pin
try:
    print("WE ASSUME THERE IS A LEAK, ...")
    print("...Press the button!")
    while not gasBtn.is_pressed:
        # if the button is not pressed nothing will happen
        pass
    # after the button is pressed
    with open('object_ident_4.py', 'r') as file:
        code = file.read()
        exec(code)

except KeyboardInterrupt:
    exit()
