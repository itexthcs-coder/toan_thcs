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


def bt_dang19_p3_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r_ngoai = random.choice([10, 12, 14, 15, 16])
        r_trong = random.choice([4, 5, 6, 7])
        val = 5 * r_ngoai * r_trong * math.sin(math.radians(36))
        number = Decimal(str(val))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (126:0.75);
\\coordinate (B) at (54:0.75);
\\coordinate (C) at (-18:0.75);
\\coordinate (D) at (-90:0.75);
\\coordinate (E) at (198:0.75);
\\coordinate (P1) at (90:1.95);
\\coordinate (P2) at (18:1.95);
\\coordinate (P3) at (-54:1.95);
\\coordinate (P4) at (-126:1.95);
\\coordinate (P5) at (162:1.95);
\\draw[line width=1pt] (P1)--(B)--(P2)--(C)--(P3)--(D)--(P4)--(E)--(P5)--(A)--cycle;
\\draw[line width=1pt, dashed] (A)--(B)--(C)--(D)--(E)--cycle;
\\draw[line width=1pt, dashed] (O)--(P1) (O)--(B);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (P1) circle (1pt) node[above] {$P$};
\\fill (B) circle (1pt) node[right] {$B$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Để trang trí lớp học, bạn Nam gấp đôi một tờ giấy màu theo nếp gấp thẳng, vẽ một nửa hình ngôi sao năm cánh đều (có lõi bên trong là một ngũ giác đều) rồi cắt theo nét vẽ (như hình vẽ). Biết rằng khoảng cách từ tâm $O$ của ngôi sao đến mỗi đỉnh cánh sao bằng $%s\\text{ cm}$ và khoảng cách từ tâm $O$ đến mỗi đỉnh của ngũ giác đều lõi bên trong bằng $%s\\text{ cm}$. Tính tổng diện tích của cả hình ngôi sao năm cánh sau khi mở tờ giấy ra (đơn vị: $\\text{cm}^2$, làm tròn kết quả đến hàng đơn vị). %s'''
                         % (r_ngoai, r_trong, hinh_tikz))

        loigiai = ('''Do tính đối xứng quay của ngôi sao năm cánh đều quanh tâm $O$, hình ngôi sao được chia thành $10$ tam giác bằng nhau chung đỉnh $O$ (như $\\triangle OPB$). \\
Mỗi tam giác có hai cạnh xuất phát từ $O$ là $OP = %s\\text{ cm}$, $OB = %s\\text{ cm}$ và góc ở tâm $\\widehat{POB} = \\frac{360^\\circ}{10} = 36^\\circ$. \\
Diện tích của mỗi tam giác nhỏ là:
$$S_{\\triangle OPB} = \\frac{1}{2} OP \\cdot OB \\cdot \\sin 36^\\circ = \\frac{1}{2} \\cdot %s \\cdot %s \\cdot \\sin 36^\\circ = %s \\sin 36^\\circ\\text{ (cm}^2\\text{)}.$$
Vậy tổng diện tích của cả hình ngôi sao năm cánh là:
$$S = 10 \\cdot %s \\sin 36^\\circ = %s \\sin 36^\\circ \\approx %s\\text{ (cm}^2\\text{)}.$$'''
                   % (r_ngoai, r_trong, r_ngoai, r_trong, r_ngoai * r_trong // 2, r_ngoai * r_trong // 2, 5 * r_ngoai * r_trong, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
