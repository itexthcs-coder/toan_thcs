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


def bt_dang18_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        AB = random.choice([4, 6, 8, 10])
        AC = 2 * AB

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (M) at (90:2);\n'
            '\\coordinate (D) at (-90:2);\n'
            '\\coordinate (A) at (210:2);\n'
            '\\coordinate (C) at (330:2);\n'
            '\\coordinate (B) at (0,-1);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (A)--(C) (M)--(A) (M)--(C) (M)--(D);\n'
            '\\draw[line width=1pt, dashed] (O)--(A) (O)--(C);\n'
            '\\fill (O) circle (1pt) node[right] {$O$};\n'
            '\\fill (M) circle (1pt) node[above] {$M$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Dọc theo một bờ biển thẳng có ba ngọn hải đăng đặt tại ba điểm $A, B, C$ theo thứ tự đó sao cho $AB = %s\\text{ km}$ và $BC = %s\\text{ km}$. Một con tàu ở ngoài khơi tại vị trí $M$ đo được góc nhìn tới hai ngọn hải đăng $A, B$ là $\\widehat{AMB} = 30^\\circ$ và góc nhìn tới hai ngọn hải đăng $B, C$ là $\\widehat{BMC} = 30^\\circ$ như hình vẽ.\\\\'
            'a) Gọi $(O)$ là đường tròn ngoại tiếp tam giác $AMC$. Chứng minh tia $MB$ là tia phân giác của góc $\\widehat{AMC}$ và cắt $(O)$ tại điểm chính giữa $D$ của cung $AC$ (không chứa $M$).\\\\'
            'b) Tính bán kính $R$ của đường tròn $(O)$ ngoại tiếp tam giác $AMC$.\\\\'
            'c) Biết tàu đang ở vị trí sao cho $MA = MC$, hãy tính khoảng cách từ con tàu $M$ đến ngọn hải đăng $B$.\n%s'
            % (AB, AB, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Vì $B$ nằm giữa $A$ và $C$ nên tia $MB$ nằm giữa hai tia $MA, MC$, lại có $\\widehat{AMB} = \\widehat{BMC} = 30^\\circ$ nên tia $MB$ là tia phân giác của góc $\\widehat{AMC}$.\\\\'
            'Trong đường tròn $(O)$, hai góc nội tiếp $\\widehat{AMD}$ và $\\widehat{CMD}$ bằng nhau nên chắn hai cung bằng nhau: $\\text{sđ}\\overset\\frown{AD} = \\text{sđ}\\overset\\frown{CD}$, do đó $D$ là điểm chính giữa của cung $AC$ (không chứa $M$).\n'
            '\\item Ta có $\\widehat{AMC} = \\widehat{AMB} + \\widehat{BMC} = 30^\\circ + 30^\\circ = 60^\\circ$. Trong đường tròn $(O)$, góc nội tiếp $\\widehat{AMC} = 60^\\circ$ chắn cung $AC$ nên góc ở tâm $\\widehat{AOC} = 2\\widehat{AMC} = 120^\\circ$.\\\\'
            'Xét $\\triangle OAC$ cân tại $O$ có $\\widehat{AOC} = 120^\\circ$ và đáy $AC = AB + BC = %s + %s = %s\\text{ km}$. Kẻ $OI \\perp AC$ tại trung điểm $I$ của $AC$, ta có $AI = %s\\text{ km}$ và $\\widehat{AOI} = 60^\\circ$, suy ra $R = OA = \\dfrac{AI}{\\sin 60^\\circ} = \\dfrac{%s}{\\dfrac{\\sqrt{3}}{2}} = \\dfrac{%s\\sqrt{3}}{3}\\text{ km}$.\n'
            '\\item Khi $MA = MC$, $\\triangle AMC$ cân tại $M$ có $\\widehat{AMC} = 60^\\circ$ nên $\\triangle AMC$ là tam giác đều cạnh $AC = %s\\text{ km}$.\\\\'
            'Khi đó đường phân giác $MB$ đồng thời là đường cao của $\\triangle AMC$ đều, suy ra $MB = \\dfrac{AC\\sqrt{3}}{2} = \\dfrac{%s\\sqrt{3}}{2} = %s\\sqrt{3}\\text{ km}$.\n'
            '\\end{enumEX}'
            % (AB, AB, AC, AB, AB, 2 * AB, AC, AC, AB)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n' + str(noidungcauhoi) +
            '\\loigiai{ \n' + str(loigiai) + '}\n'
            '\\end{ex}\n \\end{minipage} \n\n')
    return content
