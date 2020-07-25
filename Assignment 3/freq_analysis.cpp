#include <iostream>

using namespace std;

int main() {
    char s[1000];
    cin.getline(s, sizeof(s)); // Enter the encrypted text as input
    
    int freq[26] = {0};
    
    for(int i=0; s[i]!='\0'; i++) {
        if( s[i] >= 'a' && s[i] <= 'z' ) {
            freq[s[i] - 'a']++;
        }
        else if( s[i] >='A' && s[i] <= 'Z' ) {
            freq[s[i] - 'A']++;
        } 
    }
    
    for(int i=0; i<26; i++) {
        char c = 'a' + i;
        cout << c << " " << freq[i] << endl;
    }
    
    float IC = 0;
    int total_count = 0;
    
    for(int i=0; i<26; i++) {
        IC += freq[i]*(freq[i]-1);
        total_count += freq[i];
    }
    
    IC /= (total_count*(total_count-1));
    
    cout << "Total count is " << total_count << endl;
    cout << "Index of coincidence is " << IC;
}