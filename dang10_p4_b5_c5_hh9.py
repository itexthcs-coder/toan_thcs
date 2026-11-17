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



def bt_dang10_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        OA = randint(2, 5)
        AB = 3 * randint(2, 4)
        OB = OA + AB
        R_ngoai = Rational(AB, 3)
        R_trong = AB

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (1.5,0);
\\coordinate (B) at (4.5,0);
\\draw[line width=1pt, ->] (O)--(6.5,0) node[below] {$x$};
\\draw[line width=1pt] (A) circle (1cm);
\\draw[line width=1pt] (B) circle (2cm);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[below] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Trên tia $Ox$ lấy hai điểm $A$ và $B$ sao cho $OA = %s\\text{ cm}$, $OB = %s\\text{ cm}$. Xét hai đường tròn $(A; R)$ và $(B; 2R)$ với $R > 0$.\\\\
        a) Tìm giá trị của $R$ để hai đường tròn $(A)$ và $(B)$ tiếp xúc ngoài; tiếp xúc trong.\\\\
        b) Tìm khoảng giá trị của $R$ để hai đường tròn $(A)$ và $(B)$ cắt nhau tại hai điểm phân biệt. %s'''
                         % (latex(OA), latex(OB), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Vì hai điểm $A$ và $B$ cùng nằm trên tia $Ox$ và $OA < OB$ ($%s\\text{ cm} < %s\\text{ cm}$) nên điểm $A$ nằm giữa $O$ và $B$.\\\\
        Suy ra khoảng cách hai tâm là $AB = OB - OA = %s - %s = %s\\text{ cm}$.\\\\
        Với $R > 0$, ta có bán kính của hai đường tròn thỏa mãn $2R > R$.\\\\
        - Hai đường tròn $(A; R)$ và $(B; 2R)$ tiếp xúc ngoài khi và chỉ khi:\\\\
        $AB = 2R + R \\Leftrightarrow 3R = %s \\Leftrightarrow R = %s\\text{ (cm)}$.\\\\
        - Hai đường tròn $(A; R)$ và $(B; 2R)$ tiếp xúc trong khi và chỉ khi:\\\\
        $AB = 2R - R \\Leftrightarrow R = %s\\text{ (cm)}$.
        \\item Hai đường tròn $(A; R)$ và $(B; 2R)$ cắt nhau tại hai điểm phân biệt khi và chỉ khi:\\\\
        $2R - R < AB < 2R + R \\Leftrightarrow R < %s < 3R$.\\\\
        Giải hệ bất phương trình $\\begin{cases} R < %s \\\\ 3R > %s \\end{cases} \\Leftrightarrow %s < R < %s$.\\\\
        Vậy với $%s\\text{ cm} < R < %s\\text{ cm}$ thì hai đường tròn cắt nhau tại hai điểm phân biệt.
        \\end{enumEX}'''
                   % (latex(OA), latex(OB), latex(OB), latex(OA), latex(AB),
                      latex(AB), latex(R_ngoai), latex(R_trong),
                      latex(AB), latex(AB), latex(AB), latex(R_ngoai), latex(R_trong),
                      latex(R_ngoai), latex(R_trong)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
