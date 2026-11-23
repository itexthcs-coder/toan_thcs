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


def bt_dang14_p3_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = randint(6, 16)
        ac = randint(8, 18)
        if (ab * ac) % 2 != 0:
            ab += 1
        dien_tich = (ab * ac) // 2
        kq_str = str(dien_tich)

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (0,2.2);
\\coordinate (C) at (3.2,0);
\\coordinate (M) at (1.6,1.1);
\\coordinate (P) at (1.6,0);
\\coordinate (Q) at (1.6,-1.1);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(Q) (A)--(Q)--(C);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\draw[line width=1pt] (1.6,0.2)--(1.8,0.2)--(1.8,0);
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\fill (P) circle (1pt) node[below left] {$P$};
\\fill (Q) circle (1pt) node[below] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho $\\Delta ABC$ vuông tại $A$ có $AB = %s\\text{ cm}$ và $AC = %s\\text{ cm}$. Gọi $M$ là trung điểm của $BC$, $P$ là chân đường vuông góc hạ từ $M$ xuống $AC$. Lấy điểm $Q$ sao cho $P$ là trung điểm của $MQ$. Tính diện tích của hình thoi $AMCQ$ (đơn vị: $\\text{cm}^2$).%s'''
                         % (ab, ac, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''Vì $MP \\perp AC$ và $AB \\perp AC$ nên $MP // AB$.\\\\
Mà $M$ là trung điểm của $BC$ nên $MP$ là đường trung bình của $\\Delta ABC$, suy ra $MP = \\dfrac{AB}{2} = \\dfrac{%s}{2}\\text{ (cm)}$.\\\\
Vì $P$ là trung điểm của $MQ$ nên độ dài đường chéo $MQ = 2MP = AB = %s\\text{ cm}$.\\\\
Tứ giác $AMCQ$ là hình thoi có hai đường chéo $AC = %s\\text{ cm}$ và $MQ = %s\\text{ cm}$ vuông góc với nhau.\\\\
Vậy diện tích hình thoi $AMCQ$ là:\\\\
$S_{AMCQ} = \\dfrac{1}{2}AC \\cdot MQ = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2)$.'''
                   % (ab, ab, ac, ab, ac, ab, dien_tich))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
