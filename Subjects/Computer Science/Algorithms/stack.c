#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define MAXSIZE 8

int stack[MAXSIZE];
int top = -1;

int pop(){
  return ( top != -1 ) ? stack[top--] : printf("Could not retrieve data, Stack is empty.\n");
}

int push(int data){
  return ( top != MAXSIZE ) ? stack[++top] = data : printf("Could not insert data, Stack is full.\n");
}

int main(){
  srand(time(NULL));
  for ( int i = 0; i < MAXSIZE; ++i )
    push(rand() % 101);
  printf("Stack Elements: ");

  for ( int i = 0; i < MAXSIZE; ++i )
    printf("%d ", stack[i]);

  printf("\nElements popped: ");

  while ( top != -1 )
     printf("%d ", pop());

  return 0;
}
