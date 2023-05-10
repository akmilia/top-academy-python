#include <iostream> 
#include <vector> 
int main()    
{   // типо уже перевернутые
     std::vector <int> a = {2, 0, 5, 1}; 
     std::vector <int> b = {9, 1, 1, 0};    
 
    int k =0;  
    int l =0; 

     if (a.size() <= b.size())  
     { 
      k = a.size();  
       l = b.size(); 
     }
    
     else   
     { 
         k = b.size();   
          l = a.size(); 
     }
     
     std::vector <int> res;
     

      int tmp=0;   
        int s=0; 
    for (int i = 0; i <k; i++)  
    {    
       
        if (a[i] + b [i] >9) 
        { 
            s = a[i] + b [i] - 10; 
        } 
        else   
        { 
             s = a[i] + b [i]; 
        } 
          
         res.push_back(s + tmp);  
          tmp=0;
         if ( s > 9) 
         { 
            tmp =1; 
         } 
        
         std::cout<<res[i]<<"\t";
    }  

     for (int i = k; i <l; i++)  
    {    
      res.push_back();  
    }

   std::cout<<"\n";
} 
 
