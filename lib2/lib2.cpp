#include "lib2.h"
#include "lib1.h"
#include <stdio.h>


void B::function2()
{
	A a;
	a.function1();
	printf("function2\n");
}

