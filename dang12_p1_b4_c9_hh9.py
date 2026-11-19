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


def bt_dang12_p1_b4_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ds_n = [(5, "ngũ giác đều"), (6, "lục giác đều"), (8, "bát giác đều"), (9, "đa giác đều $9$ cạnh"), (10, "đa giác đều $10$ cạnh"), (12, "đa giác đều $12$ cạnh")]
        n, ten_goi = random.choice(ds_n)
        goc_tam = 360 // n
        goc_trong = 180 - goc_tam

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\foreach \\i in {1,...,8} {
    \\coordinate (P\\i) at (45*\\i:1.7);
}
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (P1)--(P2)--(P3)--(P4)--(P5)--(P6)--(P7)--(P8)--cycle;
\\draw[line width=1pt, dashed] (O)--(P1) (O)--(P2) (O)--(P3);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (P1) circle (1pt) node[above right] {$A$};
\\fill (P2) circle (1pt) node[above] {$B$};
\\fill (P3) circle (1pt) node[above left] {$C$};
\\end{tikzpicture}
\\end{center}'''

        du = [
            '$%s^\\circ$' % (goc_trong),
        ]
        da = random.choice(du)
        s = [
            '$%s^\\circ$' % (goc_tam),
            '$%s^\\circ$' % (goc_trong - 15),
            '$%s^\\circ$' % (goc_trong + 12),
            '$%s^\\circ$' % (180 - goc_tam // 2),
            '$%s^\\circ$' % (goc_tam * 2)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho một %s nội tiếp đường tròn tâm $O$ (hình vẽ minh họa trường hợp bát giác đều). Mỗi góc trong của %s đó có số đo bằng bao nhiêu độ? %s'''
                         % (ten_goi, ten_goi, hinh_tikz))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''Xét %s có $%s$ cạnh nội tiếp đường tròn tâm $O$. Ba đỉnh liên tiếp $A, B, C$ tạo thành hai tam giác cân bằng nhau là $\\triangle OAB$ và $\\triangle OBC$ (vì $OA = OB = OC = R$ và $AB = BC$). \\
Góc ở tâm chắn mỗi cạnh bằng:
$$\\widehat{AOB} = \\widehat{BOC} = \\frac{360^\\circ}{%s} = %s^\\circ.$$
Trong tam giác cân $OAB$ cân tại $O$, ta có:
$$\\widehat{OBA} = \\frac{180^\\circ - %s^\\circ}{2}.$$
Tương tự $\\widehat{OBC} = \\frac{180^\\circ - %s^\\circ}{2}$. Do đó số đo mỗi góc trong của %s là:
$$\\widehat{ABC} = \\widehat{OBA} + \\widehat{OBC} = 180^\\circ - %s^\\circ = %s^\\circ.$$'''
                   % (ten_goi, n, n, goc_tam, goc_tam, goc_tam, ten_goi, goc_tam, goc_trong))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
