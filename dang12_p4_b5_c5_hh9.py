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



def bt_dang12_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(25, 10, 39, 36), (20, 8, 37, 35), (30, 14, 65, 63), (26, 11, 25, 20)]
        R, r, d, AB = random.choice(bo_so)
        tong_thang = 2 * AB
        
        alpha = math.acos((R - r) / d)
        L_cung1 = R * (2 * math.pi - 2 * alpha)
        L_cung2 = r * (2 * alpha)
        L_tong_val = tong_thang + L_cung1 + L_cung2
        L_tong_tron = str(Decimal(str(L_tong_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O') at (4.5,0);
\\coordinate (A) at (0.55,1.65);
\\coordinate (B) at (4.72,0.66);
\\coordinate (C) at (0.55,-1.65);
\\coordinate (D) at (4.72,-0.66);
\\coordinate (H) at (0.33,0.99);
\\draw[line width=1pt] (O) circle (1.74cm);
\\draw[line width=1pt] (O') circle (0.7cm);
\\draw[line width=1pt] (A)--(B) (C)--(D) (O)--(O') (O)--(A) (O')--(B);
\\draw[line width=1pt, dashed] (O')--(H);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (O') circle (1pt) node[right] {$O'$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (H) circle (1pt) node[left] {$H$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Một động cơ điện truyền chuyển động cho một máy bơm nước thông qua hai puly (ròng rọc) hình tròn có bán kính lần lượt là $R = %s\\text{ cm}$ và $r = %s\\text{ cm}$. Khoảng cách giữa hai tâm trục của hai puly là $OO' = %s\\text{ cm}$. Hai puly được nối với nhau bằng một dây curoa mắc hở (hai nhánh dây curoa đóng vai trò là hai tiếp tuyến chung ngoài $AB$ và $CD$ của hai đường tròn).\\\\
        a) Tính tổng chiều dài hai đoạn dây curoa thẳng không tiếp xúc với puly.\\\\
        b) Tính tổng chiều dài tối thiểu của sợi dây curoa ôm trọn hệ thống hai puly trên (làm tròn kết quả đến hàng đơn vị theo đơn vị cm). %s'''
                         % (latex(R), latex(r), latex(d), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Vì $AB$ là tiếp tuyến chung ngoài của $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ nên $OA \\perp AB$ và $O'B \\perp AB$.\\\\
        Kẻ $O'H \\perp OA$ tại $H$. Tứ giác $O'HAB$ có ba góc vuông nên là hình chữ nhật, suy ra $AB = O'H$ và $AH = O'B = %s\\text{ cm}$.\\\\
        Do đó $OH = OA - AH = %s - %s = %s\\text{ cm}$.\\\\
        Áp dụng định lí Pythagore vào tam giác vuông $OHO'$, ta có:\\\\
        $AB = O'H = \\sqrt{OO'^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}$.\\\\
        Do tính đối xứng qua $OO'$, hai nhánh dây curoa thẳng bằng nhau: $CD = AB = %s\\text{ cm}$.\\\\
        Tổng chiều dài hai đoạn dây curoa thẳng là: $AB + CD = 2 \\cdot %s = %s\\text{ (cm)}$.
        \\item Trong tam giác vuông $OHO'$, ta có $\\cos \\widehat{AOO'} = \\frac{OH}{OO'} = \\frac{%s}{%s}$.\\\\
        Số đo góc ở tâm chắn cung lớn $AC$ của puly $(O)$ là $n_1 = 360^\\circ - 2\\widehat{AOO'}$, độ dài cung lớn $AC$ là $l_1 = \\frac{\\pi \\cdot %s \\cdot n_1}{180^\\circ}$.\\\\
        Số đo góc ở tâm chắn cung nhỏ $BD$ của puly $(O')$ là $n_2 = 2\\widehat{AOO'}$, độ dài cung nhỏ $BD$ là $l_2 = \\frac{\\pi \\cdot %s \\cdot n_2}{180^\\circ}$.\\\\
        Tổng chiều dài tối thiểu của sợi dây curoa là: $L = AB + CD + l_1 + l_2 \\approx %s\\text{ (cm)}$.
        \\end{enumEX}'''
                   % (latex(R), latex(r), latex(r), latex(R), latex(r), latex(R - r),
                      latex(d), latex(R - r), latex(AB), latex(AB), latex(AB), latex(tong_thang),
                      latex(R - r), latex(d), latex(R), latex(r), L_tong_tron))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
