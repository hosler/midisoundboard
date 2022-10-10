import rtmidi
import pygame

midiin = rtmidi.RtMidiIn()
pygame.init()
pygame.mixer.init()
music = pygame.mixer.Sound('solodanwhatever.mp3')

ports = range(midiin.getPortCount())
if ports:
    midiin.openPort(1)
    while True:
        m = midiin.getMessage(250) # some timeout in ms
        if m:
            if m.isNoteOn():
                music.stop()
                music.play()

