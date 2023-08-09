// test.cpp
#include <iostream>
using namespace std;

// A simple class with a constructor and a destructor
class Test {
    public:
        Test() {
            cout << "Test object created" << endl;
        }
        ~Test() {
            cout << "Test object destroyed" << endl;
        }
};

// A function that takes a pointer to a Test object and casts it to an int pointer
void cast_test(Test* t) {
    // A C-style cast that converts the pointer type
    int* i = (int*)t;
    // A C++-style cast that does the same thing
    int* j = static_cast<int*>(t);
    // Print the addresses of the pointers
    cout << "Address of t: " << t << endl;
    cout << "Address of i: " << i << endl;
    cout << "Address of j: " << j << endl;
}

// The main function
int main() {
    // Create a Test object on the stack
    Test t;
    // Create a Test object on the heap
    Test* p = new Test();
    // Call the cast_test function with both objects
    cast_test(&t);
    cast_test(p);
    // Delete the heap object
    delete p;
    // Return 0
    return 0;
}
