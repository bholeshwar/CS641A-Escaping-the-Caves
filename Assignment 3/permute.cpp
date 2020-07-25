#include <iostream>

using namespace std;

int main() {
    char s[1000];
    cin.getline(s, sizeof(s));
    
    int P[5];
    P[0] = 3; P[1] = 2; P[2] = 0; P[3] = 1; P[4] = 4;
    int count = 0;
    
    string t = "chnbkjunczfiaxjyacvpcbbppfcfcvzxgbcdcqfhfegkaznancvaafmmzawxjpxcchxjwchmvhvmvauhgjhyuchnbkwzmaxecfcpmxjpahfiszzxgbcaptcluhuhncfxzeaznajxczuicsthhfhampgfhyyxgzajamudvcsxzhiyawhzxvmhapyzpzgcpjdzjdjxczuicfthajdyzphksvcdhjgsaiwhamjmhpfzfcxlhmhunzhujzxjwnwxdjfhkcezehcxfjnyfv";
    
    string n;
    
    for(int i=0; s[i] != '\0'; i++) {
        if(s[i] >= 'a' && s[i] <= 'z') {
            n.push_back(t[(count/5)*5 + P[count%5]]);
            count++;
        }
        else {
            n.push_back(s[i]);
        }
    }
    
    cout << n;
}