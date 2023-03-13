#include <iostream>
#include <algorithm> 
#include <string>  

class Passport 
{
   protected: 
   std::string fname; 
   int age;  
   int id;

   public:
   Passport():Passport("Ivanov_Ivan", 18, NULL){}
   Passport( std::string fnameP, int ageP, int idP) :fname{fnameP}, age{ageP}, id{idP} {} 

   void print()
   {
      std::cout<<"The name of person number "<<this->id<<" is "<<this->fname<<"\n"
               <<"and he is "<<this->age<<" years old\n"; 
   }

   ~Passport(){}
}; 

class Pas_Abroad : public Passport
{
    protected: 
    int abr_id; 
    std::string *visa; 
   public: 
   
   Pas_Abroad(int abr_id, std::string *visa, int n )
   {
      this->abr_id = abr_id;  

      visa = new std::string[n]; 
   int i=0; 

   while (i<n) {
   this->visa[i] = visa[i]; 
   i++; 
   }
   }

   void print()
   {
      std::cout<<"The name of person number "<<this->id<<" is "<<this->fname<<"\n"
               <<"and he is "<<this->age<<" years old\n"
               <<"also there is an abroad passport of his number "<<this->abr_id<<"\n";  
   }


}; 

int main()
{   
   int n; 
   std::cin>>n; 

    std::string visas[n];  
    int i=0; 
    while (i<n) {
    std::cin>>visas [i] ; 
   i++; 
   } 

   Passport bt("Bulba Taras", 50, 0000); 
   bt.print(); 


   Pas_Abroad vs(1111, visas, n); 
   vs.print();
}