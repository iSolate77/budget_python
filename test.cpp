#include <iostream>

int transaction = 18;

void bar();
int foo(int);

int main(int argc, char *argv[])
{
    bar();
    foo(3);
    bar();
    return 0;
}

int foo(int a){
    a += 2;
    return a;
}

void bar(){
    std::cout << foo(transaction) << std::endl;
}
