# 3D Polytope volume

This algorithm compute fastly the volume of a convex polytope through a set of points.

The header is as simple as that.

```C
typedef struct ConvexHull {
	int i0;
	int i1;
	int i2;
	double n[4];
	struct ConvexHull * next;
} ConvexHull;

double volume(double * X, double * Y, double * Z, int nb_points);
```

![alt text](https://github.com/TimeEngineer/Polytope_volume/blob/master/img/step0.PNG "step0")

![alt text](https://github.com/TimeEngineer/Polytope_volume/blob/master/img/step1.PNG "step1")

![alt text](https://github.com/TimeEngineer/Polytope_volume/blob/master/img/step2.PNG "step2")

![alt text](https://github.com/TimeEngineer/Polytope_volume/blob/master/img/step3.PNG "step3")

![alt text](https://github.com/TimeEngineer/Polytope_volume/blob/master/img/step4.PNG "step4")

![alt text](https://github.com/TimeEngineer/Polytope_volume/blob/master/img/step5.PNG "step5")

![alt text](https://github.com/TimeEngineer/Polytope_volume/blob/master/img/final.PNG "final")