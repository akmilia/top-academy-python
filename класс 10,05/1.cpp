#include <iostream> 
int main()  
{    
    int n = 455;    
     std::cout<<"Number "<< n<<"\n"; 
    int k=0;  
    int tmp=n; 
    while (tmp>0) 
    { 
        k++; 
        tmp = tmp/10; 
    }   

     std::cout<<"Length : "<<k<<"\n"; 
    int arr[k];  
   
    for (int i=0;  i<k; i++) 
    {    
         tmp  = n%10;  
        //   std::cout<<"tmp "<<tmp<<"\n"; 
         arr[i] =tmp;  
        //   std::cout<<"arr[i] "<<arr[i]<<"\n"; 
         n = n/10; 
    } 
  //arr = [ 1, 2, 1]
   int i = 0;  
   int j = k-1;   
   //j=2
   bool flag = true; 
   while (flag==true && i!=j) 
   { 
            if (arr[i] == arr[j]) 
            {   
                if (i+1!=j-1) 
                { 
                    i++; 
                    j--; 
                } 
                else  
                {     
                    flag = false;  
                      std::cout<<"Yap \n"; 
                     break; 
                }
               
            } 
            else  
            { flag = false;  
            std::cout<<"Error \n"; 
            break; }
    } 
  std::cout<<"Finished  \n"; 
}


