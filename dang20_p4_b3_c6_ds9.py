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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang20_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        triples = [(3, 4, 5), (8, 15, 17), (5, 12, 13)]
        h0, w0, d0 = random.choice(triples)
        k = randint(2, 6)
        h_inch = h0 * k
        w_inch = w0 * k
        d_inch = d0 * k
        S_tong = h_inch + w_inch
        P_tich = h_inch * w_inch
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một màn hình máy tính phẳng dạng hình chữ nhật $ABCD$ có độ dài đường chéo $AC = %s\\text{ inch}$ (như hình vẽ). Biết rằng tổng chiều rộng và chiều cao của màn hình này bằng $%s\\text{ inch}$ (chiều rộng lớn hơn chiều cao). Sử dụng định lí Viète, hãy tính chiều rộng, chiều cao và diện tích bề mặt hiển thị của màn hình máy tính đó.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4,0);
\\coordinate (C) at (4,2.5);
\\coordinate (D) at (0,2.5);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt, dashed] (A)--(C);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(d_inch), latex(S_tong)))
        
        # Nội dung lời giải
        loigiai = ('''Gọi chiều rộng và chiều cao của màn hình máy tính lần lượt là $a$ (inch) và $b$ (inch) (điều kiện: $a > b > 0$). \\\\
Theo đề bài, tổng chiều rộng và chiều cao bằng $%s\\text{ inch}$ nên $a + b = %s$. \\\\
Áp dụng định lí Pythagore vào tam giác vuông $ABC$, ta có: \\\\
$AB^{2} + BC^{2} = AC^{2} \\Leftrightarrow a^{2} + b^{2} = %s^{2} = %s$. \\\\
Ta có: $a^{2} + b^{2} = (a + b)^{2} - 2ab \\Leftrightarrow %s^{2} - 2ab = %s \\Leftrightarrow ab = \\dfrac{%s - %s}{2} = %s$. \\\\
Khi đó, $a$ và $b$ là hai nghiệm của phương trình bậc hai: $x^{2} - %sx + %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^{2} - 4 \\cdot 1 \\cdot %s = %s > 0 \\Rightarrow \\sqrt{\\Delta} = %s$. \\\\
Phương trình có hai nghiệm phân biệt là $x_{1} = %s$ và $x_{2} = %s$. \\\\
Vì $a > b > 0$ nên chiều rộng màn hình là $a = %s\\text{ inch}$ và chiều cao màn hình là $b = %s\\text{ inch}$. \\\\
Diện tích bề mặt hiển thị của màn hình máy tính đó là: $S = ab = %s\\text{ inch}^{2}$.'''
                   % (latex(S_tong), latex(S_tong),
                      latex(d_inch), latex(d_inch**2),
                      latex(S_tong), latex(d_inch**2), latex(S_tong**2), latex(d_inch**2), latex(P_tich),
                      latex(S_tong), latex(P_tich),
                      latex(S_tong), latex(P_tich), latex((w_inch - h_inch)**2), latex(w_inch - h_inch),
                      latex(w_inch), latex(h_inch),
                      latex(w_inch), latex(h_inch),
                      latex(P_tich)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
