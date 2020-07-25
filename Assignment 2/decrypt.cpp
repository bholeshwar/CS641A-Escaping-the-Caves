#include <iostream>

using namespace std;

int main() {
    int K[9] = {10, 2, 6, 2, 3, 5, 2, 2, 1};
    
    char s[1000];
    cin.getline(s, sizeof(s)); // Take the ciphertext as input
    
    int k_pointer = 0;
    
    for(int i=0; s[i]!='\0'; i++) {
        if(s[i] >= 'a' && s[i] <= 'z') {
            s[i] = s[i] - K[k_pointer%9];
            if(s[i] < 'a') {
                s[i] += 26;
            }
            k_pointer++;
        }
        
        else if(s[i] >= 'A' && s[i] <= 'Z') {
            s[i] = s[i] - K[k_pointer%9];
            if(s[i] < 'A') {
                s[i] += 26;
            }
            k_pointer++;
        }
    }
    
    for(int i=0; s[i]!='\0'; i++) {
        cout << s[i];
    }
}