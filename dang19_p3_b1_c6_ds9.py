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


def bt_dang19_p3_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        k_num = randint(1, 3)
        k_den = randint(2, 4)
        a = Rational(k_num, k_den)
        xB = k_den * randint(2, 3)
        yB = a * (xB**2)
        d = k_den * randint(1, 2)
        while d >= xB:
            d = k_den
        xM = xB - d
        yM = a * (xM**2)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tại một công viên giải trí, người ta thiết kế một máng trượt nước có mặt cắt dọc dạng một nhánh parabol $y=ax^2$ ($x \\ge 0$), với gốc tọa độ $O(0;0)$ là điểm thấp nhất của máng ở sát mặt hồ. Biết điểm xuất phát ở độ cao $%s\\text{ m}$ so với mặt hồ và cách điểm tiếp nước theo phương ngang là $%s\\text{ m}$. Tại vị trí cách điểm xuất phát $%s\\text{ m}$ theo phương ngang, người trượt đang ở độ cao bao nhiêu mét so với mặt hồ?
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-0.8,0) -- (3.8,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,4.5) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=0:3] plot (\\x, {0.42*(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (B) at (3,3.78);
\\coordinate (M) at (2,1.68);
\\coordinate (H) at (2,0);
\\coordinate (K) at (3,0);
\\draw[line width=1pt, dashed] (B)--(K) (M)--(H);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\fill (H) circle (1pt) node[below] {$H$};
\\fill (K) circle (1pt) node[below] {$K$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(yB), str(xB), str(d)))

        # Nội dung lời giải
        loigiai = ('''Theo đề bài, điểm tiếp nước là gốc tọa độ $O(0;0)$, điểm xuất phát $B$ có hoành độ $x_B = %s$ và tung độ $y_B = %s$ nên $B(%s; %s)$. \\\\
Vì điểm $B$ thuộc nhánh parabol $y = ax^2$ ($x \\ge 0$) nên thay $x = %s, y = %s$, ta được: \\\\
$%s = a \\cdot %s^2 \\Leftrightarrow a = \\dfrac{%s}{%s} = %s$. \\\\
Suy ra phương trình của nhánh parabol máng trượt là $y = %s x^2$. \\\\
Tại vị trí $M$ cách điểm xuất phát $B$ một khoảng $%s\\text{ m}$ theo phương ngang, hoành độ của người trượt là: \\\\
$x_M = %s - %s = %s$. \\\\
Độ cao của người trượt so với mặt hồ tại vị trí $M$ là: \\\\
$y_M = %s \\cdot %s^2 = %s\\text{ (m)}$. \\\\
Vậy người trượt đang ở độ cao $%s\\text{ m}$ so với mặt hồ.'''
                   % (str(xB), latex(yB), str(xB), latex(yB),
                      str(xB), latex(yB),
                      latex(yB), str(xB), latex(yB), str(xB**2), latex(a),
                      latex(a),
                      str(d),
                      str(xB), str(d), str(xM),
                      latex(a), str(xM), latex(yM),
                      latex(yM)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (latex(yM))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
