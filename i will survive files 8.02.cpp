#include <fstream> 
#include <iostream> 
#include <string>
using namespace std; 

string read_all_file(const string &filename) // const & - read only
{
    ifstream fin(filename); 
    string result; 

    if (fin.good())
    {   
        string tmp_line;
        while (fin.good())
        {
            getline(fin, tmp_line); 
            result+=tmp_line+"\n"; 
        }
    } 
    else 
    {
        cout<<"Error reading file\n";
    }
    return result; 
} 

string diff_texts(const string &t1, const string &t2)
{
    int n_char = 0; 
    int n_line = 0 ; 
    string result ="";

    while(t1[n_char] !='\0' && t2[n_char]!='\0')
    {    
        if (t1[n_char]!=t2[n_char])
        { 
            cout<<"Error, the files are different\n"; 
            while (t1[n_line]!='\n')
            {
                result+=t1[n_line];
            }
            
            break;
        } 
        n_char++; 
        if(t1[n_char] =='\n') 
        {
            n_line= n_char + 1;

        }
    } 
    cout<<"count chars:"<<n_char; 
    return result; 
} 
int main(int argc, char* argv[])
{   
    /* 
    //общая практика
    ofstream fout("cppstudio.txt"); // создаём объект класса ofstream для записи и связываем его с файлом cppstudio.txt
    fout << "Работа с файлами в С++"; // запись строки в файл
    fout.close(); // закрываем файл
    
    char buff[50];

    ifstream fin("cppstudio.txt"); // создаём объект класса ifstream для чтения и связываем его с файлом cppstudio.txt
    fin.getline(buff, 50); 
    fin.close(); 
    cout<<buff<<endl; 
    */
    
    string text1;
    string text2; 
    string tmp_name; 
    
    cout<<"Enter text1"; 
    cin>>tmp_name; 
    

    cout<<"Enter text2"; 
    cin>>tmp_name;  

    text1 = read_all_file(tmp_name); 
    text2 = read_all_file(tmp_name);  

    cout<<diff_texts(text1, text2)<<"\n";
    

}