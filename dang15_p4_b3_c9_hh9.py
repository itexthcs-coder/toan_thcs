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


def bt_dang15_p4_b3_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r_val = randint(3, 8)
        op_val = 2 * r_val
        bc_val = r_val

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (P) at (-3,0);
\\coordinate (A) at (120:1.5);
\\coordinate (B) at (-120:1.5);
\\coordinate (C) at (-60:1.5);
\\draw[line width=1pt] (O) circle (1.5);
\\draw[line width=1pt] (P)--(A)--(C)--(B)--(P);
\\draw[line width=1pt] (O)--(B);
\\draw[line width=1pt, dashed] (P)--(O);
\\fill (O) circle (1pt) node[above right] {$O$};
\\fill (P) circle (1pt) node[left] {$P$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Từ điểm $P$ nằm ngoài đường tròn $(O; %s\\text{ cm})$ sao cho $OP = %s\\text{ cm}$, kẻ hai tiếp tuyến $PA, PB$ với đường tròn ($A, B$ là các tiếp điểm). Vẽ đường kính $AC$ của đường tròn $(O)$. \\\\
a) Chứng minh rằng tứ giác $PAOB$ nội tiếp đường tròn đường kính $OP$. \\\\
b) Chứng minh rằng $BC // OP$ và tính độ dài đoạn thẳng $BC$.%s''' % (r_val, op_val, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $PA, PB$ là các tiếp tuyến của $(O)$ tại $A$ và $B$ nên $\\widehat{PAO} = \\widehat{PBO} = 90^\\circ$.\\\\
Gọi $I$ là trung điểm của đoạn thẳng $OP$. Các tam giác vuông $PAO$ và $PBO$ có chung cạnh huyền $OP$ nên $IA = IB = IO = IP = \\dfrac{OP}{2}$.\\\\
Suy ra bốn điểm $P, A, O, B$ cùng nằm trên đường tròn tâm $I$ đường kính $OP$.
\\item Xét đường tròn $(O)$ có $AC$ là đường kính và $B \\in (O)$ nên góc nội tiếp chắn nửa đường tròn $\\widehat{ABC} = 90^\\circ$, suy ra $BC \\perp AB$.\\\\
Mặt khác, vì $PA = PB$ và $OA = OB$ nên $OP$ là đường trung trực của đoạn thẳng $AB$, suy ra $OP \\perp AB$.\\\\
Từ đó suy ra $BC // OP$ (cùng vuông góc với $AB$).\\\\
Trong tam giác $PAO$ vuông tại $A$, ta có $\\sin \\widehat{APO} = \\dfrac{OA}{OP} = \\dfrac{%s}{%s} = \\dfrac{1}{2} \\Rightarrow \\widehat{APO} = 30^\\circ \\Rightarrow \\widehat{AOP} = 60^\\circ$.\\\\
Vì $OP$ là tia phân giác của $\\widehat{AOB}$ nên $\\widehat{AOB} = 120^\\circ \\Rightarrow \\widehat{BOC} = 180^\\circ - 120^\\circ = 60^\\circ$.\\\\
Tam giác $OBC$ cân tại $O$ ($OB = OC = R$) có $\\widehat{BOC} = 60^\\circ$ nên là tam giác đều, suy ra $BC = R = %s\\text{ (cm)}$.
\\end{enumEX}''' % (r_val, op_val, bc_val))

    # Xuất câu hỏi và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
