//Processing 3.5.4
//This program creates a canvas to draw circles onto, if the cricles are places near enough, they draw lines to form a network between them.

Node[] nodes = new Node[100];
int nodeCount = 0;

void setup() {
  size(600, 600);
  for (int i = 0; i < nodes.length; i++) {
    // Each element stores the same reference to the codes array
    nodes[i] = new Node(i, nodes);
  }
}

void draw() {
  background(0);
  for (int i = 0; i < nodeCount; i++) {
    nodes[i].display();
    nodes[i].displayNetwork(nodeCount);
  }
}

void mousePressed() {
  if (nodeCount < nodes.length) {
    nodes[nodeCount].setPosition();
    nodeCount++;
  }
}
