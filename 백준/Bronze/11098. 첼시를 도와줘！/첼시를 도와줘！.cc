#include <iostream>
#include <string>

using namespace std;

void printExpensive(int p) {
    int highest_cost = 0;
    string answer = "";
    
    for (int i = 0; i < p; i++) {
        int cost;
        string name;
        
        cin >> cost >> name;
        
        if (cost > highest_cost) {
            highest_cost = cost;
            answer = name;
        }
    }
    
    cout << answer << endl;
}

int main () {
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        int p;
        cin >> p;
        printExpensive(p);
    }
    
    return 0;
}