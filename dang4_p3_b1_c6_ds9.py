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


def bt_dang4_p3_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        x0 = randint(2, 5)
        y0 = x0**2
        OA_sq = x0**2 + y0**2
        OA_latex = latex(sqrt(OA_sq))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trên parabol $(P): y=x^2$, lấy điểm $A$ có hoành độ dương sao cho đoạn thẳng $OA=%s$. Hoành độ của điểm $A$ bằng bao nhiêu?
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3,0) -- (3,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,4.5) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.1:2.1] plot (\\x, {(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (A) at (1.8,3.24);
\\coordinate (H) at (1.8,0);
\\draw[line width=1pt] (O)--(A);
\\draw[line width=1pt, dashed] (A)--(H) (A)--(0,3.24);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[right] {$A$};
\\fill (H) circle (1pt) node[below] {$H$};
\\end{tikzpicture}
\\end{center}'''
                         % (OA_latex))

        # Nội dung lời giải
        loigiai = ('''Gọi $x_0$ ($x_0 > 0$) là hoành độ của điểm $A$. Vì $A$ thuộc parabol $(P): y = x^2$ nên tung độ của $A$ là $y_0 = x_0^2$, do đó $A\\left(x_0; x_0^2\\right)$. \\\\
Gọi $H(x_0; 0)$ là hình chiếu vuông góc của $A$ lên trục hoành $Ox$. Áp dụng định lí Pythagore trong tam giác $OHA$ vuông tại $H$, ta có: \\\\
$OA^2 = OH^2 + HA^2 = x_0^2 + \\left(x_0^2\\right)^2 = x_0^4 + x_0^2$. \\\\
Theo đề bài, $OA = %s$ nên $OA^2 = %s$. Ta có phương trình: \\\\
$x_0^4 + x_0^2 = %s \\Leftrightarrow x_0^4 + x_0^2 - %s = 0 \\Leftrightarrow \\left(x_0^2 - %s\\right)\\left(x_0^2 + %s\\right) = 0$. \\\\
Vì $x_0^2 + %s > 0$ với mọi $x_0$ nên $x_0^2 = %s$. \\\\
Do $x_0 > 0$ nên $x_0 = %s$. \\\\
Vậy hoành độ của điểm $A$ bằng $%s$.'''
                   % (OA_latex, str(OA_sq),
                      str(OA_sq), str(OA_sq), str(x0**2), str(x0**2 + 1),
                      str(x0**2 + 1), str(x0**2),
                      str(x0), str(x0)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(x0))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
