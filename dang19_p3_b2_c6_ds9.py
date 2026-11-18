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

def bt_dang19_p3_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = randint(2, 5)
        h_bar = random.choice([2, 2.5, 3, 3.5])
        h_max = h_bar + 0.5 * (k**2)
        do_dai = 2 * k
        kq_str = str(do_dai)
        
        h_max_str = str(Decimal(str(h_max)).quantize(Decimal('0.01')).normalize()).replace('.', ',')
        h_bar_str = str(Decimal(str(h_bar)).quantize(Decimal('0.01')).normalize()).replace('.', ',')
        hieu_str = str(Decimal(str(h_max - h_bar)).quantize(Decimal('0.01')).normalize()).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cổng chào hình parabol được gắn vào hệ trục tọa độ $Oxy$ có phương trình $y = -\\frac{1}{2}x^2 + %s$ (với trục $Ox$ trùng với mặt đất, đơn vị trên mỗi trục tính bằng mét). Người ta lắp một thanh ngang trang trí song song với mặt đất và cách mặt đất $%s\\text{ m}$ nối hai nhánh của cổng parabol (như hình vẽ). Tính độ dài của thanh ngang đó (đơn vị: mét).
\\begin{center}
\\begin{tikzpicture}[scale=0.7, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.8,2);
\\coordinate (B) at (1.8,2);
\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.5) -- (0,4.5) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.55:2.55] plot (\\x, {-0.55*(\\x)^2 + 3.78});
\\draw[line width=1pt] (A) -- (B);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\node[above right] at (0,2) {$%s\\text{ m}$};
\\end{tikzpicture}
\\end{center}'''
                         %(h_max_str, h_bar_str, h_bar_str
                         ))

        # Nội dung lời giải
        loigiai = ('''Gọi hai đầu mút của thanh ngang gắn trên cổng parabol là $A$ và $B$. \\\\
                   Vì thanh ngang song song với mặt đất và cách mặt đất $%s\\text{ m}$ nên tung độ của hai điểm $A$ và $B$ đều bằng $%s$. \\\\
                   Thay $y = %s$ vào phương trình parabol $y = -\\frac{1}{2}x^2 + %s$, ta được: \\\\
                   $-\\frac{1}{2}x^2 + %s = %s \\Leftrightarrow \\frac{1}{2}x^2 = %s \\Leftrightarrow x^2 = %s \\Leftrightarrow x = %s$ hoặc $x = -%s$. \\\\
                   Suy ra tọa độ hai đầu mút là $A(-%s; %s)$ và $B(%s; %s)$. \\\\
                   Vậy độ dài của thanh ngang trang trí là $AB = |%s - (-%s)| = %s$ (mét).'''
                   %(h_bar_str, h_bar_str,
                     h_bar_str, h_max_str,
                     h_max_str, h_bar_str, hieu_str, str(k**2), str(k), str(k),
                     str(k), h_bar_str, str(k), h_bar_str,
                     str(k), str(k), kq_str
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(kq_str)

    # Xuất câu trắc nghiệm trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
