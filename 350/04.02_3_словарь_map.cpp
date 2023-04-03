// Написать программу формирования частотного словаря
// появления отдельных слов в некотором тексте. Обеспечить:
// 1. Чтение исходного текста из файла;
// 2. Вывод информации обо всех словах;
// 3. Вывод информации о наиболее часто встречающемся
// слове;
// 4. Запись результата в файл.


#include <iostream>
#include <map>
#include <algorithm> 
#include <fstream>
#include <string> 

void read_all_file(std::string name_file) {
    std::ifstream fin;

    fin.open(name_file);
    if (fin.is_open()) {

        while (fin.good()) {
            std::string line;

            std::getline(fin, line);
            std::cout << line << "\n";
        }
    } else {
        std::cout << "File not open!!!!\n";
    }
    fin.close();
}

using namespace std;
int main() {
    map <string, string> mp;
    
    cout << "Введите количество элементов: "; int n; cin >> n;
    string a; 
    string b;
    
    for (int i = 0; i < n; i++) {
        cout << i << ") ";  cin >> a;  cin >> b; 
        mp.operator[a] = b;  // добавляем новые элементы
    }

    map <string, string> :: iterator it = mp.begin();
    cout << "А вот все отсортированно: " << endl;
    for (int i = 0; it != mp.end(); it++, i++) {  // выводим их
        cout << i << ") Ключ " << it->first << ", значение " << it->second << endl;
    }
    
    std::cout << std::max_element(
   mp.cbegin(), 
   mp.cend(), 
   [](auto& i, auto& j) { return i.second < j.second; })->first;  
   

   read_all_file("name_file.txt"); 
   return 0;
}
