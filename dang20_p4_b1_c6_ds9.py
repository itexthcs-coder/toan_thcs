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


def bt_dang20_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [(Decimal('1.2'), Decimal('0.3'), Decimal('0.6'), Rational(5, 6), Decimal('0.3')),
                 (Decimal('1.6'), Decimal('0.4'), Decimal('0.8'), Rational(5, 8), Decimal('0.4')),
                 (Decimal('2.0'), Decimal('0.5'), Decimal('1.0'), Rational(1, 2), Decimal('0.5')),
                 (Decimal('2.4'), Decimal('0.4'), Decimal('1.2'), Rational(5, 18), Decimal('0.9'))]
        diam, depth, rad, a_par, f_len = random.choice(cases)
        
        diam_str = str(diam).replace('.', ',')
        depth_str = str(depth).replace('.', ',')
        rad_str = str(rad).replace('.', ',')
        f_str = str(f_len).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc chảo thu sóng vệ tinh có mặt cắt dọc qua tâm là một đường parabol $y = ax^2$ với đường kính miệng chảo là $%s$ m và độ sâu tại tâm chảo là $%s$ m. Để thu được tín hiệu tốt nhất, đầu thu (LNB) phải được đặt đúng tại tiêu điểm $F$ của parabol, biết rằng khoảng cách $f$ (tính bằng mét) từ đỉnh chảo $O$ đến tiêu điểm $F$ được xác định bởi công thức $f = \\frac{1}{4a}$. \\\\
a) Chọn hệ trục tọa độ $Oxy$ sao cho đỉnh chảo trùng với gốc tọa độ $O(0; 0)$ và trục tung $Oy$ là trục đối xứng hướng lên phía miệng chảo. Hãy tìm hệ số $a$. \\\\
b) Tính khoảng cách từ đỉnh chảo $O$ đến vị trí lắp đặt đầu thu $F$.'''
                         %(diam_str, depth_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $A$ và $B$ là hai điểm mép ngoài cùng của mặt cắt chảo thu sóng (với $B$ nằm bên phải trục $Oy$). \\\\
Vì đường kính miệng chảo là $%s$ m nên bán kính miệng chảo là $\\frac{%s}{2} = %s$ m. \\\\
Độ sâu tại tâm chảo là $%s$ m nên tọa độ điểm $B$ là $(%s; %s)$. \\\\
Thay $x = %s$ và $y = %s$ vào phương trình parabol $y = ax^2$, ta được: \\\\
$%s = a \\cdot (%s)^2 \\Rightarrow a = \\frac{%s}{(%s)^2} = %s$. \\\\
Vậy hệ số cần tìm là $a = %s$.
\\item Khoảng cách từ đỉnh chảo $O$ đến vị trí lắp đặt đầu thu $F$ là: \\\\
$f = \\frac{1}{4a} = \\frac{1}{4 \\cdot %s} = %s$ (m). \\\\
Vậy đầu thu phải được lắp đặt cách đỉnh chảo một khoảng bằng $%s$ mét. \\\\
\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.2,0) -- (3.2,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.6) -- (0,3.8) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.5:2.5] plot(\\x, {0.4*(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (A) at (-2.5,2.5);
\\coordinate (B) at (2.5,2.5);
\\coordinate (F) at (0,0.625);
\\draw[line width=1pt] (A)--(B);
\\draw[line width=1pt, dashed] (O)--(F);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (F) circle (1pt) node[right] {$F$};
\\end{tikzpicture}
\\end{center}
\\end{enumEX}'''
                   %(diam_str, diam_str, rad_str,
                     depth_str, rad_str, depth_str,
                     rad_str, depth_str,
                     depth_str, rad_str, depth_str, rad_str, latex(a_par),
                     latex(a_par),
                     latex(a_par), f_str,
                     f_str
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
