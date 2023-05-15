#include <iostream>  
#include <string> 

bool isspace (char c) 
{ 
    return c==' ' || c=='\n' ||  c=='\t'; 
} 

int count_w(const char * str, char sep) 
{   
    int count  = 0;  
    bool isSpace = true; 

   for (int i = 0; str[i] != '\0'; i++)
   {
    if (str[i]!=sep || !isspace(str[i])) 
    {   

        if (isSpace) 
        { 
            ++ count; 
             isSpace = false; 
        } 
        else 
        { 
            isSpace = true; 
        }
       
    } 
   } 

   return count; 
   
}

char** my_split( const char * str, char sep=' ') 
{    


    char ** split_str = new char * [count_w(str, sep) +1];

    char * tmp; 

//     for (int i = 0; str[i] != '\0'; ++i)
//     {
//         if (str[i]!=sep || !isspace(str[i])) 
//         { 
//             temp+=str[i]; 
//         } 

//         else if (!temp.empty()) 
//         { 
          
//                 result.push_back(temp); 
//                 temp= " ";
//         } 

//     }  

//     if (!temp.empty()) 
//     { 
//         result.push_back(temp); 
//     }
   
//    return result; 
    
}

int main()
{ 

}