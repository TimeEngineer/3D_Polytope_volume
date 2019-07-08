#include <stdio.h>
#include <time.h>
#include "volume.h"

#define NB_POINTS_CUBE 8
#define NB_POINTS_FIGURE1 12

#define NB_POINTS_FIGURE2 30

int main() {
	time_t t;
	srand((unsigned) time(&t));

	// double X[NB_POINTS_CUBE] = { -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, 1.0, -1.0 };
	// double Y[NB_POINTS_CUBE] = { -1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, 1.0 };
	// double Z[NB_POINTS_CUBE] = { -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0 };
	// double vol0 = volume(X, Y, Z, NB_POINTS_CUBE);
	// printf("volume = %lf\n", vol0);

	// printf("\n------------------------------\n\n");
	
	// double X1[NB_POINTS_FIGURE1] = { -1.0, 0.5, 1.0, 0.5, -0.5, -1.0, -0.5, 0.5, 1.0, 0.5, -0.5, -0.5 };
	// double Y1[NB_POINTS_FIGURE1] = { 0.0, -1.0, 0.0, 1.0, 1.0, 0.0, -1.0, -1.0, 0.0, 1.0, 1.0, -1.0 };
	// double Z1[NB_POINTS_FIGURE1] = { -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0 };
	// double vol1 = volume(X1, Y1, Z1, NB_POINTS_FIGURE1);
	// printf("volume = %lf\n", vol1);

	double X2[NB_POINTS_FIGURE2];
	double Y2[NB_POINTS_FIGURE2];
	double Z2[NB_POINTS_FIGURE2];
	int i;
	for (i = 0 ; i < NB_POINTS_FIGURE2 ; i++) {
		X2[i] = ((double) rand()/RAND_MAX-0.5)*2;
		Y2[i] = ((double) rand()/RAND_MAX-0.5)*2;
		Z2[i] = ((double) rand()/RAND_MAX-0.5)*2;
		// printf("%lf %lf %f\n", X2[i], Y2[i], Z2[i]);
	}
	double vol2 = volume(X2, Y2, Z2, NB_POINTS_FIGURE2);
	printf("volume = %lf\n", vol2);

	return 0;
}