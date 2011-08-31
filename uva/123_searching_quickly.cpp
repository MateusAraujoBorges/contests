#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

struct record {
  string title;
  string word;
  int wordPos;
  int origPos;
  int index;
};

vector<string> split(const string& s, char delim) {
  vector<string> tokens;
  stringstream ss(s);
  string tok;

  while(getline(ss,tok,delim)) {
    tokens.push_back(tok);
  }

  return tokens;
}

char cheaptolower(char in){
  if(in<='Z' && in>='A')
    return in-('Z'-'z');
  return in;
} 

char cheaptoupper(char in){
  if(in<='z' && in>='a')
    return in+('Z'-'z');
  return in;
} 

string toLowercase(string s) {
  transform(s.begin(), s.end(), s.begin(), cheaptolower);
  return s;
}

vector<record> processline(const set<string> &badwords, string &title, int origPos) {
  vector<string> titlewords = split(title,' ');
  vector<string>::iterator it;
  set<string>::iterator sit;
  vector<record> records;
  int pos = 0; //position of the current word in the title

  for(it = titlewords.begin(); it < titlewords.end(); it++) {
    string word = *it;
    bool inSet = badwords.find(word) != badwords.end();

    if(!inSet) {
      //      cout << "inSet" << word << endl;
      //add record of the title/word
      record r;
      r.title = title;
      r.word = word;
      r.wordPos = pos;
      r.origPos = origPos;
      r.index = title.find(word);
      records.push_back(r);
    } else {
      //cout << "notInSet: " << word << endl;
    }

    pos = pos + word.length() + 1; //the '1' is from the blank space
  }

  //  cout << "ending method\n";
  return records;
}

bool compareRecords(record r1, record r2) {
  return r1.word < r2.word;
}

int main () {
  string input = "dummy";
  set<string> badwords;
  vector<record> records;

  while(input.compare("::") != 0) {
    badwords.insert(input);
    cin >> input;
  }

  getline(cin,input);  //remove \n
  getline(cin,input);

  int i = 1;
  while(!cin.eof()) {
    string lowerWord = toLowercase(input);
    vector<record> r = processline(badwords,lowerWord,i);
    //    printf("%d \n",r->size()); //if I uncomment this, the program segfaults. why?
    //    r->size();
    vector<record>::iterator it;
    for (it = r.begin(); it < r.end(); it++) {
      // uppercase relevant word
      string title = it->title;
      int wordSize = (it->word).length();
      int wordStart = it->wordPos;
      transform(it->title.begin()+wordStart,it->title.begin()+wordStart+wordSize,it->title.begin()+wordStart,cheaptoupper);
      records.push_back(*it);
      //      cout << "pushed title: " << it->title  << " because of word: " << (it->word) << " at pos:" << it->wordPos << endl;
    }
    getline(cin,input);
    i++;
  }

  //sort and print records

  stable_sort(records.begin(),records.end(),compareRecords);

  for (vector<record>::iterator it = records.begin(); it < records.end(); it++) {
    cout << it->title << endl;
  }

  return 0;
}
