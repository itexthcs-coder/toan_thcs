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


def bt_dang8_p3_b3_c7_ds8(self):
    # Dạng 8: Tính diện tích hình chữ nhật trên mặt phẳng tọa độ Oxy
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        x1 = random.randint(-6, -1)
        x2 = random.randint(2, 8)
        y1 = random.randint(2, 7)
        y2 = random.randint(-6, -1)

        ab = x2 - x1
        bc = y1 - y2
        dt = ab * bc
        kq_str = str(dt)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (-2.5,0) -- (3.5,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-2.2) -- (0,2.8) node[left] {$y$};
\\draw[line width=1pt] (-1.5,2) -- (2.5,2) -- (2.5,-1.5) -- (-1.5,-1.5) -- cycle;
\\fill (-1.5,2) circle (1pt) node[above left] {$A$};
\\fill (2.5,2) circle (1pt) node[above right] {$B$};
\\fill (2.5,-1.5) circle (1pt) node[below right] {$C$};
\\fill (-1.5,-1.5) circle (1pt) node[below left] {$D$};
\\fill (0,0) circle (1pt) node[below left] {$O$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho hình chữ nhật $ABCD$ có các cạnh song song với các trục tọa độ (minh họa như hình vẽ). Biết tọa độ ba đỉnh là $A(%s;\\, %s)$, $B(%s;\\, %s)$ và $C(%s;\\, %s)$. Tính diện tích của hình chữ nhật $ABCD$.
%s'''
                         % (x1, y1, x2, y1, x2, y2, tikz_code))

        loigiai = ('''Vì $A(%s;\\, %s)$ và $B(%s;\\, %s)$ có cùng tung độ bằng $%s$ nên đoạn thẳng $AB$ song song với trục hoành $Ox$. \\\\
Độ dài cạnh $AB$ là: $AB = |%s - (%s)| = %s$. \\\\
Vì $B(%s;\\, %s)$ và $C(%s;\\, %s)$ có cùng hoành độ bằng $%s$ nên đoạn thẳng $BC$ song song với trục tung $Oy$. \\\\
Độ dài cạnh $BC$ là: $BC = |%s - (%s)| = %s$. \\\\
Vậy diện tích của hình chữ nhật $ABCD$ là: $S_{ABCD} = AB \\cdot BC = %s \\cdot %s = %s$.'''
                   % (x1, y1, x2, y1, y1,
                      x2, x1, ab,
                      x2, y1, x2, y2, x2,
                      y1, y2, bc,
                      ab, bc, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
