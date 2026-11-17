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


def bt_dang3_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = randint(2, 8)
        om = 2 * r
        om2 = om ** 2
        r2 = r ** 2
        am2 = om2 - r2
        am = r * sqrt(3)
        ah = Rational(r, 2) * sqrt(3)
        ab = r * sqrt(3)
        mh = Rational(3 * r, 2)
        dt = Rational(3 * r2, 4) * sqrt(3)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ và điểm $M$ nằm ngoài đường tròn sao cho $OM = %s\\text{ cm}$. Kẻ hai tiếp tuyến $MA$ và $MB$ với đường tròn ($A$ và $B$ là hai tiếp điểm). Đường thẳng $OM$ cắt dây $AB$ tại $H$. Tính diện tích tam giác $MAB$. \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (O) at (0,0);
            \\coordinate (M) at (-3.6,0);
            \\coordinate (A) at (-0.9,1.5588);
            \\coordinate (B) at (-0.9,-1.5588);
            \\coordinate (H) at (-0.9,0);
            \\draw[line width=1pt] (O) circle (1.8);
            \\draw[line width=1pt] (M)--(A)--(O)--(B)--cycle;
            \\draw[line width=1pt] (M)--(O) (A)--(B);
            \\fill (O) circle (1pt) node[right] {$O$};
            \\fill (M) circle (1pt) node[left] {$M$};
            \\fill (A) circle (1pt) node[above] {$A$};
            \\fill (B) circle (1pt) node[below] {$B$};
            \\fill (H) circle (1pt) node[above right] {$H$};
        \\end{tikzpicture}
        \\end{center}'''
        %(latex(r), latex(om)))

        # Nội dung lời giải
        loigiai = ('''Theo tính chất của hai tiếp tuyến cắt nhau, ta có $OM$ là tia phân giác của góc $\\widehat{AOB}$. Trong tam giác cân $AOB$ ($OA = OB = %s\\text{ cm}$), đường phân giác $OM$ đồng thời là đường cao và đường trung trực của đoạn thẳng $AB$. \\\\
        Suy ra $OM \\perp AB$ tại $H$ và $H$ là trung điểm của $AB$. \\\\
        Xét tam giác $OAM$ vuông tại $A$ ($\\widehat{OAM} = 90^\\circ$ do $MA$ là tiếp tuyến của $(O)$ tại $A$), áp dụng định lí Pythagore ta có: \\\\
        $AM^2 = OM^2 - OA^2 = %s^2 - %s^2 = %s - %s = %s \\Rightarrow AM = %s\\text{ (cm)}$. \\\\
        Áp dụng hệ thức lượng trong tam giác vuông $OAM$ có đường cao $AH$, ta có: \\\\
        $AH \\cdot OM = OA \\cdot AM \\Rightarrow AH = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$. \\\\
        Do đó độ dài dây cung $AB = 2AH = 2 \\cdot %s = %s\\text{ (cm)}$. \\\\
        Áp dụng định lí Pythagore trong tam giác $AHM$ vuông tại $H$: \\\\
        $MH = \\sqrt{AM^2 - AH^2} = \\sqrt{%s - \\left(%s\\right)^2} = %s\\text{ (cm)}$. \\\\
        Vậy diện tích tam giác $MAB$ là: \\\\
        $S_{MAB} = \\dfrac{1}{2} \\cdot MH \\cdot AB = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2\\text{)}$.'''
        %(latex(r), latex(om), latex(r), latex(om2), latex(r2), latex(am2), latex(am), latex(r), latex(am), latex(om), latex(ah), latex(ah), latex(ab), latex(am2), latex(ah), latex(mh), latex(mh), latex(ab), latex(dt)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
