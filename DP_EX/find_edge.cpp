#include<bits/stdc++.h>
#define N 5000009
using namespace std;
typedef long long ll;
int st[N],tong[N],tt,top;
map<int,string>mp; 
inline ll rd(){
	ll x=0;char c=getchar();bool f=0;
	while(!isdigit(c)){if(c=='-')f=1;c=getchar();}
	while(isdigit(c)){x=(x<<1)+(x<<3)+(c^48);c=getchar();}
	return f?-x:x;
}
char s[100000];
int main(){
	int x,y;
	freopen("node_id_cntid.csv","r",stdin); 
	while(scanf("%s",s)!=EOF){
		int len=strlen(s);
		if(!isdigit(s[0]))continue;
		int xx=0;
		string S="";
		int tag=0;
		for(int i=0;i<len;++i){
			if(s[i]==',')tag=1;
			else if(!tag)xx=xx*10+s[i]-'0';
			else S=S+s[i];
		}
		mp[xx]=S;
	} 
	fclose(stdin);
	freopen("answer.txt","r",stdin); 
	freopen("my.json","w",stdout);
	puts("[");
	int tag=0;
	while(scanf("%d%d",&x,&y)!=EOF){
		if(mp.find(x)!=mp.end()&&mp.find(y)!=mp.end()){
			if(tag)printf(",\n");
			else tag=1;
			printf("{\n");
			printf("\"source\":\"");
			cout<<x;
			printf("\",\n");
			printf("\"target\":\"");
			cout<<y;
			printf("\"\n");
			printf("}");
		}
	}
	puts("]");
    return 0;
}

