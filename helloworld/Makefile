
binaries= ctest gtest

.PHONY : all
all : $(binaries) 

ctest :
	g++ --std=c++11 -o ctest testCatch.cpp

gtest :
	g++ --std=c++11 -o gtest gtest.cpp -lgtest -lpthread

.PHONY : test

test: 
	./ctest -sr junit -o ctestresults.xml
	./gtest --gtest_output=xml:gtestresults.xml

.PHONY : clean

clean:
	rm -f $(binaries) *.o
