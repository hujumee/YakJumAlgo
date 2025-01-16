#include <iostream>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;

    string res;
    for (int i = 0; i < N; i++) {
        int tmp;
        cin >> tmp;
        if (tmp < X) res = res + to_string(tmp) + " ";
    }
    cout << res;
}