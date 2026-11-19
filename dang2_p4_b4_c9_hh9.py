# -*- coding: utf-8 -*-
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


def bt_dang2_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ten_tg = random.choice(["ABC", "MNP"])
        a, b, c = ten_tg[0], ten_tg[1], ten_tg[2]
        anh_tg = "DEF" if ten_tg == "ABC" else "QRS"
        d, e, f = anh_tg[0], anh_tg[1], anh_tg[2]
        ten_lg = "%s%s%s%s%s%s" % (a, d, b, e, c, f)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (90:1.7);
\\coordinate (D) at (150:1.7);
\\coordinate (B) at (210:1.7);
\\coordinate (E) at (270:1.7);
\\coordinate (C) at (330:1.7);
\\coordinate (F) at (30:1.7);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (A)--(D)--(B)--(E)--(C)--(F)--cycle;
\\draw[line width=1pt, dashed] (A)--(B)--(C)--cycle;
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (D) circle (1pt) node[left] {$%s$};
\\fill (B) circle (1pt) node[left] {$%s$};
\\fill (E) circle (1pt) node[below] {$%s$};
\\fill (C) circle (1pt) node[right] {$%s$};
\\fill (F) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (a, d, b, e, c, f)

        noidungcauhoi = ('''Cho tam giác đều $%s$ nội tiếp đường tròn tâm $O$ theo thứ tự ngược chiều kim đồng hồ (như hình vẽ). Phép quay ngược chiều $60^\\circ$ tâm $O$ biến các điểm $%s, %s, %s$ lần lượt thành các điểm $%s, %s, %s$. Chứng minh rằng đa giác $%s$ là một lục giác đều. %s'''
                         % (ten_tg, a, b, c, d, e, f, ten_lg, hinh_tikz))

        loigiai = ('''Vì tam giác đều $%s$ nội tiếp đường tròn $(O)$ theo thứ tự ngược chiều kim đồng hồ nên ba cung nhỏ $%s%s, %s%s, %s%s$ đều có số đo bằng $\\frac{360^\\circ}{3} = 120^\\circ$. \\\\
Phép quay ngược chiều $60^\\circ$ tâm $O$ biến các điểm $%s, %s, %s$ lần lượt thành $%s, %s, %s$ nên các điểm $%s, %s, %s$ cùng nằm trên đường tròn $(O)$ và lần lượt là điểm chính giữa của các cung nhỏ $%s%s, %s%s, %s%s$. \\\\
Khi đó sáu điểm $%s, %s, %s, %s, %s, %s$ chia đường tròn $(O)$ thành $6$ cung nhỏ bằng nhau, mỗi cung có số đo bằng $60^\\circ$. \\\\
Suy ra sáu cạnh của đa giác lồi $%s$ bằng nhau:
$$%s%s = %s%s = %s%s = %s%s = %s%s = %s%s.$$
Mặt khác, mỗi góc trong của đa giác $%s$ là góc nội tiếp chắn $4$ cung nhỏ liên tiếp của $(O)$ nên đều có số đo bằng $\\frac{4 \\cdot 60^\\circ}{2} = 120^\\circ$. \\\\
Vậy đa giác $%s$ là một lục giác đều.'''
                   % (ten_tg, a, b, b, c, c, a,
                      a, b, c, d, e, f, d, e, f, a, b, b, c, c, a,
                      a, d, b, e, c, f, ten_lg,
                      a, d, d, b, b, e, e, c, c, f, f, a,
                      ten_lg, ten_lg))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
