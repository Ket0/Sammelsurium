// templateArgumentDeduction.cpp

#include <iostream>

// (1) Funktionstemplate
template <typename T>
void showMe(const T& t){
  std::cout << t << std::endl;
}

// (2) Klassentemplate
template <typename T>
struct ShowMe{
  ShowMe(const T& t){
    std::cout << t << std::endl;
  }
};

int main(){
  
  std::cout << std::endl;
    
  // Fall (1) Funktionstemplate
  // 
  // Template kann seine Temmplateargumente 
  // automatisch aus seinen Funktions-
  // argumenten ableiten
  // (auch vor C++17 moeglich)
  showMe(5.5);          // not showMe<double>(5.5);
  showMe(5);            // not showMe<int>(5);
  
  // Fall (2) Klassentemplate
  //
  // C++17 kann auch fuer Klassentemplates
  // sein Templateargument automatisch
  // ableiten
  ShowMe(5.5);          // not ShowMe<double>(5.5);
  ShowMe(5);            // not ShowMe<int>(5);
  
  std::cout << std::endl;
 
  // ENTER zum Programmbeenden
  std::cin.get();
  
 }
