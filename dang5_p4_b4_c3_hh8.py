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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang5_p4_b4_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = random.choice([('A', 'B', 'C', 'D', 'O'), ('M', 'N', 'P', 'Q', 'I')])
        dA, dB, dC, dD, dO = bo_diem

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (%s) at (0,2.2);
\\coordinate (%s) at (4,2.2);
\\coordinate (%s) at (4,0);
\\coordinate (%s) at (0,0);
\\coordinate (%s) at (2,1.1);
\\draw[line width=1pt] (%s)--(%s)--(%s)--(%s)--cycle (%s)--(%s) (%s)--(%s);
\\fill (%s) circle (1pt) node[above left] {$%s$};
\\fill (%s) circle (1pt) node[above right] {$%s$};
\\fill (%s) circle (1pt) node[below right] {$%s$};
\\fill (%s) circle (1pt) node[below left] {$%s$};
\\fill (%s) circle (1pt) node[above=2pt] {$%s$};
\\end{tikzpicture}
\\end{center}'''
        % (dA, dB, dC, dD, dO, dA, dB, dC, dD, dA, dC, dB, dD, dA, dA, dB, dB, dC, dC, dD, dD, dO, dO))

        noidungcauhoi = ('''Cho hình bình hành $%s%s%s%s$ có hai đường chéo $%s%s$ và $%s%s$ cắt nhau tại $%s$. Biết $\\triangle %s%s%s$ là tam giác cân tại $%s$. Chứng minh rằng hình bình hành $%s%s%s%s$ là hình chữ nhật. %s'''
                         % (dA, dB, dC, dD, dA, dC, dB, dD, dO, dO, dA, dB, dO, dA, dB, dC, dD, hinh_ve))

        loigiai = ('''Vì $%s%s%s%s$ là hình bình hành nên hai đường chéo $%s%s$ và $%s%s$ cắt nhau tại trung điểm $%s$ của mỗi đường. \\\\
Suy ra $%s%s = 2%s%s$ và $%s%s = 2%s%s$. \\\\
Mặt khác, $\\triangle %s%s%s$ cân tại $%s$ (giả thiết) nên $%s%s = %s%s$. \\\\
Do đó $%s%s = 2%s%s = 2%s%s = %s%s$. \\\\
Hình bình hành $%s%s%s%s$ có hai đường chéo $%s%s$ và $%s%s$ bằng nhau nên theo Định lí 2, $%s%s%s%s$ là hình chữ nhật.'''
                   % (dA, dB, dC, dD, dA, dC, dB, dD, dO,
                      dA, dC, dO, dA, dB, dD, dO, dB,
                      dO, dA, dB, dO, dO, dA, dO, dB,
                      dA, dC, dO, dA, dO, dB, dB, dD,
                      dA, dB, dC, dD, dA, dC, dB, dD, dA, dB, dC, dD))
    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
