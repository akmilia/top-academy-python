
#include <iostream> 
#include <string> 
#include <fstream>  
#include <sstream>   
//у меня файл на 1.5 гб получился

class Person 
{
    protected: 
    std::string name;
    std::string owner;
    int number; 
    std::string adress;   
    std::string occupation;   

    public:
    Person() : name("Bereza"), owner("pole"), number(5100000), adress("Tisovaya, 3"), occupation ("wizard") {}  

    Person(std::string nameP, std::string ownerP, int numberP, std::string adressP, std::string occupationP ) : 
    name {nameP},   owner{ownerP},  number{numberP},  adress{adressP},  occupation{occupationP} {}   

    std::string & getname() {return this->name; }  
    std::string & getowner() {return this->owner; } 
    int & getnumb() {return this->number;}  
    std::string & getocup() {return this->occupation; }   


    ~Person() {}
}; 

class Guide: protected Person
{   
    protected: 
    Person *guid; 
    int size;
    int cap;  

    public:
    Guide(Person *guidP, int sizeP) : guid {guidP},   size{sizeP} 
    {   
        this->cap = this->size*2; 
        guid = new Person [this->cap]; 
        for (int i=0; i<this->size; ++i)
        this->guid[i] = guidP[i]; 
    }  

     void add_end(const Person& pers)  
    { 
        if (this->size+1 < this->cap) 
        { 
            this->size++; 
            this->guid[this->size] = Person(pers);
        } 
        else 
        std::cout<<"You are trying to do an impossible stuff/n"; 
        
    }  
   
    std::string show_all() const 
    {   
        std::stringstream buffer;
        for (int i=0; i<this->size; ++i)
        
       buffer<<i<<" person: "<<this->guid[i].getname()<<this->guid[i].getnumb()<<"who works as "<<this->guid[i].getocup()<<"\n";          
        return buffer.str(); 
    } 
    
    // std::ofstream show_all() const 
    // {   
    //      std::ofstream out; 
    //     for (int i=0; i<this->size; ++i)
    //     return i<<" person: "<<this->guid[i].getname()<<this->guid[i].getnumb()<<"who works as "<<this->guid[i].getocup()<<"\n";          
    // } 
 
    int by_name(std::string val) 
    { 
        for (int i=0; i<this->size; ++i) 
        if (this->guid[i].getname() == val) 
        return i;
        return -1;
    } 

    int by_owner(std::string val) 
    {
         for (int i=0; i<this->size; ++i) 
        if (this->guid[i].getowner() == val) 
        return i;
        return -1;
    } 

    int by_number(int val) 
    { 
         for (int i=0; i<this->size; ++i) 
        if (this->guid[i].getnumb() == val) 
        return i;
        return -1;
    }
  
    int by_occupation(std::string val)
    { 
         for (int i=0; i<this->size; ++i) 
        if (this->guid[i].getocup() == val) 
        return i;
        return -1;
    }  


  ~Guide( ) {  }
};

void write_in_file(std::string name_file, const Guide& g) 
{
    std::ofstream fout;

    fout.open(name_file); // перезпись в файл

    if (fout.is_open()) {
        while (fout.good()) {
                fout<<g.show_all()<< "\n";
            }
        }
     else {
        std::cout << "File not open!!!!\n";
    }

}

// void write()
//     std::ofstream out;          // поток для записи
//     out.open("D:\\hello.txt"); // окрываем файл для записи
//     if (out.is_open())
//     {
//         out << "Hello World!" << std::endl;
//     }
     
//     std::cout << "End of program" << std::endl;
//     return 0;
// }

// \\std::ofstream& << ("au.txt", std::ios::app, const Guide & g)
// {  
//     if (fout.is_open())
// {
//     out << g .<< std::endl;
// }
// out.close();        

//}


int main() 
{
   Person one("one", "chisla", 2500000, "Kazan", "fisher"); 
   Person two("two", "chisla", 250103156, "Kazan", "k-pop idol"); 
   Person three("three", "chisla", 89988989, "Mosc", "fisher"); 
   Person persons[3] = {one, two, three};  

   Guide guid (persons, 3);  
   guid.show_all(); 

   guid.add_end(Person("big bang", "korea", 000000, "cage", "oldskuli")); 

//    if(guid.by_name("three")!=-1) 
//    std::cout<<guid.[guid.by_name("three")].getname()<<"/n"; 
   
   write_in_file("au.txt", guid); 
}
 
