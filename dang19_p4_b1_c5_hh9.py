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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang19_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(3, 12)
        s_max = 2 * (R**2)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (40:1.8);
\\coordinate (B) at (-40:1.8);
\\coordinate (C) at (220:1.8);
\\coordinate (D) at (140:1.8);
\\coordinate (H) at (1.379,0);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (-2.3,0)--(2.3,0) node[above] {$d$};
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt, dashed] (O)--(A);
\\draw[line width=1pt] (1.179,0)--(1.179,0.2)--(1.379,0.2);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above right] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[below left] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ cố định, đường thẳng $d$ đi qua $O$ và điểm $A$ di động trên đường tròn $(O)$ ($A \\notin d$). Gọi $B$ là điểm đối xứng với $A$ qua $d$; gọi $C$ và $D$ lần lượt là điểm đối xứng với $A$ và $B$ qua $O$ (như hình vẽ). \\\\
a) Gọi $H$ là hình chiếu vuông góc của $A$ trên $d$. Chứng minh rằng diện tích tứ giác $ABCD$ bằng $4 \\cdot OH \\cdot AH$. \\\\
b) Tìm vị trí của điểm $A$ trên đường tròn $(O)$ để tứ giác $ABCD$ có diện tích lớn nhất và tính giá trị lớn nhất đó.
%s''' % (R, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Theo tính chất đối xứng của đường tròn, tứ giác $ABCD$ là hình chữ nhật nhận $O$ làm tâm đối xứng và $d$ là đường trung trực của $AB, CD$.\\\\
Vì $H$ là hình chiếu vuông góc của $A$ trên $d$ nên $H$ là trung điểm của $AB$, do đó $AB = 2 \\cdot AH$.\\\\
Trong tam giác $ABD$, $O$ là trung điểm của $BD$ và $H$ là trung điểm của $AB$ nên $OH$ là đường trung bình của tam giác $ABD$, suy ra $AD = 2 \\cdot OH$.\\\\
Vậy diện tích hình chữ nhật $ABCD$ là:\\\\
$S_{ABCD} = AB \\cdot AD = (2 \\cdot AH) \\cdot (2 \\cdot OH) = 4 \\cdot OH \\cdot AH$.
\\item Xét tam giác $OHA$ vuông tại $H$, áp dụng định lí Pythagore ta có:\\\\
$OH^2 + AH^2 = OA^2 = R^2 = %s^2 = %s$.\\\\
Áp dụng bất đẳng thức $(OH - AH)^2 \\ge 0 \\Leftrightarrow 2 \\cdot OH \\cdot AH \\le OH^2 + AH^2$, suy ra:\\\\
$S_{ABCD} = 4 \\cdot OH \\cdot AH \\le 2(OH^2 + AH^2) = 2R^2 = 2 \\cdot %s^2 = %s\\text{ cm}^2$.\\\\
Dấu đẳng thức xảy ra khi và chỉ khi $OH = AH$, tức là tam giác $OHA$ vuông cân tại $H$, hay $\\widehat{AOH} = 45^{\\circ}$.\\\\
Vậy diện tích tứ giác $ABCD$ đạt giá trị lớn nhất bằng $%s\\text{ cm}^2$ khi điểm $A \\in (O)$ sao cho tia $OA$ tạo với đường thẳng $d$ một góc bằng $45^{\\circ}$ (khi đó $ABCD$ là hình vuông).
\\end{enumEX}''' % (R, R**2, R, s_max, s_max))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
