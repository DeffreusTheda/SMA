#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEFAULT_LEN 30
#define MAX 99

int main(int argc, char* argv[]) {
  printf("%s!\n", argv[0]);
	int len = ( argc > 1 ) ? atoi(argv[1]) : DEFAULT_LEN ;
	int unsorted[len];
	srand(time(NULL));

	printf("Unsorted : ");
	for ( int i = 0; i < len; ++i ) {
		unsorted[i] = rand() % (MAX + 1);
		printf("%2d ", unsorted[i]);
	}
	printf("\n");

	clock_t start_time = clock();
	for ( int i = 0; i < len - 1; i++ ) {
		int min_idx = i;

		for ( int j = i + 1; j < len; j++ )
			if ( unsorted[j] < unsorted[min_idx] )
				min_idx = j;

		if (min_idx != i) {
			int temp = unsorted[i];
			unsorted[i] = unsorted[min_idx];
			unsorted[min_idx] = temp;
  	}
	}
	clock_t end_time = clock();

	printf("Sorted   : ");
	for ( int i = 0; i < len; ++i )
			printf("%2d ", unsorted[i]);
	printf("\n");

	printf("Time     : %f second\n", (double)(end_time - start_time) / CLOCKS_PER_SEC);

	for ( int i = 0; i < len - 1; ++i )
		if ( unsorted[i] > unsorted[i+1] ) {
			printf("Check    : Incorrect!\n");
			exit(1);
		}
	printf("Check    : Correct\n");
	exit(0);
}
