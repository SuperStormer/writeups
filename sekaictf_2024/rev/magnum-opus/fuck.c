#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
  srand(time(0) + 2);
  for (int i = 0; i < 100; i++) {
    printf("%d ", rand() % 9);
  }
}
