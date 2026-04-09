#include<iostream>

int main() {
   char name[20];
   int i; 
    gets(name);
    for(i=1; i<=4; i++) {
        printf("%s\n", name);
    }
    
    return 0;
}
