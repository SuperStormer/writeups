#include <stdlib.h>
#include <stdio.h>

int main(){
	srand(0x539);
	int iVar1 = rand();
	int key = 0xcafebabe ^ (iVar1 + 0x1467f3U);
	printf("%d", key);
}
