#ifndef _VOLUME_H_
#define _VOLUME_H_

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "io.h"

// #define DEBUG
// #define PRINT
// #define PLOT
// #define INSIDE

typedef struct ConvexHull {
	int i0;
	int i1;
	int i2;
	double n[4];
	struct ConvexHull * next;
} ConvexHull;

double volume(double * X, double * Y, double * Z, int nb_points);

#endif