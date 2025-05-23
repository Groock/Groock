//processing 3.5.4
//This program creates a 9x9 box matrix on the canvas that you can use the mouse to rotate around.

void setup() {
  size(200, 200, P3D);
  noStroke();
}

void draw() {
  lights();
  background(0);
  translate(width/2, height/2, -height);
  float rz = map(mouseY, 0, height, 0, PI);
  float ry = map(mouseX, 0, width, 0, HALF_PI);
  rotateZ(rz);
  rotateY(ry);
  for (int y = -1; y <= 1; y++) {
    for (int x = -1; x <= 1; x++) {
      for (int z = -1; z <= 1; z++) {
        pushMatrix();
        translate(50*x, 50*y, -50*z);
        box(25);
        popMatrix();
      }
    }
  }
}
