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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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


def bt_dang9_p3_b3_c7_ds8(self):
    # Dạng 9: Tính độ dài đoạn thẳng nối hai điểm nằm trên hai trục tọa độ
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        bo_ba = random.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15)])
        a, b, c = bo_ba
        sx = random.choice([-1, 1])
        sy = random.choice([-1, 1])
        xp = sx * a
        yq = sy * b
        kq_str = str(c)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.75, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (-2.5,0) -- (2.5,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-1.2) -- (0,2.8) node[left] {$y$};
\\draw[line width=1pt] (-1.8,0) -- (0,2.2);
\\fill (0,0) circle (1pt) node[below right] {$O$};
\\fill (-1.8,0) circle (1pt) node[below] {$P$};
\\fill (0,2.2) circle (1pt) node[right] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $P(%s;\\, 0)$ và $Q(0;\\, %s)$ (minh họa như hình vẽ). Tính độ dài đoạn thẳng $PQ$.
%s'''
                         % (xp, yq, tikz_code))

        loigiai = ('''Điểm $P(%s;\\, 0)$ nằm trên trục hoành $Ox$ nên khoảng cách từ $P$ đến gốc tọa độ $O$ là $OP = |%s| = %s$. \\\\
Điểm $Q(0;\\, %s)$ nằm trên trục tung $Oy$ nên khoảng cách từ $Q$ đến gốc tọa độ $O$ là $OQ = |%s| = %s$. \\\\
Vì hai trục tọa độ $Ox$ và $Oy$ vuông góc với nhau tại $O$ nên tam giác $OPQ$ vuông tại $O$. \\\\
Áp dụng định lí Pythagore vào tam giác $OPQ$ vuông tại $O$, ta có: \\\\
$PQ^2 = OP^2 + OQ^2 = %s^2 + %s^2 = %s + %s = %s$. \\\\
Suy ra $PQ = \\sqrt{%s} = %s$.'''
                   % (xp, xp, a,
                      yq, yq, b,
                      a, b, a**2, b**2, c**2,
                      c**2, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
