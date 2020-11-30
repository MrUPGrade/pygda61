def setup():
    frameRate(10);
    background(255);
    size(1000, 1000, P3D);
    stroke(0, 0, 0, 20)
    fill(100, 50, 200, 20)


def draw():
    # background(255)
    ellipse(random(0, 1000), random(0, 1000), random(0, 1000),
            random(0, 1000))
    
