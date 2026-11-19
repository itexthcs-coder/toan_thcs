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


def bt_dang11_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(5, 13)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (-2,0);\n'
            '\\coordinate (B) at (2,0);\n'
            '\\coordinate (H) at (-0.8,0);\n'
            '\\coordinate (C) at (113.58:2);\n'
            '\\coordinate (D) at (-113.58:2);\n'
            '\\coordinate (M) at (45:2);\n'
            '\\coordinate (E) at (intersection of A--M and C--D);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (A)--(B) (C)--(D) (A)--(C) (A)--(M) (B)--(M) (C)--(M);\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[right] {$B$};\n'
            '\\fill (H) circle (1pt) node[below left] {$H$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (D) circle (1pt) node[below left] {$D$};\n'
            '\\fill (M) circle (1pt) node[above right] {$M$};\n'
            '\\fill (E) circle (1pt) node[above left] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho đường tròn $(O; %s\\text{ cm})$ đường kính $AB$. Vẽ dây cung $CD \\perp AB$ tại điểm $H$ nằm giữa $O$ và $A$. Lấy điểm $M$ thuộc cung nhỏ $BC$ ($M$ khác $B, C$), dây $AM$ cắt $CD$ tại $E$ như hình vẽ.\\\\'
            'a) Chứng minh $\\widehat{AMB} = 90^\\circ$ và $\\triangle AHE \\backsim \\triangle AMB$.\\\\'
            'b) Chứng minh $AE \\cdot AM = AH \\cdot AB = AC^2$.\\\\'
            'c) Chứng minh $\\widehat{ACE} = \\widehat{AMC}$ và tia $CB$ là tia phân giác của góc $\\widehat{DCM}$.\n%s'
            % (R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong đường tròn $(O)$, góc nội tiếp $\\widehat{AMB}$ chắn nửa đường tròn đường kính $AB$ nên $\\widehat{AMB} = 90^\\circ$. Xét $\\triangle AHE$ và $\\triangle AMB$ có $\\widehat{AHE} = \\widehat{AMB} = 90^\\circ$ và $\\widehat{A}$ chung nên $\\triangle AHE \\backsim \\triangle AMB$ (g.g).\n'
            '\\item Từ $\\triangle AHE \\backsim \\triangle AMB$, ta suy ra $\\dfrac{AH}{AM} = \\dfrac{AE}{AB} \\Rightarrow AE \\cdot AM = AH \\cdot AB$.\\\\'
            'Mặt khác, $\\widehat{ACB} = 90^\\circ$ (góc nội tiếp chắn nửa đường tròn đường kính $AB$) nên $\\triangle ABC$ vuông tại $C$ có đường cao $CH$, suy ra $AC^2 = AH \\cdot AB$. Vậy $AE \\cdot AM = AH \\cdot AB = AC^2$.\n'
            '\\item Vì $AB \\perp CD$ tại $H$ nên $AB$ là đường trung trực của $CD$, suy ra $AC = AD$ và $BC = BD$. Trong đường tròn $(O)$, hai dây cung bằng nhau căng hai cung bằng nhau nên $\\text{sđ}\\overparen{AC} = \\text{sđ}\\overparen{AD}$ và $\\text{sđ}\\overparen{BC} = \\text{sđ}\\overparen{BD}$.\\\\'
            'Do đó $\\widehat{ACE} = \\widehat{ACD} = \\widehat{AMC}$ (hai góc nội tiếp chắn hai cung bằng nhau $AD$ và $AC$), và $\\widehat{DCB} = \\widehat{MCB}$ (hai góc nội tiếp chắn hai cung bằng nhau $BD$ và $BC$), suy ra tia $CB$ là tia phân giác của góc $\\widehat{DCM}$.\n'
            '\\end{enumEX}'
            
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
