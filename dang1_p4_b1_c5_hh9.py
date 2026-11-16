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


def bt_dang1_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m0 = random.randint(4, 7)
        R0 = 2 * m0 - 3
        oa = R0 - 2
        ob = R0
        oc = R0 + 2
        m_min = (oa + 3) // 2 + 1
        m_max = (oc + 3) // 2 if (oc + 3) % 2 != 0 else (oc + 3) // 2 - 1
        tap_m = '; '.join(str(i) for i in range(m_min, m_max + 1))

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (1.1,0);
\\coordinate (B) at (45:1.7);
\\coordinate (C) at (2.4,0);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (O)--(B) node[midway, above left] {$R$};
\\draw[line width=1pt] (O)--(C);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[below] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho đường tròn $(O; 2m - 3)$ (với $m > \\dfrac{3}{2}$) và ba điểm $A, B, C$ sao cho $OA = %s\\text{ cm}$, $OB = %s\\text{ cm}$, $OC = %s\\text{ cm}$ (minh họa như hình vẽ). \\\\
a) Với $m = %s$, hãy xác định vị trí của mỗi điểm $A, B, C$ đối với đường tròn $(O)$. \\\\
b) Tìm tất cả các giá trị nguyên của $m$ để điểm $A$ nằm bên trong đường tròn $(O)$ đồng thời điểm $C$ nằm bên ngoài đường tròn $(O)$.
%s''' % (oa, ob, oc, m0, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Với $m = %s$, bán kính của đường tròn là $R = 2 \\cdot %s - 3 = %s\\text{ cm}$.\\\\
So sánh khoảng cách từ tâm $O$ đến các điểm $A, B, C$ với bán kính $R = %s\\text{ cm}$:\\\\
- Vì $OA = %s\\text{ cm} < %s\\text{ cm}$ nên điểm $A$ nằm trong đường tròn $(O)$.\\\\
- Vì $OB = %s\\text{ cm} = R$ nên điểm $B$ nằm trên đường tròn $(O)$.\\\\
- Vì $OC = %s\\text{ cm} > %s\\text{ cm}$ nên điểm $C$ nằm ngoài đường tròn $(O)$.
\\item Để điểm $A$ nằm bên trong đường tròn $(O)$ và điểm $C$ nằm bên ngoài đường tròn $(O)$ thì khoảng cách từ $O$ đến $A, C$ phải thỏa mãn:\\\\
$OA < R < OC \\Leftrightarrow %s < 2m - 3 < %s \\Leftrightarrow %s < 2m < %s \\Leftrightarrow %s < m < %s$.\\\\
Vì $m$ là số nguyên nên $m \\in \\{%s\\}$.
\\end{enumEX}''' % (m0, m0, R0, R0, oa, R0, ob, oc, R0, oa, oc, oa + 3, oc + 3, Rational(oa + 3, 2), Rational(oc + 3, 2), tap_m))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
