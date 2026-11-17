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


def bt_dang8_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_val = random.choice([1, 2])
        a_str = "" if a_val == 1 else latex(a_val)
        y1 = a_val * 1
        y2 = a_val * 4
        ab_len = 2
        cd_len = 4
        h_trap = y2 - y1
        area_trap = Rational(1, 2) * (ab_len + cd_len) * h_trap

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho parabol $(P): y = %sx^2$. Hai đường thẳng $y = %s$ và $y = %s$ lần lượt cắt $(P)$ tại các điểm $A, B$ (với $x_A < 0 < x_B$) và $C, D$ (với $x_C < 0 < x_D$). \\\\
a) Tìm tọa độ các điểm $A, B, C, D$. \\\\
b) Chứng minh tứ giác $ABDC$ là hình thang cân và tính diện tích của tứ giác đó.'''
                         %(a_str, latex(y1), latex(y2)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thay $y = %s$ vào phương trình $y = %sx^2$, ta có: \\\\
$%sx^2 = %s \\Rightarrow x^2 = 1 \\Rightarrow x = -1$ hoặc $x = 1$. \\\\
Vì $x_A < 0 < x_B$ nên $A(-1; %s)$ và $B(1; %s)$. \\\\
Thay $y = %s$ vào phương trình $y = %sx^2$, ta có: \\\\
$%sx^2 = %s \\Rightarrow x^2 = 4 \\Rightarrow x = -2$ hoặc $x = 2$. \\\\
Vì $x_C < 0 < x_D$ nên $C(-2; %s)$ và $D(2; %s)$.
\\item Hai đoạn thẳng $AB$ và $CD$ lần lượt nằm trên hai đường thẳng $y = %s$ và $y = %s$ cùng song song với trục hoành $Ox$ nên $AB // CD$. Suy ra tứ giác $ABDC$ là hình thang. \\\\
Mặt khác, $A$ đối xứng với $B$ qua trục tung $Oy$ và $C$ đối xứng với $D$ qua trục tung $Oy$ nên đoạn thẳng $AC$ đối xứng với đoạn thẳng $BD$ qua trục tung $Oy$. \\\\
Do đó $AC = BD$. Hình thang $ABDC$ có hai cạnh bên bằng nhau nên là hình thang cân. \\\\
Ta có độ dài hai đáy là $AB = |1 - (-1)| = %s$ và $CD = |2 - (-2)| = %s$. \\\\
Chiều cao của hình thang cân là khoảng cách giữa hai đường thẳng $y = %s$ và $y = %s$, bằng $h = %s - %s = %s$. \\\\
Diện tích hình thang cân $ABDC$ là: \\\\
$S_{ABDC} = \\frac{(AB + CD) \\cdot h}{2} = \\frac{(%s + %s) \\cdot %s}{2} = %s$ (đơn vị diện tích). \\\\
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3,0) -- (3,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.6) -- (0,5) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.2:2.2] plot(\\x, {(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1,1);
\\coordinate (B) at (1,1);
\\coordinate (C) at (-2,4);
\\coordinate (D) at (2,4);
\\draw[line width=1pt] (A)--(B)--(D)--(C)--cycle;
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (C) circle (1pt) node[left] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\end{tikzpicture}
\\end{center}
\\end{enumEX}'''
                   %(latex(y1), a_str,
                     a_str, latex(y1),
                     latex(y1), latex(y1),
                     latex(y2), a_str,
                     a_str, latex(y2),
                     latex(y2), latex(y2),
                     latex(y1), latex(y2),
                     latex(ab_len), latex(cd_len),
                     latex(y1), latex(y2), latex(y2), latex(y1), latex(h_trap),
                     latex(ab_len), latex(cd_len), latex(h_trap), latex(area_trap)
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
