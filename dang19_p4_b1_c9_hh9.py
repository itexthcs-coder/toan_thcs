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


def bt_dang19_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([6, 8, 10, 12, 14])
        BC = 2 * R
        AB = R

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (B) at (-2,0);\n'
            '\\coordinate (C) at (2,0);\n'
            '\\coordinate (A) at (120:2);\n'
            '\\coordinate (H) at ($(B)!(A)!(C)$);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(H);\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (B) circle (1pt) node[left] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (A) circle (1pt) node[above left] {$A$};\n'
            '\\fill (H) circle (1pt) node[below] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Một người thợ cơ khí cần cắt một tấm kim loại hình tam giác $ABC$ nội tiếp trong một phôi thép hình tròn tâm $O$, bán kính $R = %s\\text{ cm}$ sao cho cạnh $BC$ đi qua tâm $O$ và góc $\\widehat{ABC} = 60^\\circ$ như hình vẽ.\\\\'
            'a) Chứng minh tam giác $ABC$ là tam giác vuông và tính độ dài các cạnh $AB, AC$.\\\\'
            'b) Kẻ đường cao $AH$ của tam giác $ABC$. Tính độ dài đoạn thẳng $AH$ và diện tích tấm kim loại $ABC$.\\\\'
            'c) Tính bán kính $r$ của đường tròn nội tiếp tam giác $ABC$.\n%s'
            % (R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Vì $BC$ đi qua tâm $O$ của đường tròn $(O; %s\\text{ cm})$ nên $BC$ là đường kính và $BC = 2R = %s\\text{ cm}$. Góc nội tiếp $\\widehat{BAC}$ chắn nửa đường tròn đường kính $BC$ nên $\\widehat{BAC} = 90^\\circ$, do đó $\\triangle ABC$ vuông tại $A$.\\\\'
            'Xét $\\triangle ABC$ vuông tại $A$ có $\\widehat{ABC} = 60^\\circ$, ta có $AB = BC \\cdot \\cos 60^\\circ = %s \\cdot \\dfrac{1}{2} = %s\\text{ cm}$ và $AC = BC \\cdot \\sin 60^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2} = %s\\sqrt{3}\\text{ cm}$.\n'
            '\\item Trong $\\triangle ABC$ vuông tại $A$ có đường cao $AH$, ta có $AH = \\dfrac{AB \\cdot AC}{BC} = \\dfrac{%s \\cdot %s\\sqrt{3}}{%s} = %s\\sqrt{3}\\text{ cm}$.\\\\'
            'Diện tích tấm kim loại $ABC$ là $S_{ABC} = \\dfrac{1}{2} \\cdot AB \\cdot AC = \\dfrac{1}{2} \\cdot %s \\cdot %s\\sqrt{3} = %s\\sqrt{3}\\text{ cm}^2$.\n'
            '\\item Bán kính đường tròn nội tiếp $\\triangle ABC$ vuông tại $A$ là $r = \\dfrac{AB + AC - BC}{2} = \\dfrac{%s + %s\\sqrt{3} - %s}{2} = \\dfrac{%s\\sqrt{3} - %s}{2}\\text{ cm}$.\n'
            '\\end{enumEX}'
            % (R, BC, BC, AB, BC, R, AB, R, BC, R // 2, AB, R, (R * R) // 2, AB, R, BC, R, R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
