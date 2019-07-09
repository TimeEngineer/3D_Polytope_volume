#include <stdio.h>
#include <time.h>
#include <math.h>
#include "volume.h"

#define NB_POINTS_FIGURE0 8
#define NB_POINTS_FIGURE1 12
#define NB_POINTS_FIGURE2 1000
#define NB_POINTS_FIGURE3 10000

#define MEASURE

int main() {
	int i;
	time_t t;
	srand((unsigned) time(&t));

	double X[NB_POINTS_FIGURE0] = { -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, 1.0, -1.0 };
	double Y[NB_POINTS_FIGURE0] = { -1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, 1.0 };
	double Z[NB_POINTS_FIGURE0] = { -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0 };
	
	#ifdef MEASURE
	clock_t begin = clock();
	#endif

	double vol0 = volume(X, Y, Z, NB_POINTS_FIGURE0);

	#ifdef MEASURE
	clock_t end = clock();
	double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	printf("\ntime spent is : %.9lf\n", time_spent);
	#endif

	printf("volume = %lf\n", vol0);

	printf("\n------------------------------\n\n");
	
	double X1[NB_POINTS_FIGURE1] = { -1.0, 0.5, 1.0, 0.5, -0.5, -1.0, -0.5, 0.5, 1.0, 0.5, -0.5, -0.5 };
	double Y1[NB_POINTS_FIGURE1] = { 0.0, -1.0, 0.0, 1.0, 1.0, 0.0, -1.0, -1.0, 0.0, 1.0, 1.0, -1.0 };
	double Z1[NB_POINTS_FIGURE1] = { -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0 };
	
	#ifdef MEASURE
	begin = clock();
	#endif

	double vol1 = volume(X1, Y1, Z1, NB_POINTS_FIGURE1);

	#ifdef MEASURE
	end = clock();
	time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	printf("\ntime spent is : %.9lf\n", time_spent);
	#endif

	printf("volume = %lf\n", vol1);

	printf("\n------------------------------\n\n");

	double X2[NB_POINTS_FIGURE2];
	double Y2[NB_POINTS_FIGURE2];
	double Z2[NB_POINTS_FIGURE2];
	for (i = 0 ; i < NB_POINTS_FIGURE2 ; i+= 4) {
		X2[i] = ((double) rand()/RAND_MAX-0.5)*2;
		double _a = X2[i] * X2[i];
		double _b = 1.0;
		Y2[i] = ((double) rand()/RAND_MAX) * (_b - _a);
		Y2[i] = sqrt(Y2[i]);
		Z2[i] = sqrt(1.0 - X2[i] * X2[i] - Y2[i] * Y2[i]);
		// printf("%lf\n", X2[i] * X2[i] + Y2[i] * Y2[i] + Z2[i] * Z2[i]);
		X2[i+1] = X2[i];
		Y2[i+1] = Y2[i];
		Z2[i+1] = -Z2[i];
		X2[i+2] = X2[i];
		Y2[i+2] = -Y2[i];
		Z2[i+2] = Z2[i];
		X2[i+3] = X2[i];
		Y2[i+3] = -Y2[i];
		Z2[i+3] = -Z2[i];
	}

	#ifdef MEASURE
	begin = clock();
	#endif
	
	double vol2 = volume(X2, Y2, Z2, NB_POINTS_FIGURE2);
	
	#ifdef MEASURE
	end = clock();
	time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	printf("\ntime spent is : %.9lf\n", time_spent);
	#endif

	printf("volume = %lf\n", vol2);

	printf("\n------------------------------\n\n");

	double X3[NB_POINTS_FIGURE3];
	double Y3[NB_POINTS_FIGURE3];
	double Z3[NB_POINTS_FIGURE3];
	for (i = 0 ; i < NB_POINTS_FIGURE3 ; i++) {
		X3[i] = ((double) rand()/RAND_MAX-0.5)*2;
		Y3[i] = ((double) rand()/RAND_MAX-0.5)*2;
		Z3[i] = ((double) rand()/RAND_MAX-0.5)*2;
	}

	#ifdef MEASURE
	begin = clock();
	#endif

	double vol3 = volume(X3, Y3, Z3, NB_POINTS_FIGURE3);

	#ifdef MEASURE
	end = clock();
	time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	printf("\ntime spent is : %.9lf\n", time_spent);
	#endif
	
	printf("volume = %lf\n", vol3);

	return 0;
}