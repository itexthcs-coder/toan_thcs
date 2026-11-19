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


def bt_dang3_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([4, 6, 8, 10, 12])

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (-2,0);\n'
            '\\coordinate (B) at (2,0);\n'
            '\\coordinate (I) at (-1,0);\n'
            '\\coordinate (C) at (120:2);\n'
            '\\coordinate (D) at (-120:2);\n'
            '\\coordinate (M) at (45:2);\n'
            '\\coordinate (K) at (intersection of A--M and C--D);\n'
            '\\coordinate (P) at (intersection of B--M and C--D);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (A)--(B) (C)--(D) (A)--(C)--(B) (A)--(D) (A)--(M) (B)--(P) (I)--(P);\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[right] {$B$};\n'
            '\\fill (I) circle (1pt) node[below left] {$I$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (D) circle (1pt) node[below left] {$D$};\n'
            '\\fill (M) circle (1pt) node[above right] {$M$};\n'
            '\\fill (K) circle (1pt) node[left] {$K$};\n'
            '\\fill (P) circle (1pt) node[above left] {$P$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho đường tròn $(O; %s\\text{ cm})$ đường kính $AB$. Gọi $I$ là trung điểm của đoạn thẳng $OA$. Qua $I$ kẻ dây cung $CD \\perp AB$ tại $I$. Lấy điểm $M$ nằm trên cung nhỏ $BC$ ($M$ khác $B, C$), dây $AM$ cắt $CD$ tại $K$ như hình vẽ.\\'
            'a) Chứng minh tam giác $ACD$ là tam giác đều.\\'
            'b) Chứng minh $\\triangle AIK \\backsim \\triangle AMB$ và tính tích $AK \\cdot AM$.\\'
            'c) Tia $BM$ cắt đường thẳng $CD$ tại $P$. Chứng minh $IC^2 = IK \\cdot IP$.\n%s'
            % (R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Vì $CD \\perp AB$ tại trung điểm $I$ của $OA$ nên $CD$ là đường trung trực của $OA$, suy ra $CA = CO$. Mà $OA = OC = %s\\text{ cm}$ nên $\\triangle OAC$ đều, do đó $\\widehat{CAO} = 60^\\circ$. Tương tự $\\triangle OAD$ đều nên $\\widehat{DAO} = 60^\\circ$, suy ra $\\widehat{CAD} = 120^\\circ$? Chính xác hơn: $AC = AD$ (do $AB$ là đường trung trực của $CD$) và $\\widehat{CAD} = 60^\\circ$ nếu $I$ là trung điểm $OB$, còn ở đây $\\widehat{CAO} = 60^\\circ \\Rightarrow \\widehat{CAB} = 60^\\circ$ và $AC = AD$ nên $\\triangle ACD$ cân tại $A$ có $\\widehat{CAD} = 120^\\circ$? Không, $\\widehat{CAD} = \\widehat{CAI} + \\widehat{DAI} = 60^\\circ + 60^\\circ = 120^\\circ$ khi $\\triangle OAC$ đều, còn $\\triangle CBD$ mới là tam giác đều vì $\\widehat{CBA} = 30^\\circ \\Rightarrow \\widehat{CBD} = 60^\\circ$. Vậy $\\triangle CBD$ là tam giác đều (và $\\triangle OAC, \\triangle OAD$ đều).\n'
            '\\item Trong đường tròn $(O)$, góc nội tiếp $\\widehat{AMB}$ chắn nửa đường tròn đường kính $AB$ nên $\\widehat{AMB} = 90^\\circ$. Xét $\\triangle AIK$ và $\\triangle AMB$ có $\\widehat{AIK} = \\widehat{AMB} = 90^\\circ$ và $\\widehat{A}$ chung nên $\\triangle AIK \\backsim \\triangle AMB$ (g.g).\\'
            'Suy ra $\\dfrac{AI}{AM} = \\dfrac{AK}{AB} \\Rightarrow AK \\cdot AM = AI \\cdot AB = \\dfrac{%s}{2} \\cdot (2 \\cdot %s) = %s^2 = %s\\text{ cm}^2$.\n'
            '\\item Xét $\\triangle AIK$ và $\\triangle PIB$ có $\\widehat{AIK} = \\widehat{PIB} = 90^\\circ$ và $\\widehat{AKI} = \\widehat{PBI}$ (cùng phụ với $\\widehat{IAB}$) nên $\\triangle AIK \\backsim \\triangle PIB$ (g.g), suy ra $IK \\cdot IP = IA \\cdot IB$.\\'
            'Mặt khác, $\\widehat{ACB} = 90^\\circ$ (góc nội tiếp chắn nửa đường tròn) nên trong $\\triangle ABC$ vuông tại $C$ có đường cao $CI$, ta có $IC^2 = IA \\cdot IB$. Vậy $IC^2 = IK \\cdot IP$.\n'
            '\\end{enumEX}'
            % (R, R, R, R, R * R)
        )
        # Sửa ý a) hỏi chứng minh tam giác CBD đều để khớp 100% hình học
        noidungcauhoi = (
            'Cho đường tròn $(O; %s\\text{ cm})$ đường kính $AB$. Gọi $I$ là trung điểm của đoạn thẳng $OA$. Qua $I$ kẻ dây cung $CD \\perp AB$ tại $I$. Lấy điểm $M$ nằm trên cung nhỏ $BC$ ($M$ khác $B, C$), dây $AM$ cắt $CD$ tại $K$ như hình vẽ.\\'
            'a) Chứng minh tam giác $CBD$ là tam giác đều.\\'
            'b) Chứng minh $\\triangle AIK \\backsim \\triangle AMB$ và tính tích $AK \\cdot AM$.\\'
            'c) Tia $BM$ cắt đường thẳng $CD$ tại $P$. Chứng minh $IC^2 = IK \\cdot IP$.\n%s'
            % (R, hinh_ve)
        )
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Vì $CD \\perp AB$ tại trung điểm $I$ của $OA$ nên $CD$ là đường trung trực của $OA$, suy ra $CA = CO = OA = %s\\text{ cm}$, do đó $\\triangle OAC$ đều và $\\widehat{CAB} = 60^\\circ$.\\'
            'Vì $\\widehat{ACB} = 90^\\circ$ (góc nội tiếp chắn nửa đường tròn đường kính $AB$) nên $\\widehat{CBA} = 90^\\circ - 60^\\circ = 30^\\circ$. Lại có $AB \\perp CD$ tại $I$ nên $AB$ là đường trung trực của $CD$, suy ra $BC = BD$ và $\\widehat{CBD} = 2\\widehat{CBA} = 60^\\circ$. Vậy $\\triangle CBD$ là tam giác đều.\n'
            '\\item Trong đường tròn $(O)$, góc nội tiếp $\\widehat{AMB}$ chắn nửa đường tròn đường kính $AB$ nên $\\widehat{AMB} = 90^\\circ$. Xét $\\triangle AIK$ và $\\triangle AMB$ có $\\widehat{AIK} = \\widehat{AMB} = 90^\\circ$ và $\\widehat{A}$ chung nên $\\triangle AIK \\backsim \\triangle AMB$ (g.g).\\'
            'Suy ra $\\dfrac{AI}{AM} = \\dfrac{AK}{AB} \\Rightarrow AK \\cdot AM = AI \\cdot AB = \\dfrac{%s}{2} \\cdot (2 \\cdot %s) = %s^2 = %s\\text{ cm}^2$.\n'
            '\\item Xét $\\triangle AIK$ và $\\triangle PIB$ có $\\widehat{AIK} = \\widehat{PIB} = 90^\\circ$ và $\\widehat{AKI} = \\widehat{PBI}$ (cùng phụ với $\\widehat{IAB}$) nên $\\triangle AIK \\backsim \\triangle PIB$ (g.g), suy ra $IK \\cdot IP = IA \\cdot IB$.\\'
            'Mặt khác, trong $\\triangle ABC$ vuông tại $C$ có đường cao $CI$, ta có $IC^2 = IA \\cdot IB$. Vậy $IC^2 = IK \\cdot IP$.\n'
            '\\end{enumEX}'
            % (R, R, R, R, R * R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
