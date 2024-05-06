import random
import numpy as np
import pygame
import timeit
import sys
from collections import deque
from matplotlib import cm
sys.path.append('.')
from ripplecalculations import new_, new__

class RippleVisualizer:
    def __init__(self, ear):
        self.c = deque([])
        self.ear = ear
        self.fps = 80
        self.cols = 600
        self.rows = 600
        self.clock = pygame.time.Clock()
        self.dampening = 0.97
        self.TIME_PASSED_SECONDS = self.clock.tick(self.fps)
        self.frames = 0
        self.cm = cm.plasma
        self.colors = [list((255*np.array(self.cm(i))[:3]).astype(int)) for i in np.linspace(0,255,12000).astype(int)]
        # self.colors = self.colors[::-1]

    def start(self):
        self.screenrect = pygame.Rect(0,0,self.cols,self.rows)
        pygame.display.init()
        # self.screen = pygame.display.set_mode(self.screenrect.size, pygame.HWSURFACE, 32)
        self.screen = pygame.display.set_mode(self.screenrect.size)
        pygame.init()

        # self.current = numpy.zeros((self.cols,self.rows), dtype = numpy.float32)
        # self.previous = self.current.copy()
        # self.texture = pygame.image.load('background.jpg').convert()
        # self.texture = pygame.transform.smoothscale(self.texture, (self.cols, self.rows))
        # self.texture.set_colorkey((0, 0, 0, 0), pygame.RLEACCEL)
        # self.texture.set_alpha(None)
        # self.texture_array = pygame.surfarray.array3d(self.texture)
        # self.back_array = self.texture_array.copy()
        self._is_running = True
        # self.pulse()
        

    def pulse(self, v):
        # print(v)
        # self.current[self.cols//2,self.rows//2] = 8192
        # print(self.c)
        # print(self.ear.strongest_frequency)
        # print(len(self.colors))
        try:
            self.c.append([self.frames,self.colors[int(self.ear.strongest_frequency)] + [255]])
        except:
            print(int(self.ear.strongest_frequency))

    def copy(self, fromm, tom):
        for i in range(self.rows):
            for j in range(self.cols):
                tom[i][j] = fromm[i][j]

    def update(self):
        self.screen.fill((0,0,0,0))
        # if not self.frames % 3==0:
        #     self.frames+=1
        #     return
        # print(max(self.ear.fft))
        # print(self.ear.strongest_frequency)
        # print(numpy.log2(self.ear.strongest_frequency))
        # v = int(numpy.log2(self.ear.strongest_frequency))
        volume = self.ear.loudest
        # # print(volume)
        if volume > 10000:
            pygame.display.set_caption('Spectrum Analyzer -- (FFT-Peak: %05d Hz)' %self.ear.strongest_frequency)
            self.pulse(0)
        else:
            pygame.display.set_caption('No sounds detected')
        # # v = int(self.ear.strongest_frequency/200)
        # # if v==0:
        # #     v = 60
        # # m = 60/v
        # # if self.frames%m==0:
        # #     self.pulse(0)
        #     # self.pulse(volume)
        i = 0
        while i < len(self.c):
            if self.frames-self.c[i][0] > self.rows//2-30:
                self.c.popleft()
            else:
                # print(self.c[i][1])
                try:
                    pygame.draw.circle(self.screen, self.c[i][1], (self.rows//2,self.cols//2), self.frames-self.c[i][0], 1)
                except:
                    print(self.c[i][1])
                    raise ValueError("David did it again")
                i+=1
        pygame.display.update()
        # self.previous, self.current, self.back_array = new__(self.cols, self.rows, self.previous, self.current, self.texture_array, self.back_array)
        
        # # print(self.previous[self.rows//2][self.cols//2])
        # array = numpy.full((self.cols, self.rows, 3), 0)
        # copyarray = numpy.zeros((self.cols,self.rows))
        # self.copy(self.previous,copyarray)
        # array[:, :, :] = copyarray.reshape((self.cols, self.rows, 1))
        # numpy.putmask(array, array < 0, 0)
        
        # pygame.surfarray.blit_array(self.screen, array)

        # # print(self.previous[self.rows//2][self.cols//2])
        # # print(self.current[self.rows//2][self.cols//2])
        # # print(copyarray[self.rows//2][self.cols//2])

        # # self.screen.blit(pygame.surfarray.make_surface(self.back_array).convert(), (0, 0))
        # pygame.display.flip()

        self.frames+=1



