## Notes

Building with cmake from within `cpp_src`:
- Create a build directory:
```
mkdir build && cd build
```
- Run cmake:
```
cmake ../
```
- And then finally make things:
```
make
```

Alternatively, compile and run single problems with this:
```
g++ -std=c++17 -g problem-001.cpp -o /tmp/problem-001 && /tmp/problem-001
```