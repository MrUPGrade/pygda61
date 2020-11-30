t = 0
offset = 0.2

def setup():
    frameRate(60);
    background(0);
    size(1000, 1000, P3D);
    delay(100);


def draw():
    global t, offset
    # background(0)
    
    translate(width/2, height/2)
        
    colorMode(HSB, 100)
    strokeWeight(5)
        
    stroke(t%100, 100, 100, 90)
    line(x1(t), y1(t), x2(t), y2(t))
    
    t+= offset;
    

def x1(t):
  return sin(t) * 200


def y1(t):
  return cos(t) * 200


def x2(t):
  return sin(t) * 200 * -1


def y2(t):
  return cos(t) * 200 * -1
