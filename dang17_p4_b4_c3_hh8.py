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


def bt_dang17_p4_b4_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.4);
\\coordinate (B) at (4.2,2.4);
\\coordinate (C) at (4.2,0);
\\coordinate (D) at (0,0);
\\coordinate (M) at (1.5,1.5);
\\coordinate (H) at (1.5,2.4);
\\coordinate (K) at (1.5,0);
\\coordinate (P) at (0,1.5);
\\coordinate (Q) at (4.2,1.5);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(A) (M)--(B) (M)--(C) (M)--(D);
\\draw[line width=1pt, dashed] (H)--(K) (P)--(Q);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\fill (H) circle (1pt) node[above] {$H$};
\\fill (K) circle (1pt) node[below] {$K$};
\\fill (P) circle (1pt) node[left] {$P$};
\\fill (Q) circle (1pt) node[right] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hình chữ nhật $ABCD$ và một điểm $M$ bất kì nằm trong hình chữ nhật. Kẻ $MH \\perp AB$ tại $H$, $MK \\perp CD$ tại $K$, $MP \\perp AD$ tại $P$, $MQ \\perp BC$ tại $Q$. \\\\
a) Chứng minh các tứ giác $AHMP$, $BHMQ$, $CKMQ$, $DKMP$ là các hình chữ nhật. \\\\
b) Chứng minh rằng $MA^2 + MC^2 = MB^2 + MD^2$. %s'''
                         % (hinh_ve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tứ giác $AHMP$ có $\\widehat{HAP} = 90^\\circ$ ($ABCD$ là hình chữ nhật), $\\widehat{AHM} = 90^\\circ$ ($MH \\perp AB$) và $\\widehat{APM} = 90^\\circ$ ($MP \\perp AD$). \\\\
Vì có ba góc vuông nên tứ giác $AHMP$ là hình chữ nhật. \\\\
Chứng minh hoàn toàn tương tự, các tứ giác $BHMQ$, $CKMQ$ và $DKMP$ đều có ba góc vuông nên chúng đều là các hình chữ nhật.
\\item Từ các hình chữ nhật $AHMP$, $BHMQ$, $CKMQ$, $DKMP$, ta có các cặp cạnh đối bằng nhau: \\\\
$MP = AH$, $MH = AP$, $MQ = BH$, $MK = DP = CQ$. \\\\
Áp dụng định lí Pythagore vào các tam giác vuông $\\triangle AMP$, $\\triangle CMQ$, $\\triangle BMH$, $\\triangle DMP$, ta có: \\\\
$MA^2 + MC^2 = (MP^2 + AP^2) + (MQ^2 + CQ^2) = AH^2 + AP^2 + BH^2 + DP^2$. \\\\
$MB^2 + MD^2 = (MH^2 + BH^2) + (MP^2 + DP^2) = AP^2 + BH^2 + AH^2 + DP^2$. \\\\
Vậy $MA^2 + MC^2 = MB^2 + MD^2$.
\\end{enumEX}''')
    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
