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


def bt_dang1_p3_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        R = random.randint(5, 10)
        oa = R - 2
        ob = R
        oc_str = '%s,5' % (R + 1)
        od_str = '%s,9' % (R - 1)
        oe_str = '%s,1' % R
        kq_str = '3'

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (0.8,0.4);
\\coordinate (B) at (30:1.7);
\\coordinate (C) at (2.4,0);
\\coordinate (D) at (140:1.55);
\\coordinate (E) at (-20:1.95);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (O)--(B) node[midway, above left] {$R$};
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[below] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\fill (E) circle (1pt) node[below right] {$E$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ và năm điểm $A, B, C, D, E$ lần lượt có khoảng cách tới tâm $O$ là $OA = %s\\text{ cm}$, $OB = %s\\text{ cm}$, $OC = %s\\text{ cm}$, $OD = %s\\text{ cm}$, $OE = %s\\text{ cm}$ (minh họa như hình vẽ). Có bao nhiêu điểm trong năm điểm đã cho thuộc hình tròn $(O; %s\\text{ cm})$?
%s''' % (R, oa, ob, oc_str, od_str, oe_str, R, tikz_code))

        loigiai = ('''Hình tròn $(O; %s\\text{ cm})$ gồm các điểm nằm trên và nằm trong đường tròn $(O; %s\\text{ cm})$, tức là các điểm $M$ thỏa mãn $OM \\le %s\\text{ cm}$.\\\\
So sánh khoảng cách từ tâm $O$ đến năm điểm đã cho với bán kính $R = %s\\text{ cm}$:\\\\
- $OA = %s\\text{ cm} < %s\\text{ cm}$ nên điểm $A$ nằm trong đường tròn $(O)$.\\\\
- $OB = %s\\text{ cm} = R$ nên điểm $B$ nằm trên đường tròn $(O)$.\\\\
- $OC = %s\\text{ cm} > %s\\text{ cm}$ nên điểm $C$ nằm ngoài đường tròn $(O)$.\\\\
- $OD = %s\\text{ cm} < %s\\text{ cm}$ nên điểm $D$ nằm trong đường tròn $(O)$.\\\\
- $OE = %s\\text{ cm} > %s\\text{ cm}$ nên điểm $E$ nằm ngoài đường tròn $(O)$.\\\\
Vậy có $3$ điểm ($A, B, D$) thuộc hình tròn $(O; %s\\text{ cm})$.''' % (R, R, R, R, oa, R, ob, oc_str, R, od_str, R, oe_str, R, R))

        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
