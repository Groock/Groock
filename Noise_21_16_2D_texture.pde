//Processing 3.5.4
//Noise 2D texture
//This creates a static nosie texture

float xnoise = 0.0;
float ynoise = 0.0;
float inc = 0.4;

void setup() {
  size(700, 100);
  noLoop();
  noSmooth();
}

void draw() {
  background(0);
  for (int y = 0; y < height; y++) {
    for (int x = 0; x < width; x++) {
      float gray = noise(xnoise, ynoise) * 255;
      stroke(gray);
      point(x, y);
      xnoise = xnoise + inc;
    }
    xnoise = 0;
    ynoise = ynoise + inc;
  }
}
