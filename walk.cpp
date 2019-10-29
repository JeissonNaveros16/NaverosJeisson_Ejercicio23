#include <iostream>
#include <random>
#include <stdlib.h>

int main(){
  float pi = 2.0*asin(1.0);
  float theta = 0.0;
  float x = 0.0;
  float y = 0.0; 
    
  srand48(8);

  while ((x*x + y*y)<10000){  
    theta = drand48()*2.0*pi;
    x = x + cos(theta);
    y = y + sin(theta);
    std::cout << x << " " << y << std::endl;
  }
  
  return 0;
}

