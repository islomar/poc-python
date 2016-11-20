#Profiling

https://julien.danjou.info/blog/2015/guide-to-python-profiling-cprofile-concrete-case-carbonara

##Instructions for installing a profiling visualization tool
##Option 1
1. Install https://jiffyclub.github.io/snakeviz/
2. Run `pip install snakeviz`
3. Run `snakeviz <filename.cprof>`

##Option 2
1. Install pyprof2calltree
`pip install pyprof2calltree`

2. On Mac, you have to compile KcacheGrind:
https://kcachegrind.github.io/html/Download.html

3. Run `pyprof2calltree -k -i <filename.cprof>`