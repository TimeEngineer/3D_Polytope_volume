#include <stdio.h>
#include <time.h>
#include <math.h>
#include "volume.h"

#define NB_POINTS_FIGURE0 8
#define NB_POINTS_FIGURE1 12
#define NB_POINTS_FIGURE2 1000
#define NB_POINTS_FIGURE3 10000
#define NB_POINTS_FIGURE4 10
#define NB_POINTS_FIGURE5 22
#define NB_POINTS_FIGURE6 27
// #define MEASURE

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

	printf("\n------------------------------\n\n");

	double X4[NB_POINTS_FIGURE4] = { 0.965, -0.824, -0.890, -0.867, -0.839, 0.966, -0.871, -0.921, -0.938, -1.000 };
	double Y4[NB_POINTS_FIGURE4] = { 0.999, -0.857, -0.807, -0.779, -0.770, 1.000, -1.000, -0.883, -0.709, -0.704 };
	double Z4[NB_POINTS_FIGURE4] = { 0.999, -0.831, -0.726, -0.833, -0.950, 1.000, -0.749, -0.648, -0.839, -0.684 };   

	#ifdef MEASURE
	clock_t begin = clock();
	#endif

	double vol4 = volume(X4, Y4, Z4, NB_POINTS_FIGURE4);

	#ifdef MEASURE
	clock_t end = clock();
	double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	printf("\ntime spent is : %.9lf\n", time_spent);
	#endif

	printf("volume = %lf\n", vol4);

	printf("\n------------------------------\n\n");

	double X5[NB_POINTS_FIGURE5] = { 0.824, 0.823, -0.809, -0.796, -0.688, -0.763, -0.714, 0.827, 0.827, -0.838, -0.866, -0.883, -0.933, 0.824, -0.898, 0.823, -0.829, 0.824, -0.955, -1.000, -0.967, -0.947 };
	double Y5[NB_POINTS_FIGURE5] = { 0.997, 0.996, -0.603, -0.682, -0.774, -0.538, -0.648, 1.000, 0.997, -0.812, -1.000, -0.706, -0.775, 0.997, -0.549, 0.999, -0.490, 1.000, -0.544, -0.444, -0.417, -0.585 };
	double Z5[NB_POINTS_FIGURE5] = { 0.997, 0.996, -0.767, -0.659, -0.812, -0.940, -0.855, 1.000, 0.997, -0.585, -0.611, -0.494, -0.423, 1.000, -0.666, 0.996, -0.861, 0.997, -0.526, -0.519, -0.621, -0.431 };

	#ifdef MEASURE
	clock_t begin = clock();
	#endif

	double vol5 = volume(X5, Y5, Z5, NB_POINTS_FIGURE5);

	#ifdef MEASURE
	clock_t end = clock();
	double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	printf("\ntime spent is : %.9lf\n", time_spent);
	#endif

	printf("volume = %lf\n", vol5);
	
	printf("\n------------------------------\n\n");

	double X6[NB_POINTS_FIGURE6] = { 0.695, -0.750, 0.692, 0.695, 0.698, 0.698, 0.698, 0.700, 0.700, 0.700, -0.843, 0.698, -0.749, 0.700, 0.693, 0.693, -1.000, 0.695, 0.693, 0.693, 0.695, 0.695, -0.965, 0.693, 0.693, 0.695, 0.693 };
	double Y6[NB_POINTS_FIGURE6] = { 0.995, -0.403, 0.992, 0.993, 0.993, 0.998, 0.995, 1.000, 0.995, 1.000, -0.823, 0.993, -1.000, 0.995, 0.993, 0.993, -0.969, 0.995, 0.995, 0.998, 0.998, 1.000, -0.318, 0.998, 0.998, 1.000, 0.995 };
	double Z6[NB_POINTS_FIGURE6] = { 0.995, -0.769, 0.993, 0.993, 0.993, 0.993, 0.993, 1.000, 0.995, 0.995, -0.469, 0.998, -0.655, 1.000, 0.995, 0.998, -0.333, 1.000, 0.993, 0.993, 0.993, 0.995, -0.386, 0.998, 0.995, 1.000, 0.998 };

	#ifdef MEASURE
	clock_t begin = clock();
	#endif

	double vol6 = volume(X6, Y6, Z6, NB_POINTS_FIGURE6);

	#ifdef MEASURE
	clock_t end = clock();
	double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	printf("\ntime spent is : %.9lf\n", time_spent);
	#endif

	printf("volume = %lf\n", vol6);

	return 0;
}