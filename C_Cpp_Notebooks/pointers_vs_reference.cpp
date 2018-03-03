//To compile: g++ -o pointers_vs_reference pointers_vs_reference.c
//
//
//
#include <stdio.h>
#include <iostream>

using namespace std;

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

  //In the following line, compiler will give error because
  //    references must be initialized and then cannot be reassigned thereafter
  //int &r2;

  //printf("i=%d, *p = %d\n",i,*p);        //works with both gcc & g++
  printf("i=%d, *p = %d, r = %d\n",i,*p,r);//works only with g++

  //printing addresses of all three
  cout<<"Addresses of i, p & r: "<<&i<<", "<<&p<<", "<<&r<<endl;
  cout<<"Values of i, p & r: "<<i<<", "<<p<<", "<<r<<endl;



  return 0;
}
