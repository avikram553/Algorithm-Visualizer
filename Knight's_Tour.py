import pygame
from heapq import heappush, heappop # for priority queue
import random

#from ALGO.N_queen import *
N=10
0;dtime=300
pygame.init()
WIDTH=650;HEIGHT=650
block=WIDTH//N
win=pygame.display.set_mode((WIDTH,HEIGHT))
Q_HEIGHT=(block*3)//4;Q_WIDTH=(block*3)//4
knight_img= pygame.image.load('knight2.png') 
knight_img=pygame.transform.scale(knight_img,(Q_HEIGHT,Q_WIDTH))
WHITE=(255,255,255);BLACK=(0,0,0);RED=(255,0,0)
pygame.display.set_caption("KNIGHT'S TOUR")
x=block//2;y=block//2
x1=(block-Q_HEIGHT)//2
line_w=-int(-70//N)
win.fill((120,0,120))
k1=[1];k2=[];k3=[];k4=[]
class Knight():
    def __init__(self,v):
        self.n=v
        self.cb=[[0 for x in range(v)] for y in range(v)]
        self.ans=[]
    def grid(self):
        for i in range(self.n):
            for j in range(self.n):
                if([i,j] in self.ans):
                    color=(0,180,0)
                elif((i+j)%2==0):
                    color=WHITE
                else:
                    color=BLACK
                pygame.draw.rect(win,color,(i*block,j*block,block,block))
    def show(self):
        self.grid()
        xx,yy=self.ans[0]
        for i in range(1,len(self.ans)):
            tx,ty=self.ans[i]
            pygame.draw.line(win, (255,0,0), (x+xx*block,x+yy*block), (x+tx*block,x+ty*block),line_w)
            xx,yy=self.ans[i]
        win.blit(knight_img,(x1+xx*block,x1+yy*block))
        pygame.display.update()
        pygame.time.delay(dtime)
        
    def solve(self):
        print("start")
        kx = random.randint(0, self.n - 1)
        ky = random.randint(0, self.n - 1)
        dx = [-2, -1, 1, 2, -2, -1, 1, 2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        for k in range(self.n**2):
            self.cb[ky][kx] = k + 1
            self.ans.append([kx,ky])
            self.show()
            #print(self.ans)
            pq = [] # priority queue of available neighbors
            for i in range(8):
                nx = kx + dx[i]; ny = ky + dy[i]
                if 0<=nx<self.n and 0<=ny<self.n:
                    if self.cb[ny][nx] == 0:
                        # count the available neighbors of the neighbor
                        ctr = 0
                        for j in range(8):
                            ex = nx + dx[j]; ey = ny + dy[j]
                            if 0<=ex<self.n and 0<=ey<self.n:
                                if self.cb[ey][ex] == 0: ctr += 1
                        heappush(pq, (ctr, i))
            # move to the neighbor that has min number of available neighbors
            if len(pq) > 0:
                (p, m) = heappop(pq)
                kx += dx[m]; ky += dy[m]
            else:
                break
        #print(self.ans)
        return True
    
run=True
kn=Knight(N)
while(run):
    win.fill((0,0,0))
    execute=False
    pygame.time.delay(10)
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            run=False
    k=pygame.key.get_pressed()
    if(k[pygame.K_SPACE]):
        execute=True
    
    if(not execute):
        kn.grid()
        pygame.display.update() 
        continue

    kn.solve()
    pygame.time.delay(50000)    
    #break
    run=False

