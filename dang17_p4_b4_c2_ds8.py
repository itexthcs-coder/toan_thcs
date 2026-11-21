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


def bt_dang17_p4_b4_c2_ds8(self):
    y = symbols('y')
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        c_cat = random.choice([4, 5])
        hieu_xy = random.choice([8, 10, 12])
        y_val = random.randint(22, 30)
        x_val = y_val + hieu_xy
        the_tich = c_cat * (x_val - 2*c_cat) * (y_val - 2*c_cat)
        tich_hai_canh = (x_val - 2*c_cat) * (y_val - 2*c_cat)
        
        tikz_hinh = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (0,0) rectangle (4.2,2.8);
    \\draw[line width=1pt, dashed] (0,2.2) rectangle (0.6,2.8);
    \\draw[line width=1pt, dashed] (3.6,2.2) rectangle (4.2,2.8);
    \\draw[line width=1pt, dashed] (0,0) rectangle (0.6,0.6);
    \\draw[line width=1pt, dashed] (3.6,0) rectangle (4.2,0.6);
    \\draw[line width=1pt, <->] (0,3.05) -- (4.2,3.05) node[midway, above] {$x$};
    \\draw[line width=1pt, <->] (-0.25,0) -- (-0.25,2.8) node[midway, left] {$y$};
    \\node at (0.3,2.5) {$%s$};
\\end{tikzpicture}
\\end{center}''' % (c_cat)
        
        noidungcauhoi = ('''Một xưởng sản xuất bao bì sử dụng một tấm bìa hình chữ nhật có chiều dài $x\\text{ (cm)}$ và chiều rộng $y\\text{ (cm)}$ ($x > y > %s$). Ở bốn góc của tấm bìa, người ta cắt bỏ bốn hình vuông bằng nhau có cạnh là $%s\\text{ cm}$ rồi gập lại để tạo thành một chiếc hộp không nắp có chiều cao $%s\\text{ cm}$. \\
a) Viết biểu thức biểu thị diện tích đáy hộp và thể tích $V$ của chiếc hộp theo $x$ và $y$. \\\\
b) Biết chiều dài tấm bìa ban đầu hơn chiều rộng là $%s\\text{ cm}$ ($x - y = %s$) và thể tích của chiếc hộp là $V = %s\\text{ cm}^3$. Hãy tính chiều dài và chiều rộng của tấm bìa carton ban đầu.'''
                         % (2*c_cat, c_cat, c_cat, hieu_xy, hieu_xy, the_tich) + tikz_hinh)
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Đáy hộp là hình chữ nhật có chiều dài $x - %s\\text{ (cm)}$ và chiều rộng $y - %s\\text{ (cm)}$.\\\\
Diện tích đáy hộp là $S_{\\text{đáy}} = (x - %s)(y - %s)\\text{ (cm}^2\\text{)}$.\\\\
Thể tích của chiếc hộp không nắp chiều cao $%s\\text{ cm}$ là:
\\begin{align*}
V = %s(x - %s)(y - %s)\\text{ (cm}^3\\text{)}.
\\end{align*}
\\item Vì $x - y = %s$ nên $x = y + %s$. Thay vào công thức thể tích với $V = %s$, ta có:
\\begin{align*}
%s(y + %s - %s)(y - %s) &= %s \\\\
(y + %s)(y - %s) &= %s \\\\
y^2 %s %sy - %s &= 0 \\\\
(y - %s)(y + %s) &= 0.
\\end{align*}
Vì $y > %s$ nên $y = %s\\text{ (cm)}$, suy ra chiều dài $x = %s + %s = %s\\text{ (cm)}$.
\\end{enumEX}''' % (2*c_cat, 2*c_cat, 2*c_cat, 2*c_cat, c_cat,
                      c_cat, 2*c_cat, 2*c_cat,
                      hieu_xy, hieu_xy, the_tich,
                      c_cat, hieu_xy, 2*c_cat, 2*c_cat, the_tich,
                      hieu_xy - 2*c_cat, 2*c_cat, tich_hai_canh,
                      '+' if (hieu_xy - 4*c_cat) >= 0 else '-', abs(hieu_xy - 4*c_cat),
                      tich_hai_canh + 2*c_cat*(hieu_xy - 2*c_cat),
                      y_val, y_val + hieu_xy - 4*c_cat,
                      2*c_cat, y_val, y_val, hieu_xy, x_val))

    # Xuất câu hỏi và lời giải tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
