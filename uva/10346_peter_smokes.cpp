#include <iostream>
using namespace std;

int smoke(int cigar, int tomake) {
  int butt = 0;
  int totalCigars = 0;

  int i = cigar;
  while (i >= tomake) {
    int made = i / tomake;
    int remain = i % tomake;
    i = made + remain;
    totalCigars += made*tomake;
  }
  totalCigars += i;

  return totalCigars;
}


int main() {

  int a,b;
  bool eof = false;
  cin >> a >> b;  

  while(!eof) {
    cout << smoke(a,b) << endl;
    cin >> a >> b;
    eof = cin.eof();
  }

  return 0;
}
