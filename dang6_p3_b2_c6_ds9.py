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

def bt_dang6_p3_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = randint(1, 4)
        area = 12 * k
        kq_str = str(area)
        
        if k == 1:
            p_latex = '\\frac{1}{2}x^2'
            d_latex = 'x + 4'
        elif k % 2 == 0:
            p_latex = '%sx^2' % (k // 2)
            d_latex = '%sx + %s' % (k, 4 * k)
        else:
            p_latex = '\\frac{%s}{2}x^2' % k
            d_latex = '%sx + %s' % (k, 4 * k)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho parabol $(P): y = %s$ và đường thẳng $(d): y = %s$ cắt nhau tại hai điểm phân biệt $A$ và $B$ như hình vẽ dưới đây. Tính diện tích tam giác $OAB$ (với $O$ là gốc tọa độ).
\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-2,1);
\\coordinate (B) at (4,4);
\\coordinate (M) at (0,2);
\\draw[->, line width=1pt] (-3.5,0) -- (5,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,5.2) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-3:4.4] plot (\\x, {0.25*(\\x)^2});
\\draw[line width=1pt] (-3,0.5) -- (4.8,4.4);
\\draw[line width=1pt, dashed] (-2,0) -- (A) -- (0,1);
\\draw[line width=1pt, dashed] (4,0) -- (B) -- (0,4);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above left] {$B$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\end{tikzpicture}
\\end{center}'''
                         %(p_latex, d_latex
                         ))

        # Nội dung lời giải
        loigiai = ('''Phương trình hoành độ giao điểm của $(P)$ và $(d)$ là: \\\\
                   $%s = %s \\Leftrightarrow x^2 - 2x - 8 = 0$. \\\\
                   Giải phương trình trên ta được hai nghiệm phân biệt $x_1 = -2$ và $x_2 = 4$. \\\\
                   Suy ra tọa độ các giao điểm là $A(-2; %s)$ và $B(4; %s)$. \\\\
                   Đường thẳng $(d)$ cắt trục tung $Oy$ tại điểm $M(0; %s)$ nên $OM = %s$. \\\\
                   Diện tích tam giác $OAB$ là: \\\\
                   $S_{OAB} = S_{OAM} + S_{OBM} = \\frac{1}{2} \\cdot OM \\cdot |x_A| + \\frac{1}{2} \\cdot OM \\cdot |x_B| = \\frac{1}{2} \\cdot %s \\cdot (2 + 4) = %s$.'''
                   %(p_latex, d_latex,
                     str(2*k), str(8*k),
                     str(4*k), str(4*k),
                     str(4*k), kq_str
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
