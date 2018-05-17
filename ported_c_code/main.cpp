#include "nGramClean.cpp"

int main(int argc, char * argv[]){
	std::string x;
	nGramClean my;
	x=my.clean_up("222");
	std::cout << x << std::endl;
	return 0;
}