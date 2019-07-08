#ifndef _IO_H_
#define _IO_H_

#include <stdio.h>

FILE * open_file();
void write_step(FILE * fp, int step);
void write_init(FILE * fp, int i0, int i1, int i2, int color);
void write(FILE * fp, int i0, int i1, int i2, int i3, int color);
void close_file(FILE * fp);

#endif