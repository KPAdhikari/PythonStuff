//To compile: gcc -o pointers_vs_reference pointers_vs_reference.c
//
//  I made this code to confirm for myself that 'reference' variables
//     are not valid in C. It was an addition to C++, so if we have
//     lines of code having to do with 'references', gcc will produce
//     errors, whereas g++ will compile that.
//
#include <stdio.h>

int main() {
  int i = 10;  //ordinary variable
  int *p = &i; //pointer variable that stores the address of 'i'

  //
  //If we try to compile it with gcc, with the following
  // line enabled, it will give us an error that says something like
  //    error: expected identifier or '('
  // This is because 'reference' variable is defined only in C++
  //
  int &r = i; //r is the reference (alias) to 'i'

  //printf("i=%d, *p = %d\n",i,*p);        //works with both gcc & g++
  printf("i=%d, *p = %d, r = %d\n",i,*p,r);//works only with g++


  return 0;
}
