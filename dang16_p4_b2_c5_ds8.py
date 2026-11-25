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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang16_p4_b2_c5_ds8(self):
    # Dạng 16 (Tự luận - Vận dụng): Chuyển đổi biểu đồ cột kép sang bảng 2 chiều và biểu đồ hình quạt tròn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tikz_q = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Số học sinh};
        \\draw[line width=1pt, ->] (0,0) -- (5.4,0) node[right] {Xếp loại};
        \\draw[line width=1pt, fill=black!35] (0.5,0) rectangle (1.0,1.2) (2.1,0) rectangle (2.6,2.0) (3.7,0) rectangle (4.2,0.8);
        \\draw[line width=1pt, fill=white] (1.0,0) rectangle (1.5,1.5) (2.6,0) rectangle (3.1,1.8) (4.2,0) rectangle (4.7,0.7);
        \\node[above] at (0.75,1.2) {$12$}; \\node[above] at (1.25,1.5) {$15$};
        \\node[above] at (2.35,2.0) {$20$}; \\node[above] at (2.85,1.8) {$18$};
        \\node[above] at (3.95,0.8) {$8$}; \\node[above] at (4.45,0.7) {$7$};
        \\node[below] at (1.0,0) {Tốt}; \\node[below] at (2.6,0) {Khá}; \\node[below] at (4.2,0) {Đạt};
        \\draw[line width=1pt, fill=black!35] (5.1,1.8) rectangle (5.4,2.1); \\node[right] at (5.4,1.95) {Lớp 8A};
        \\draw[line width=1pt, fill=white] (5.1,1.3) rectangle (5.4,1.6); \\node[right] at (5.4,1.45) {Lớp 8B};
        \\end{tikzpicture}
        \\end{center}""" )
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) circle (1.5);
        \\draw[line width=1pt] (0,0) -- (0:1.5) (0,0) -- (121.5:1.5) (0,0) -- (292.5:1.5);
        \\node at (60.75:0.9) {$33,75\\%$};
        \\node at (207:0.9) {$47,5\\%$};
        \\node at (326.25:0.95) {$18,75\\%$};
        \\node[right] at (1.9, 0.6) {Tốt: $33,75\\%$};
        \\node[right] at (1.9, 0.0) {Khá: $47,5\\%$};
        \\node[right] at (1.9, -0.6) {Đạt: $18,75\\%$};
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Cho biểu đồ cột kép biểu diễn kết quả xếp loại học lực Học kì I của hai lớp 8A và 8B:%sa) Lập bảng thống kê hai chiều biểu diễn số lượng học sinh theo từng mức xếp loại của cả hai lớp (có thêm cột và hàng Tổng số).\\\\
        b) Nếu gộp chung học sinh của cả hai lớp 8A và 8B thành một tập thể, hãy tính tỉ lệ phần trăm của từng mức xếp loại (Tốt, Khá, Đạt) và vẽ biểu đồ hình quạt tròn biểu diễn cơ cấu xếp loại học lực của cả hai lớp gộp lại.""" % tikz_q)
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Bảng thống kê hai chiều kết quả xếp loại học lực Học kì I của hai lớp 8A và 8B:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|}
        \\hline
        \\textbf{Lớp / Xếp loại} & Tốt & Khá & Đạt & \\textbf{Tổng số} \\\\
        \\hline
        \\textbf{Lớp 8A} & $12$ & $20$ & $8$ & $40$ \\\\
        \\hline
        \\textbf{Lớp 8B} & $15$ & $18$ & $7$ & $40$ \\\\
        \\hline
        \\textbf{Tổng số} & $27$ & $38$ & $15$ & $80$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        \\item Tỉ lệ phần trăm của từng mức xếp loại khi gộp chung hai lớp ($80$ học sinh):\\\\
        - Mức Tốt: $\\dfrac{27}{80} \\cdot 100\\%% = 33,75\\%%$.\\\\
        - Mức Khá: $\\dfrac{38}{80} \\cdot 100\\%% = 47,5\\%%$.\\\\
        - Mức Đạt: $\\dfrac{15}{80} \\cdot 100\\%% = 18,75\\%%$.\\\\
        Biểu đồ hình quạt tròn biểu diễn cơ cấu xếp loại học lực của cả hai lớp:%s
        \\end{enumEX}""" % tikz_a)

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
