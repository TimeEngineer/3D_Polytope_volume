#include "volume.h"

void print_convexhull(ConvexHull * ch) {
	ConvexHull * convexhull = ch;
	while (convexhull) {
		printf("(%d %d %d) ", convexhull->i0, convexhull->i1, convexhull->i2);
		convexhull = convexhull->next;
	} printf("\n");
}

/* build plane with normal n with 3 points */
void plane(double * X, double * Y, double * Z, int i0, int i1, int i2, double * n) {
	/* vectors */
	double _a0 = X[i1] - X[i0];
	double _a1 = Y[i1] - Y[i0];
	double _a2 = Z[i1] - Z[i0];
	double _b0 = X[i2] - X[i0];
	double _b1 = Y[i2] - Y[i0];
	double _b2 = Z[i2] - Z[i0];
	/* cross product */
	n[0] = _a1 * _b2 - _a2 * _b1; // a
	n[1] = _a2 * _b0 - _a0 * _b2; // b
	n[2] = _a0 * _b1 - _a1 * _b0; // c
	/* equation of plane: ax + by + cz + d = 0 */
	n[3] = - n[0] * X[i0] - n[1] * Y[i0] - n[2] * Z[i0]; // d
}

/* build plane with normal n oriented in the opposite direction of i3 */
void oriented_plane(double * X, double * Y, double * Z, int i0, int i1, int i2, int i3, double * n) {
	plane(X, Y, Z, i0, i1, i2, n);
	double _a0 = X[i0] - X[i3];
	double _a1 = Y[i0] - Y[i3];
	double _a2 = Z[i0] - Z[i3];
	double _dot = n[0] * _a0 + n[1] * _a1 + n[2] * _a2;
	n[0] *= _dot;
	n[1] *= _dot;
	n[2] *= _dot;
	n[3] *= _dot;
}

/* _a0 _b0 _c0 */
/* _a1 _b1 _c1 */
/* _a2 _b2 _c2 */
double volume_tetrahedron(double * X, double * Y, double * Z, int i0, int i1, int i2, int i3) {
	/* vectors */
	double _a0 = X[i1] - X[i0];
	double _a1 = Y[i1] - Y[i0];
	double _a2 = Z[i1] - Z[i0];
	double _b0 = X[i2] - X[i0];
	double _b1 = Y[i2] - Y[i0];
	double _b2 = Z[i2] - Z[i0];
	double _c0 = X[i3] - X[i0];
	double _c1 = Y[i3] - Y[i0];
	double _c2 = Z[i3] - Z[i0];
	/* determinant */
	double _det = _a0 * _b1 * _c2;
	_det += _b0 * _c1 * _a2;
	_det += _c0 * _a1 * _b2;
	_det -= _c0 * _b1 * _a2; 
	_det -= _b0 * _a1 * _c2;
	_det -= _a0 * _c1 * _b2;
	/* volume */
	return (_det < 0 ? -_det : _det)/6.0;
}

double distance_to_plane(double x, double y, double z, double * n) {
	return n[0] * x + n[1] * y + n[2] * z + n[3];
}

/* pop a triangle from the convex hull */
void pop(ConvexHull ** ch, ConvexHull * old) {
	if (*ch == old) {
		*ch = old->next;
	}
	else {
		ConvexHull * convexhull = *ch;
		while (convexhull->next != old) {
			convexhull = convexhull->next;
		}
		convexhull->next = convexhull->next->next;
	}
	free(old);
}

/* add a triangle to the convex hull */
void add_triangle(double * X, double * Y, double * Z, ConvexHull ** ch, int i0, int i1, int i2, int i3) {
	/* find the back of the convex hull */
	ConvexHull * convexhull = *ch;
	while (convexhull->next) {
		/* convex hull can't have twice the same triangle, this is an intersection, pop it ! */
		if (((convexhull->next->i0 == i0 && convexhull->next->i1 == i1) || (convexhull->next->i0 == i1 && convexhull->next->i1 == i0)) && convexhull->next->i2 == i2) {
			pop(ch, convexhull->next);
			return;
		}
		convexhull = convexhull->next;
	}
	/* build the new triangle */
	ConvexHull * ch_new = (ConvexHull *) malloc(sizeof(ConvexHull));
	ch_new->i0 = i0;
	ch_new->i1 = i1;
	ch_new->i2 = i2;
	oriented_plane(X, Y, Z, i0, i1, i2, i3, ch_new->n);
	ch_new->next = NULL;
	/* link the new triangle */
	convexhull->next = ch_new;
}

/* build a tetrahedron */
ConvexHull * new_convexhull(double * X, double * Y, double * Z, int i0, int i1, int i2, int i3) {
	ConvexHull * ch = (ConvexHull *) malloc(sizeof(ConvexHull));
	ch->i0 = i0;
	ch->i1 = i1;
	ch->i2 = i2;
	oriented_plane(X, Y, Z, i0, i1, i2, i3, ch->n);
	ch->next = NULL;
	/* minimal convex hull is tetrahedron */
	add_triangle(X, Y, Z, &ch, i0, i1, i3, i2);
	add_triangle(X, Y, Z, &ch, i0, i2, i3, i1);
	add_triangle(X, Y, Z, &ch, i1, i2, i3, i0);
	return ch;
}

/* find the farthest point upper the first triangle */
int farthest_point(double * X, double * Y, double * Z, int nb_points, ConvexHull ** ch, int * list_points, FILE * fp) {
	int i;
	
	#ifdef DEBUG
	printf("\nAvailable points [ ");
	for (i = 0 ; i < nb_points ; i++) {
		printf("%d ", list_points[i]);
	} printf("]\n\n");
	#endif

	int max = -1;
	double distance_max = 0.0;
	/* iterate over all surface of the convex hull */
	ConvexHull * convexhull = *ch;
	while (convexhull) {
		for (i = 0 ; i < nb_points ; i++) {
			/* check if the point is not used */
			if (list_points[i]) {
				double distance = distance_to_plane(X[i], Y[i], Z[i], convexhull->n);
				/* check if the distance is greater than the max */
				if (distance > distance_max) {
					distance_max = distance;
					max = i;
				}
			}
		}
		/* check if a maximum is found for this triangle */
		if (max != -1) {
			return max;	
		}
		/* else there is no point on this side, pop this triangle for performance */
		else {
			ConvexHull * temp = convexhull;
			convexhull = convexhull->next;

			#ifdef PLOT
			write_init(fp, temp->i0, temp->i1, temp->i2, 1);
			#endif

			pop(ch, temp);
		}
	}
	return -1;
}

/* try to expand the convex hull with a point */
void expand(double * X, double * Y, double * Z, int nb_points, ConvexHull ** ch, int index, int * list_points, double * vol, FILE * fp) {
	/* mark this point as used */
	list_points[index] = 0;
	/* iterate over triangles to merge a larger convex hull */
	ConvexHull * convexhull = *ch;
	while (convexhull) {
		double distance = distance_to_plane(X[index], Y[index], Z[index], convexhull->n);
		/* 1e-15 is a threshold to avoid imprecision */
		if (distance > 1e-15 && convexhull->i2 != index) {
			/* sum the volume of the created tetrahedron */
			double v = volume_tetrahedron(X, Y, Z, convexhull->i0, convexhull->i1, convexhull->i2, index);
			*vol += v;

			#ifdef INSIDE
			write(fp, convexhull->i0, convexhull->i1, convexhull->i2, index, 1);
			#endif

			/* build the new tetrahedron */
			add_triangle(X, Y, Z, &convexhull, convexhull->i0, convexhull->i1, index, convexhull->i2);
			add_triangle(X, Y, Z, &convexhull, convexhull->i0, convexhull->i2, index, convexhull->i1);
			add_triangle(X, Y, Z, &convexhull, convexhull->i1, convexhull->i2, index, convexhull->i0);
			
			/* pop the used triangle */
			ConvexHull * temp = convexhull;
			convexhull = convexhull->next;
			pop(ch, temp);
		}
		else {
			convexhull = convexhull->next;
		}
	}
}

/* initialize 4 points for our first tetrahedron */
void init(double * X, double * Y, double * Z, int nb_points, int * i0, int * i1, int * i2, int * i3, int * list_points) {
	int i;
	double max_x = X[0], min_x = X[0];
	double max_y = Y[0], min_y = Y[0];
	double max_z = Z[0], min_z = Z[0];

	int index_max_x = 0, index_min_x = 0;
	int index_max_y = 0, index_min_y = 0;
	int index_max_z = 0, index_min_z = 0;
	
	for (i = 0 ; i < nb_points ; i++) {
		if (X[i] > max_x) {
			max_x = X[i];
			index_max_x = i;
		}
		if (X[i] < min_x) {
			min_x = X[i];
			index_min_x = i;
		}
		if (Y[i] > max_y) {
			max_y = Y[i];
			index_max_y = i;
		}
		if (Y[i] < min_y) {
			min_y = Y[i];
			index_min_y = i;
		}
		if (Z[i] > max_z) {
			max_z = Z[i];
			index_max_z = i;
		}
		if (Z[i] < min_z) {
			min_z = Z[i];
			index_min_z = i;
		}
	}

	if (index_max_x != index_min_x) {
		*i0 = index_max_x;
		*i1 = index_min_x;
	}
	else if (index_max_y != index_min_y) {
		*i0 = index_max_y;
		*i1 = index_min_y;	
	}
	else if (index_max_z != index_min_z) {
		*i0 = index_max_z;
		*i1 = index_min_z;
	}

	for (i = 0 ; i < nb_points ; i++) {
		if (i != *i0 && i != *i1) {
			*i2 = i;
			break;
		}
	}
	if (*i0 == *i1 || *i0 == *i2 || *i1 == *i2) {
		printf("Abort: no plane\n");
		exit(1);
	}

	double n[4];
	plane(X, Y, Z, *i0, *i1, *i2, n);

	double distance_max = -1.0;
	int index_max = -1;
	for (i = 0 ; i < nb_points ; i++) {
		if (i != *i0 && i != *i1 && i != *i2) {
			list_points[i] = 1;
			double distance = distance_to_plane(X[i], Y[i], Z[i], n);
			distance = distance < 0 ? -distance : distance;
			if (distance > distance_max) {
				distance_max = distance;
				index_max = i;
			}
		}
		else {
			list_points[i] = 0;
		}
	}

	list_points[index_max] = 0;

	#ifdef PRINT
	printf("max_x = %.2lf min_x = %.2lf\n", max_x, min_x);
	printf("max_y = %.2lf min_y = %.2lf\n", max_y, min_y);
	printf("max_z = %.2lf min_z = %.2lf\n", max_z, min_z);
	printf("(i0, i1, i2, i3) = (%d, %d, %d, %d)\n", index_max_x, index_min_x, *i2, index_max);
	#endif

	*i3 = index_max;

	if (*i3 == -1) {
		printf("Abort: no volume\n");
		exit(1);	
	}
}

/* find the volume of a polytope described by a cloud of points */
double volume(double * X, double * Y, double * Z, int nb_points) {
	/* 4 points are needed to get a 3D convex hull */
	if (nb_points < 4) {
		printf("Abort: 4 points are needed\n");
		return -1;
	}

	int list_points[nb_points];
	int i0, i1, i2, i3;
	init(X, Y, Z, nb_points, &i0, &i1, &i2, &i3, list_points);

	#ifdef PLOT
	FILE * fp = open_file(X, Y, Z, nb_points);
	int i = 0;
	write_step(fp, i);
	write_init(fp, i0, i1, i2, 0);
	write(fp, i0, i1, i2, i3, 0);
	#endif

	#ifndef PLOT
	FILE * fp = NULL;
	#endif

	/* initialize the first tetrahedron */
	ConvexHull * ch = new_convexhull(X, Y, Z, i0, i1, i2, i3);
	double vol = volume_tetrahedron(X, Y, Z, i0, i1, i2, i3);
	int index = farthest_point(X, Y, Z, nb_points, &ch, list_points, fp);
	
	#ifdef DEBUG
	print_convexhull(ch);
	#endif

	/* while it is growable */
	while (index != -1) {
		#ifdef DEBUG
		printf("adding %d ...\n", index);
		#endif

		#ifdef PLOT
		i++;
		write_step(fp, i);
		#endif

		/* expand the convex hull */
		expand(X, Y, Z, nb_points, &ch, index, list_points, &vol, fp);
		
		#ifdef DEBUG
		print_convexhull(ch);
		#endif

		index = farthest_point(X, Y, Z, nb_points, &ch, list_points, fp);
	}

	#ifdef PLOT
	close_file(fp);
	#endif

	return vol;
}