//Processing 3.5.4
//This program creates a noise texture image that animates on a loop.

float inc = 0.06;
int density = 4;
float znoise = 0.0;

void setup(){
  size (1000,1000);
  noStroke();
}
  
void draw() {
  float xnoise = 0.0;
  float ynoise = 0.0;
  for (int y = 0; y < height; y += density) {
    for (int x = 0; x < width; x += density) {
      float n = noise(xnoise, ynoise, znoise) * 255;
      fill(n);
      rect(y, x, density, density);
      xnoise += inc;
    }
    xnoise = 0.0;
    ynoise += inc;
  }
  znoise += inc;
}
