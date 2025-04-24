//Processing 3.5.4
//This program creates small automata that move about the canvas to create randmozied colourful patterns on a loop, images included on the Github.
//group 1
float x = 900.0;
float y = 450.0;
float x2 = 1900.0;
float y2 = 999.0;
float x3 = 300.0;
float y3 = 300.0;
//group 2
float x4 = 900.0;
float y4 = 900.0;
float x5 = 900.0;
float y5 = 900.0;
float x6 = 900.0;
float y6 = 900.0;

int newx_co_neg = -10;
int newx_co_pos = 10;
int newy_co_neg = -10;
int newy_co_pos = 10;

// Snail trail number 1 colour vaiables
int st1col1 = 150;
int st1col2 = 150;
int st1col3 = 150;

void setup() {
  size (1900, 1000);
  //randomSeed(0); // Force the same random values
  background(0);
  noStroke();
}

void draw() {
  // Snail trail number 1
  if (x >= width) {
    x = 1;
  } else if (x <= 0) {
    x = width-1;
  } else {
    x += random(newx_co_neg, newx_co_pos); //Asign new x-coordinate
  }
  if (y >= height) {
    y = 1;
  } else if (y <= 0) {
    y = height-1;
  } else {
    y += random(newy_co_neg, newy_co_pos); //Assign new y-coordinate
  }
  // Colour selection
  fill((st1col1), (st1col2), (st1col3));
  
  //colour number 1
  if (st1col1 >= 270) {
    st1col1 = 1;
  } else if (st1col1 <= 0) {
    st1col1 = 269;
  }
  else {
    st1col1+= random(1,3);
  }
  
  //colour number 2
  if (st1col2 >= 270) {
    st1col2 = 1;
  } else if (st1col2 <= 0) {
    st1col2 = 269;
  }
  else {
    st1col2+= random(-3,3);
  }
  
  //colour number 3
  if (st1col3 >= 270) {
    st1col3 = 1;
  } else if (st1col3 <= 0) {
    st1col3 = 269;
  }
  else {
    st1col3+= random(-3,3);
  }
  
  // Shape selection
  ellipse(x, y, 20, 20);

  // Snail trail number 2
  if (x2 >= width) {
    x2 = 1;
  } else if (x2 <= 0) {
    x2 = width-1;
  } else {
    x2 += random(newx_co_neg, newx_co_pos); //Asign new x-coordinate
  }
  if (y2 >= height) {
    y2 = 1;
  } else if (y2 <= 0) {
    y2 = height-1;
  } else {
    y2 += random(newy_co_neg, newy_co_pos); //Assign new y-coordinate
  }
  // Colour selection
  fill(random(80, 200), 20, 60);
  // Shape selection
  ellipse(x2, y2, 10, 10);
  
  // Snail trail number 3
  if (x3 >= width) {
    x3 = 1;
  } else if (x3 <= 0) {
    x3 = width-1;
  } else {
    x3 += random(newx_co_neg, newx_co_pos); //Asign new x-coordinate
  }
  if (y3 >= height) {
    y3 = 1;
  } else if (y3 <= 0) {
    y3 = height-1;
  } else {
    y3 += random(newy_co_neg, newy_co_pos); //Assign new y-coordinate
  }
  // Colour selection
  fill(random(0, 255), random(0, 255), random(0, 255));
  // Shape selection
  ellipse(x3, y3, 8, 8);
  
  //group 2
  // Snail trail number 4
  if (x4 >= width) {
    x4 = 1;
  } else if (x4 <= 0) {
    x4 = width-1;
  } else {
    x4 += random(newx_co_neg, newx_co_pos); //Asign new x-coordinate
  }
  if (y4 >= height) {
    y4 = 1;
  } else if (y4 <= 0) {
    y4 = height-1;
  } else {
    y4 += random(newy_co_neg, newy_co_pos); //Assign new y-coordinate
  }
  // Colour selection
  fill(random(174, 190), random(200, 221), 60);
  // Shape selection
  ellipse(x4, y4, 6, 6);
  
  // Snail trail number 5
  if (x5 >= width) {
    x5 = 1;
  } else if (x5 <= 0) {
    x5 = width-1;
  } else {
    x5 += random(newx_co_neg, newx_co_pos); //Asign new x-coordinate
  }
  if (y5 >= height) {
    y5 = 1;
  } else if (y5 <= 0) {
    y5 = height-1;
  } else {
    y5 += random(newy_co_neg, newy_co_pos); //Assign new y-coordinate
  }
  // Colour selection
  fill(random(0, 255), random(0, 255), random(0, 255));
  // Shape selection
  ellipse(x5, y5, 6, 6);
  
  // Snail trail number 6
  if (x6 >= width) {
    x6 = 1;
  } else if (x6 <= 0) {
    x6 = width-1;
  } else {
    x6 += random(newx_co_neg, newx_co_pos); //Asign new x-coordinate
  }
  if (y6 >= height) {
    y6 = 1;
  } else if (y6 <= 0) {
    y6 = height-1;
  } else {
    y6 += random(newy_co_neg, newy_co_pos); //Assign new y-coordinate
  }
  // Colour selection
  fill(random(0, 255), random(0, 255), random(0, 255));
  // Shape selection
  ellipse(x6, y6, 6, 6);
}
