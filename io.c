#include "io.h"

FILE * open_file(double * X, double * Y, double * Z, int nb_points) {
	FILE * fp;
	fp = fopen("./plt.py", "w+");
	fputs("from mpl_toolkits.mplot3d import Axes3D\n"
		  "import matplotlib.pyplot as plt\n"
		  "import numpy as np\n\n"
		  "fig = plt.figure()\n"
		  "ax = fig.add_subplot(111, projection='3d')\n\n", fp);
	int i;
	char num[6];
	fputs("X = [ ", fp);
	for (i = 0 ; i < nb_points ; i++) {
		snprintf (num, 6, "%lf", X[i]);
		fputs(num, fp);
		if (i < nb_points-1) {
			fputc(',', fp);
		}
	} fputs(" ]\n", fp);
	fputs("Y = [ ", fp);
	for (i = 0 ; i < nb_points ; i++) {
		snprintf (num, 6, "%lf", Y[i]);
		fputs(num, fp);
		if (i < nb_points-1) {
			fputc(',', fp);
		}
	} fputs(" ]\n", fp);
	fputs("Z = [ ", fp);
	for (i = 0 ; i < nb_points ; i++) {
		snprintf (num, 6, "%lf", Z[i]);
		fputs(num, fp);
		if (i < nb_points-1) {
			fputc(',', fp);
		}
	} fputs(" ]\n", fp);

	fputs("\nax.scatter(X, Y, Z, marker='o')\n\n", fp);
	
	return fp;
}

void write_step(FILE * fp, int step) {
	fputs("# STEP ", fp);
	char num[6];
	snprintf (num, 6, "%d", step);
	fputs(num, fp);
	fputc('\n', fp);
}

void write_init(FILE * fp, int i0, int i1, int i2, int color) {
	fputs("i, j, k = ", fp); 
	char num[6];
	snprintf (num, 6, "%d", i0);
	fputs(num, fp);
	fputs(", ", fp);
	snprintf (num, 6, "%d", i1);
	fputs(num, fp);
	fputs(", ", fp);
	snprintf (num, 6, "%d", i2);
	fputs(num, fp);
	fputc('\n', fp);
	if (color) {
		fputs("ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='b')\n"
			  "ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='b')\n"
			  "ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='b')\n\n", fp);
	}
	else {
		fputs("ax.plot([X[i], X[j]], [Y[i], Y[j]], [Z[i], Z[j]], color='orange')\n"
			  "ax.plot([X[i], X[k]], [Y[i], Y[k]], [Z[i], Z[k]], color='orange')\n"
			  "ax.plot([X[j], X[k]], [Y[j], Y[k]], [Z[j], Z[k]], color='orange')\n\n", fp);
	}
}

void write(FILE * fp, int i0, int i1, int i2, int i3, int color) {
	fputs("i, j, k, l = ", fp);
	char num[6];
	snprintf (num, 6, "%d", i0);
	fputs(num, fp);
	fputs(", ", fp);
	snprintf (num, 6, "%d", i1);
	fputs(num, fp);
	fputs(", ", fp);
	snprintf (num, 6, "%d", i2);
	fputs(num, fp);
	fputs(", ", fp);
	snprintf (num, 6, "%d", i3);
	fputs(num, fp);
	fputc('\n', fp);
	if (color) {
		fputs("ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='r')\n"
			  "ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='r')\n"
			  "ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='r')\n\n", fp);
	}
	else {
		fputs("ax.plot([X[l], X[i]], [Y[l], Y[i]], [Z[l], Z[i]], color='orange')\n"
			  "ax.plot([X[l], X[j]], [Y[l], Y[j]], [Z[l], Z[j]], color='orange')\n"
			  "ax.plot([X[l], X[k]], [Y[l], Y[k]], [Z[l], Z[k]], color='orange')\n\n", fp);
	}
}

void close_file(FILE * fp) {
	fputs("ax.set_xticks([])\n"
		  "ax.set_yticks([])\n"
		  "ax.set_zticks([])\n"
		  "ax.set_xlabel('X Label')\n"
		  "ax.set_ylabel('Y Label')\n"
		  "ax.set_zlabel('Z Label')\n\n"
		  "plt.show()\n", fp);
	fclose(fp);
}
