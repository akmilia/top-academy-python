#include <iostream>  
#include <vector>  
#include <string> 

bool isspace (char c) 
{ 
    return c==' ' || c=='\n' ||  c=='\t'; 
}

std::vector<std::string> my_split(std::string str, char sep=' ') 
{  
    std::vector<std::string>  result; 
   std::string temp =""; 
    for (int i = 0; str[i] != '\0'; ++i)
    {
        if (str[i]!=sep || !isspace(str[i])) 
        { 
            temp+=str[i]; 
        } 

        else if (!temp.empty()) 
        { 
          
                result.push_back(temp); 
                temp= " ";
        } 

    }  

    if (!temp.empty()) 
    { 
        result.push_back(temp); 
    }
   
   return result; 
    
}

int main()
{ 
   std::string str = "Her name is Alice! She is"; 

   auto split_test = my_split(str);  

   for (auto i = split_test.begin(); i != split_test.end(); i++)
   {
   std::cout<<*i<<"\n"; 
   }
   return 0; 

}