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


def bt_dang9_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ae = randint(2, 8)
        bc = randint(6, 15)
        chu_vi = 2 * (ae + bc)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ có chu vi bằng $%s\\text{ cm}$ và độ dài cạnh $BC = %s\\text{ cm}$. Đường tròn $(I)$ tiếp xúc với cả ba cạnh $BC$, $CA$, $AB$ của tam giác $ABC$ lần lượt tại các tiếp điểm $D$, $E$, $F$. Tính độ dài đoạn thẳng $AE$. \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (B) at (0,0);
            \\coordinate (C) at (4,0);
            \\coordinate (A) at (1.3,3);
            \\coordinate (I) at (1.68,1.03);
            \\coordinate (D) at (1.68,0);
            \\coordinate (E) at (2.49,1.67);
            \\coordinate (F) at (0.73,1.68);
            \\draw[line width=1pt] (A)--(B)--(C)--cycle;
            \\draw[line width=1pt] (I) circle (1.03);
            \\fill (A) circle (1pt) node[above] {$A$};
            \\fill (B) circle (1pt) node[below left] {$B$};
            \\fill (C) circle (1pt) node[below right] {$C$};
            \\fill (I) circle (1pt) node[below right] {$I$};
            \\fill (D) circle (1pt) node[below] {$D$};
            \\fill (E) circle (1pt) node[above right] {$E$};
            \\fill (F) circle (1pt) node[above left] {$F$};
        \\end{tikzpicture}
        \\end{center}'''
        %(latex(chu_vi), latex(bc)))

        # Nội dung lời giải
        loigiai = ('''Vì đường tròn $(I)$ tiếp xúc với các cạnh $BC$, $CA$, $AB$ lần lượt tại $D$, $E$, $F$ nên theo tính chất của hai tiếp tuyến cắt nhau xuất phát từ các đỉnh $A$, $B$, $C$ tới đường tròn $(I)$, ta có: \\\\
        $AE = AF$, $BD = BF$ và $CD = CE$. \\\\
        Chu vi của tam giác $ABC$ là: \\\\
        $AB + BC + CA = (AF + BF) + (BD + CD) + (CE + AE)$ \\\\
        $= (AE + AF) + (BD + BF) + (CD + CE)$ \\\\
        $= 2AE + 2BD + 2CD = 2AE + 2(BD + CD) = 2AE + 2BC$. \\\\
        Thay chu vi tam giác $ABC$ bằng $%s\\text{ cm}$ và $BC = %s\\text{ cm}$ vào biểu thức trên, ta được: \\\\
        $2AE + 2 \\cdot %s = %s \\Rightarrow 2AE = %s - %s = %s \\Rightarrow AE = %s\\text{ (cm)}$. \\\\
        Vậy độ dài đoạn thẳng $AE = %s\\text{ cm}$.'''
        %(latex(chu_vi), latex(bc), latex(bc), latex(chu_vi), latex(chu_vi), latex(2*bc), latex(2*ae), latex(ae), latex(ae)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
