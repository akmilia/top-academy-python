#include <iostream> 
#include <string>

class Passport
{
    protected: 
    std::string name; 
    std::string surname; 
    std::string country; 
    char date[8]; 

   public:  
    Passport(): Passport("Ivan", "Ivanov", "Russia", "12.12.12"){}
    Passport(std::string nameP, std::string surnameP, std::string countryP, char *dateP): name{nameP}, surname{surnameP}, country{countryP}, date{*dateP} {} 
    
   

    ~Passport(){}
};  

class ForeignPassport : Passport
{
    protected: 
    
};
int main()
{

}