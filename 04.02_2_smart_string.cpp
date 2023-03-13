
// Тема: Строки и умные указатели
// Задание.
// Создайте пользовательские классы умных указателей.
// Один из классов должен повторять функциональность
// стандартного класса unique_ptr, а другой shared_ptr. Напишите код по тестированию ваших классов. 
#include <iostream>
using namespace std;
 
template<class T>
class my_unique_ptr {
    T* ptr;
public:
    my_unique_ptr() : ptr(nullptr) {}
    my_unique_ptr(const my_unique_ptr& sp) = delete; 

    my_unique_ptr(T* p) {
        ptr = p;
    }
   
    t& operator* () {
        return *ptr;
    }
 
    t* get() {
        return ptr;
    }
    void reset() {
        delete ptr;
        ptr = nullptr;
    }
    void release() {
        ptr = nullptr;
    }
    void swap(my_unique_ptr<t>& up) {
        std::swap(ptr, up.ptr);
    } 

     ~my_unique_ptr() {
        delete ptr;
    }
 
};
 
template<class T>
class my_shared_ptr {
    T* ptr = nullptr;
    size_t* count = nullptr;
public:
    my_shared_ptr() : ptr(nullptr), count(nullptr) {}
    my_shared_ptr(const my_shared_ptr& sp) {
        ptr = sp.ptr;
        count = sp.count;
        *count++;
    };
    my_shared_ptr(T* p) {
        ptr = p;
        count = new size_t(1);
    }
 
    ~my_shared_ptr() {
        if ((*count) > 1) {
            (*count)--;
            return;
        }
        delete ptr;
        delete count;
    }
 
    T& operator* () {
        return *ptr;
    }
    T* operator->() {
        return ptr;
    }
   
void operator= (my_shared_ptr<T>& up) {
        up.ptr = ptr;
        *(count)++;
    }

 
    T* get() {
        return ptr;
    }
    void reset() {
        delete ptr;
        ptr = nullptr;
    }
    void swap(my_shared_ptr<T>& up) {
        std::swap(ptr, up.ptr);
    }
    size_t use_count() {
        return *count;
    }
};
 
 
int main()
{
    
    shared_ptr<int> p(new int(5));
    shared_ptr<int> p2;
    cout << p.use_count() << "\n";
    p2 = p;
    cout << p.use_count() << "\n";
 
    shared_ptr<int> y;
    cout << p.use_count() << "\n";
    y = p2;
    cout << p.use_count() << "\n";
 
    
    my_shared_ptr<int> p3(new int(5));
    my_shared_ptr<int> p4;
    cout << p3.use_count() << "\n";
    p4 = p3;
    cout << p3.use_count() << "\n";
 
    my_shared_ptr<int> x;
    cout << p.use_count() << "\n";
    x = p4;
    cout << p3.use_count() << "\n";
 
    return 0;
}
