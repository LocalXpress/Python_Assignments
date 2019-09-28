#include <stdio.h>

int main(int argc, char const *argv[])
{
	float i;

	for (i = 0; i < 20; i = i + 0.5465)
	{
		printf("%f\n",i);
	}
	return 0;
}