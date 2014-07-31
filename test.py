import gpiocrust

with gpiocrust.Header() as header:
    shiny_led = gpiocrust.OutputPin(11)
    shiny_led.value = True