#ifndef _VOLUME_H_
#define _VOLUME_H_

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define MIN_DISTANCE 1e-15
#define DEBUG
#define PRINT

typedef struct ConvexHull {
	int i0;
	int i1;
	int i2;
	double n[4];
	struct ConvexHull * next;
} ConvexHull;

double volume(double * X, double * Y, double * Z, int nb_points);

#endif