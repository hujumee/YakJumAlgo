#include <string>
#include <vector>

using namespace std;

int solution(vector<int> number) {
    int answer = 0;
    
    int val1, val2, val3;
    
    for (int i = 0; i < number.size() - 2; i++) {
        for (int j = i+1; j < number.size() - 1; j++) {
            for (int k = j+1; k < number.size(); k++) {
                val1 = number[i];
                val2 = number[j];
                val3 = number[k];
                
                if (val1 + val2 + val3 == 0) answer++;
            }
        }
    }
    
    return answer;
}