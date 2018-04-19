import sys
from PyQt5.QtWidgets import QApplication
from window import Window

testing_data = """0,150
1,223
2,465
3,1070
4,1900
5,2696
6,3380
7,3923
8,4143
9,3926
10,3444
11,2898
12,2312
13,1660
14,1028
15,430
16,133"""

testing_data_weighted = """0,150,1
1,223,1
2,3000,1
3,1070,20
4,1900,1
5,2696,1
6,3380,2
7,3923,1
8,4143,1
9,3926,1
10,3444,1
11,2898,1
12,2312,2
13,1660,1
14,1028,1
15,430,1
16,133,1"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())