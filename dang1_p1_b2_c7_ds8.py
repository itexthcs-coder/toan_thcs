import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang1_p1_b2_c7_ds8(self):
    # Dạng 1: Nhận biết quy trình giải bài toán bằng cách lập phương trình
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)
    
    if dang == '1':
        noidungcauhoi = "Trong các bước giải một bài toán bằng cách lập phương trình, bước đầu tiên cần thực hiện là gì?"
        da = "Chọn ẩn số và đặt điều kiện thích hợp cho ẩn số."
        s = [
            "Giải phương trình vừa lập được.",
            "Kiểm tra xem nghiệm có thỏa mãn điều kiện của ẩn không.",
            "Kết luận đáp số của bài toán."
        ]
        loigiai = "Quy trình giải bài toán bằng cách lập phương trình gồm 3 bước:\\\\Bước 1: Lập phương trình (Chọn ẩn số và đặt điều kiện thích hợp cho ẩn số; biểu diễn các đại lượng chưa biết theo ẩn và các đại lượng đã biết; lập phương trình biểu thị mối quan hệ giữa các đại lượng).\\\\Bước 2: Giải phương trình.\\\\Bước 3: Trả lời (Kiểm tra xem trong các nghiệm của phương trình, nghiệm nào thỏa mãn điều kiện của ẩn, nghiệm nào không, rồi kết luận).\\\\Vậy bước đầu tiên cần thực hiện là chọn ẩn số và đặt điều kiện thích hợp cho ẩn số."
    elif dang == '2':
        noidungcauhoi = "Trong quy trình giải bài toán bằng cách lập phương trình, sau khi giải phương trình tìm được giá trị của ẩn ở Bước 2, bước tiếp theo cần thực hiện là gì?"
        da = "Kiểm tra xem nghiệm nào thỏa mãn điều kiện của ẩn rồi kết luận."
        s = [
            "Đặt điều kiện thích hợp cho ẩn số.",
            "Biểu diễn các đại lượng chưa biết theo ẩn.",
            "Lập phương trình biểu thị mối quan hệ giữa các đại lượng."
        ]
        loigiai = "Sau khi giải phương trình (Bước 2), ta thực hiện Bước 3 (Trả lời): Kiểm tra xem trong các nghiệm của phương trình, nghiệm nào thỏa mãn điều kiện của ẩn, nghiệm nào không, rồi kết luận."
    else:
        noidungcauhoi = "Khi thực hiện Bước 1 của việc giải bài toán bằng cách lập phương trình, ngay sau khi chọn ẩn số và đặt điều kiện thích hợp cho ẩn số, ta cần làm gì?"
        da = "Biểu diễn các đại lượng chưa biết theo ẩn và các đại lượng đã biết."
        s = [
            "Giải phương trình để tìm giá trị của ẩn.",
            "Đối chiếu nghiệm với điều kiện ban đầu.",
            "Kết luận bài toán ngay lập tức."
        ]
        loigiai = "Bước 1 (Lập phương trình) gồm ba ý nhỏ theo thứ tự:\\\\- Chọn ẩn số và đặt điều kiện thích hợp cho ẩn số;\\\\- Biểu diễn các đại lượng chưa biết theo ẩn và các đại lượng đã biết;\\\\- Lập phương trình biểu thị mối quan hệ giữa các đại lượng."

    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)

    da_d = ('\\True ' + str(da))
    list_1 = [da_d, str(das1), str(das2), str(das3)]
    random.shuffle(list_1)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
