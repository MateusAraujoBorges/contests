#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

struct record {
  int pos;
  string val;
};

bool compareRecords(record r1, record r2) {
  //cout << "comparing pos " << r1.pos << " and " << r2.pos << endl;
  return r1.pos < r2.pos;
}

vector<record> process() {
  //  cout << "entering method" << endl;
  vector<record> vec;
  string positions = " ";
  getline(cin,positions);
    //cout << positions << "aaa"<< endl;
  //extract positions from string
  stringstream ss(positions);
  int pos;
  
  while(!ss.eof()) {
	ss >> pos;
	record r;
	r.pos = pos;
	vec.push_back(r);
		//cout << "stored pos:" << r.pos << endl;
  }

  //extract values from string
  getline(cin,positions);
  stringstream zz(positions);
  string value;

  vector<record>::iterator it = vec.begin();
    //cout << positions << "aaa"<< endl;
  while(!zz.eof()) {
	zz >> value;
	it->val = value;
	//cout << "stored val:" << (*it).val  << " with pos:" << (*it).pos << endl;
	it++;
  }
    //cout << "endmethod: vec size = " << vec.size() << endl;
  return vec;
}

int main() {
  int ncases;
  cin >> ncases;
  //  cout <<ncases <<endl;

  string dummy;
  getline(cin,dummy); //remove empty lines
  for(int i = 0; i < ncases; i++) {
	getline(cin,dummy); //remove empty lines

	vector<record> vec = (process());
	//	cout << "back to front" <<endl;
	//	cout << "sss" << (vec.size()) << endl;
	sort(vec.begin(),vec.end(),compareRecords);
	vector<record>::iterator it;
	for(it = vec.begin();it < vec.end();it++) {
	  record r = *it;
	  string val = r.val;
	  cout << val  << endl;
	}
	if(ncases - 1 != i) {
	  cout << endl; 
	}
  }
}
