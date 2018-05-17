#ifndef NGRAMCLEAN_H
#define NGRAMCLEAN_H

#include <iostream>


class nGramClean{
	public:
		std::vector<std::string> stopwords;
		nGramClean();
		std::string clean_up(std::string raw);
};

#endif