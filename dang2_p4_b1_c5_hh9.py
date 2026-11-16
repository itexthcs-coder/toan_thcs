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


def bt_dang2_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        xi = -random.randint(1, 3)
        yi = random.randint(1, 3)
        R = 5
        xa = xi + 3
        ya = yi + 4
        xb = 2 * xi - xa
        yb = 2 * yi - ya
        io_sq = xi**2 + yi**2

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (I) at (-0.4,0.8);
\\coordinate (A) at (0.68,2.24);
\\coordinate (B) at (-1.48,-0.64);
\\draw[->, line width=1pt] (-2.6,0)--(2.2,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-1.4)--(0,3.0) node[left] {$y$};
\\draw[line width=1pt] (I) circle (1.8);
\\draw[line width=1pt] (A)--(B);
\\fill (O) circle (1pt) node[below right] {$O$};
\\fill (I) circle (1pt) node[above left] {$I$};
\\fill (A) circle (1pt) node[above right] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho điểm $I(%s; %s)$ và đường tròn $(I; %s)$ (minh họa như hình vẽ). \\\\
a) Chứng minh rằng điểm $A(%s; %s)$ nằm trên đường tròn $(I; %s)$ và xét vị trí tương đối của gốc tọa độ $O(0; 0)$ đối với đường tròn $(I; %s)$. \\\\
b) Tìm tọa độ điểm $B$ đối xứng với điểm $A$ qua tâm $I$ và chứng minh điểm $B$ cũng nằm trên đường tròn $(I; %s)$.
%s''' % (xi, yi, R, xa, ya, R, R, R, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Áp dụng định lí Pythagore trong mặt phẳng tọa độ $Oxy$, khoảng cách từ tâm $I(%s; %s)$ đến điểm $A(%s; %s)$ là:\\\\
$IA = \\sqrt{(%s - (%s))^2 + (%s - %s)^2} = \\sqrt{3^2 + 4^2} = %s = R$.\\\\
Vì $IA = R$ nên điểm $A(%s; %s)$ nằm trên đường tròn $(I; %s)$.\\\\
Khoảng cách từ tâm $I(%s; %s)$ đến gốc tọa độ $O(0; 0)$ là:\\\\
$IO = \\sqrt{(0 - (%s))^2 + (0 - %s)^2} = \\sqrt{%s} < %s = R$.\\\\
Vậy gốc tọa độ $O(0; 0)$ nằm bên trong đường tròn $(I; %s)$.
\\item Vì điểm $B(x_B; y_B)$ đối xứng với điểm $A(%s; %s)$ qua tâm $I(%s; %s)$ nên $I$ là trung điểm của đoạn thẳng $AB$.\\\\
Suy ra $\\dfrac{%s + x_B}{2} = %s \\Rightarrow x_B = %s$ và $\\dfrac{%s + y_B}{2} = %s \\Rightarrow y_B = %s$. Vậy $B(%s; %s)$.\\\\
Ta có $IB = \\sqrt{(%s - (%s))^2 + (%s - %s)^2} = \\sqrt{(-3)^2 + (-4)^2} = %s = R$, do đó điểm $B$ cũng nằm trên đường tròn $(I; %s)$.
\\end{enumEX}''' % (xi, yi, xa, ya, xa, xi, ya, yi, R, xa, ya, R, xi, yi, xi, yi, io_sq, R, R, xa, ya, xi, yi, xa, xi, xb, ya, yi, yb, xb, yb, xb, xi, yb, yi, R, R))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
