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


def bt_dang2_p4_b1_c5_ds8(self):
    # Dạng 2: Xây dựng quy trình theo dõi năng suất cây trồng thực nghiệm
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        so_ngay = random.choice([25, 30, 35])
        h1 = str(round(random.uniform(8.2, 10.5), 1)).replace('.', ',')
        h2 = str(round(random.uniform(14.5, 18.2), 1)).replace('.', ',')
        h3 = str(round(random.uniform(21.0, 25.8), 1)).replace('.', ',')

        tikz_rau = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[right] {Giai đoạn};\n"
            "\\draw[line width=1pt, ->] (0,0) -- (0,3.0) node[above] {Chiều cao (cm)};\n"
            "\\draw[line width=1pt] (1.2,0.5) -- (3.0,1.4) -- (4.8,2.4);\n"
            "\\fill (1.2,0.5) circle (1pt) node[above left] {$%s$};\n"
            "\\fill (3.0,1.4) circle (1pt) node[above left] {$%s$};\n"
            "\\fill (4.8,2.4) circle (1pt) node[above left] {$%s$};\n"
            "\\draw[line width=1pt] (1.2,-0.1) -- (1.2,0.1) node[below=4pt] {Ngày $10$};\n"
            "\\draw[line width=1pt] (3.0,-0.1) -- (3.0,0.1) node[below=4pt] {Ngày $20$};\n"
            "\\draw[line width=1pt] (4.8,-0.1) -- (4.8,0.1) node[below=4pt] {Ngày $%s$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
            % (h1, h2, h3, so_ngay)
        )

        noidungcauhoi = ('''Trong vườn thực nghiệm sinh học, nhóm học sinh lớp $8B$ muốn đánh giá hiệu quả của hai loại phân bón hữu cơ đối với giống rau cải xanh sau $%s$ ngày gieo trồng thông qua các chỉ số: \\textit{Chiều cao trung bình của cây (cm)} (minh họa ở biểu đồ bên dưới), \\textit{Số lá trên mỗi cây}, và \\textit{Mức độ xanh tốt của lá (Rất tốt, Tốt, Trung bình, Kém)}.
%s
a) Nêu cách thức thu thập các dữ liệu trên và xác định phương pháp thu thập tương ứng.\\\\
b) Hãy phân loại chi tiết từng loại dữ liệu thu được theo sơ đồ phân loại đã học.''' % (so_ngay, tikz_rau))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Nhóm học sinh tiến hành trồng hai luống rau cải xanh với hai loại phân bón khác nhau trong cùng điều kiện chăm sóc, sau $%s$ ngày trực tiếp dùng thước đo chiều cao từng cây, đếm số lá trên mỗi cây và quan sát độ xanh tốt của lá. Đây là \\textbf{phương pháp thu thập dữ liệu trực tiếp} thông qua làm thí nghiệm và quan sát, đo đạc thực tế.
\\item Phân loại chi tiết ba loại dữ liệu thu được:\\\\
- \\textit{Chiều cao trung bình của cây (cm)}: thu được từ phép đo độ dài, có thể nhận giá trị thực tùy ý trong một khoảng nên là \\textbf{số liệu liên tục}.\\\\
- \\textit{Số lá trên mỗi cây}: thu được từ phép đếm phần tử, chỉ nhận giá trị nguyên dương nên là \\textbf{số liệu rời rạc}.\\\\
- \\textit{Mức độ xanh tốt của lá (Rất tốt, Tốt, Trung bình, Kém)}: không phải là số nhưng sắp xếp được theo thứ bậc chất lượng nên là \\textbf{dữ liệu không là số, có thể sắp thứ tự}.
\\end{enumEX}''' % so_ngay)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
